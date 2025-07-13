# 📰 News Research Tool

A user-friendly and intelligent news research tool designed for effortless information retrieval and question answering based on financial and stock market-related news articles — specifically tailored for Sri Lankan markets.

---

## 🚀 Features

- 🔗 Load one or more article URLs or upload a file containing URLs.
- 📄 Extract article content using **LangChain's UnstructuredURLLoader**.
- 🧠 Generate semantic embeddings using **OpenAI Embeddings**.
- 🔍 Use **FAISS** for fast similarity-based retrieval of relevant information.
- 💬 Ask questions and get answers along with **source references** using powerful LLMs (like GPT).
- 💾 Vector index is cached locally for reuse and performance.

---

## ⚙️ Installation

1. **Clone this repository**:

```bash
git clone https://github.com/nazikanshaffAM/news-researcher-LLM.git
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set your OpenAI API key**:

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶️ Usage

1. **Run the Streamlit app**:

```bash
streamlit run main.py
```

2. **In the web interface**:

- Paste news article URLs in the sidebar.
- Click **"Process URLs"** to load and embed the content.
- Ask any question related to the articles.
- Get concise answers and links to the sources used.

---

## 📁 Project Structure

```bash
news-researcher-LLM/
│
├── main.py                # Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # API key (not committed to Git)
├── faiss_index/           # (Auto-created) Local FAISS vector store
└── Notebooks/             # Jupyter notebooks for experiments (optional)
```

---

## 📌 Example Questions

Once the tool has processed the articles, try asking:

- *What is the current performance of Sri Lanka’s banking sector?*
- *What are the top gainers in the CSE today?*
- *How has foreign investment influenced recent market trends?*

---

## 📬 Contact

Developed by **Anshaff Ameer**  

