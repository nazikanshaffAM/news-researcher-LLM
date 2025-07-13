import os
import streamlit as st
import time

from langchain.chains import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI

from dotenv import load_dotenv
load_dotenv()  # Load environment variables (like OPENAI_API_KEY)

# --- Streamlit UI ---
st.set_page_config(page_title="News Research Tool", page_icon="📰", layout="wide")
st.title("📰 News Research Tool")
st.markdown("Effortlessly research news articles with AI-powered Q&A and source tracking.")

st.sidebar.header("🔗 Enter News Article URLs")
url_count = st.sidebar.number_input(
    "How many URLs do you want to input?", min_value=1, max_value=10, value=3, step=1, key="url_count"
)
urls = []
for i in range(url_count):
    url = st.sidebar.text_input(f"URL {i+1}", key=f"url_{i}")
    if url:
        urls.append(url)

process_url_clicked = st.sidebar.button("🚀 Process URLs")
faiss_path = "faiss_index"
main_placeholder = st.empty()


# Initialize LLM
llm = OpenAI(temperature=0.9, max_tokens=500)

# --- Main Processing ---
if process_url_clicked and urls:
    with st.spinner("Loading data from URLs..."):
        loader = WebBaseLoader(urls)
        data = loader.load()
    st.success("✅ Data loaded successfully!")

    with st.spinner("Splitting text into chunks..."):
        text_splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000,
            chunk_overlap=100
        )
        docs = text_splitter.split_documents(data)
    st.success("✅ Text split into chunks!")

    with st.spinner("Building embedding vector..."):
        embeddings = OpenAIEmbeddings()
        vectorstore_openai = FAISS.from_documents(docs, embeddings)
        time.sleep(1)
        vectorstore_openai.save_local(faiss_path)
    st.success("✅ Embedding vector built and saved!")

st.markdown("---")

# --- Question Input & Answer Section ---
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("❓ Ask a Question")
    query = st.text_input("Type your question about the articles:", key="question_input")
    ask_button = st.button("🔍 Get Answer", key="ask_button")

with col2:
    if ask_button and query and os.path.exists(faiss_path):
        with st.spinner("Retrieving answer..."):
            embeddings = OpenAIEmbeddings()
            vectorstore = FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)
            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )
            result = chain({"question": query}, return_only_outputs=True)
            st.success("✅ Answer retrieved!")

        st.header("📝 Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("🔗 Sources")
            with st.expander("Show Sources"):
                sources_list = [s for s in sources.split("\n") if s.strip()]
                for idx, source in enumerate(sources_list, 1):
                    st.markdown(f"{idx}. {source}")
    elif ask_button and not os.path.exists(faiss_path):
        st.error("❌ Please process URLs first before asking a question.")


