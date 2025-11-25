# 🤖 UniMate AI – Smart Assistant for Students

UniMate AI is a powerful learning assistant designed to help students interact with documents,  
ask questions intelligently, generate quizzes, perform web-assisted searches,  
and download their full AI conversation as a formatted PDF.

---

## 🌟 Features

### 🔍 PDF-Based Question Answering (RAG)
- Upload any PDF  
- Extract content and embed it using modern sentence-transformer models  
- Build a FAISS vector store for retrieval  
- Ask precise questions about the document

### 💬 Conversational AI
- Natural, friendly, context-aware chat  
- Uses high-quality HuggingFace Inference models  
- Maintains chat history for contextual replies

### 🌐 Web Search Fallback
If the AI model doesn’t know something, UniMate AI automatically:
- Performs a Google Custom Search  
- Merges results into a helpful answer  
- Ensures accurate, up-to-date information

### 📝 Quiz Generator
- Automatically generates MCQs from your last few messages  
- Useful for revision and testing understanding

### 📄 Export Chat to PDF
- Clean and beautifully formatted export  
- Includes message styling  
- Timestamped output

### 🎨 Simple User Interface
- Chat panel  
- PDF upload sidebar  
- Quiz section  
- Download tools  
- About panel  

---

## 🧠 Tech Stack

- **Python**
- **LangChain (prompting, runnables, messaging)**
- **HuggingFace Inference Endpoints**
- **FAISS (vector similarity search)**
- **pypdf (PDF text extraction)**
- **ReportLab (PDF generation)**
- **Google Custom Search API**
- **dotenv (environment variables)**

---

## 🔧 Installation

```bash
git clone <your-repo-url>
cd <your-folder>
pip install -r requirements.txt
```

(Optional) Create and activate a virtual environment first.

---

## 🔐 Environment Variables

Create a `.env` file with:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
GOOGLE_API_KEY=your_api_key_here
GOOGLE_CSE_ID=your_custom_search_engine_id
```

---

## 📂 Project Structure

```
/
├── Home.py                    # Main app
├── pages/                     # Additional UI pages (if used)
├── vectordb/                  # (Optional) Prebuilt FAISS database
├── requirements.txt           # Dependencies
├── runtime.txt                # Python version pin
└── .env.example               # Example environment variables
```

---

## ▶️ How to Use

1. Start the application  
2. Upload a PDF to enable document-based answering  
3. Ask any question—general or PDF-specific  
4. Generate quizzes based on your chat  
5. Download your conversation as a formatted PDF

---

## 🧩 Troubleshooting

- Make sure your environment variables are set  
- Check for missing Python packages with:  
  ```bash
  pip install -r requirements.txt
  ```
- Ensure your vector DB loads correctly  
- If running online, verify deployment uses Python 3.10 or 3.11  

---

## 🚀 Roadmap

- Support for multiple PDFs at once  
- Enhanced quiz formatting  
- Better web-search summarization  
- More PDF export options  
- Dark mode UI  

---

## 📜 License
Add your license details here.

