# 📚 Generative AI – Intelligent Multi-Document RAG System
### Intelligent Multi-Document Retrieval-Augmented Generation (RAG) System

DocuMind AI is an AI-powered document intelligence application that allows users to upload multiple PDF documents and interact with them through natural-language conversations.

Built using **Retrieval-Augmented Generation (RAG)**, the application retrieves relevant information from uploaded documents and uses Google's Gemini model to generate context-aware answers with source references.

Instead of manually searching through lengthy documents, users can simply ask questions and receive relevant answers grounded in their uploaded files.

---

## 🚀 Features

- **Multi-PDF Upload:** Upload and process multiple PDF documents simultaneously.
- **Intelligent Document Processing:** Extract text from PDFs and split it into manageable chunks.
- **Semantic Search:** Retrieve relevant document sections using Hugging Face embeddings and FAISS.
- **AI-Powered Question Answering:** Generate contextual responses using Google Gemini.
- **Source References:** Display the original document name and page number associated with retrieved information.
- **Conversational Memory:** Maintain recent conversation history to support follow-up questions.
- **Context-Aware Responses:** Answer questions using retrieved document content.
- **Information Grounding:** Instruct the LLM not to invent information when the answer is unavailable in the uploaded documents.
- **Interactive Interface:** Simple Streamlit interface for document management and conversations.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Google Gemini 3.6 Flash |
| LLM Framework | LangChain |
| PDF Processing | PyPDF |
| Text Splitting | RecursiveCharacterTextSplitter |
| Embedding Model | all-MiniLM-L6-v2 |
| Vector Database | FAISS |
| Embedding Integration | Hugging Face |
| Environment Management | Python dotenv |

---

## 🏗️ System Architecture

```text
             PDF Documents
                    |
                    v
          Document Extraction
               (PyPDF)
                    |
                    v
             Text Splitting
       (RecursiveCharacterTextSplitter)
                    |
                    v
             Text Embeddings
          (Hugging Face Model)
                    |
                    v
             FAISS Vector Store
                    |
                    |
 User Question ----+
                    |
                    v
          Semantic Retrieval
                    |
                    v
          Relevant Document Chunks
                    |
                    v
         Conversation History
                    |
                    v
           Google Gemini LLM
                    |
                    v
          Contextual AI Response
                    |
                    v
          Answer + Source References
                    |
                    v
             Streamlit UI
```

---

## 📂 Project Structure

```text
DocuMind-AI/
│
├── app.py                  # Streamlit application
├── config.py               # Application configuration
├── document_processor.py   # PDF extraction and text splitting
├── vector_store.py         # Embedding generation and FAISS retrieval
├── rag_pipeline.py         # RAG pipeline and Gemini integration
│
├── data/
│   └── sample_pdfs/        # Sample PDF documents
│
├── .env                    # API key configuration
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone 
cd Multi-Document-RAG-System
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Google Gemini API

Get your API key from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Keep your API key private. Never commit your `.env` file to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💬 How to Use

1. Launch DocuMind AI.
2. Open the sidebar and upload one or more PDF documents.
3. Click **Process Documents**.
4. Wait for document extraction, chunking, embedding generation, and vector indexing to complete.
5. Enter a natural-language question in the chat interface.
6. Review the generated answer.
7. Expand the **View Sources** section to see the referenced document names and page numbers.
8. Ask follow-up questions to continue the conversation.

---

## ⚡ RAG Configuration

The following parameters control document processing and retrieval:

| Parameter | Value |
|---|---:|
| Chunk Size | 1000 |
| Chunk Overlap | 200 |
| Top-K Retrieval | 4 |
| Embedding Model | all-MiniLM-L6-v2 |
| LLM | Gemini 2.5 Flash |
| Temperature | 0.2 |

**Document Chunking:** Documents are divided into smaller overlapping chunks to preserve context and improve retrieval.

**Embedding Generation:** Each chunk is converted into a numerical vector using the Hugging Face embedding model.

**Semantic Retrieval:** FAISS performs similarity search to identify the most relevant chunks for a user query.

**Response Generation:** Gemini receives the retrieved context, conversation history, and current question to generate a grounded response.

---

## 🧪 Example Questions

After uploading the sample reports, try asking:

- What was the company's total revenue in FY 2025–26?
- Which business segment contributed the most revenue?
- What was the company's operating profit margin?
- What is the Recovery Time Objective (RTO)?
- How does the workflow software segment perform?
- What were the company's priorities for FY 2026–27?

You can also ask follow-up questions to explore information across multiple documents.

---

## 🔒 Limitations and Future Improvements

Current implementation:
- Supports text-based PDF documents.
- Uses in-memory FAISS indexing.
- Maintains conversation history within the active Streamlit session.
- Retrieves a fixed number of relevant document chunks.
- Uses prompt-based grounding for unavailable information.

Planned improvements:
- Persistent vector database storage.
- Improved conversational query rewriting for follow-up questions.
- Retrieval relevance scoring and confidence thresholds.
- Advanced source-level citations and highlighted document passages.
- Support for scanned PDFs using OCR.
- Document-level filtering and deletion.
- More robust evaluation of retrieval accuracy and answer faithfulness.
- Deployment with scalable document storage.

---

## 👨‍💻 Author

**Deepanshu Kumar**

B.Tech – Data Science

Interested in Artificial Intelligence, Machine Learning, Generative AI, and building practical AI-powered applications.

**GitHub:** [DeepanshuKumar09](https://github.com/DeepanshuKumar09)

---

## 📄 License

This project is developed for educational and portfolio purposes. You may modify and extend it with appropriate attribution.