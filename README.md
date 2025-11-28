<div align="center">

# 🎓 UniMate AI - Your AI-Powered Study Companion

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.1%2B-green.svg)

### *A Retrieval-Augmented Generation (RAG) chatbot designed to help engineering students study smarter, not harder.*

</div>

---

## 🚀 Overview

<table>
<tr>
<td width="50%">

### The Problem 😰
Engineering students often find themselves cramming the night before exams, struggling to navigate dense textbooks and scattered resources.

</td>
<td width="50%">

### The Solution ✨
UniMate AI combines the power of Large Language Models with course-specific knowledge bases to provide instant, accurate answers with intelligent fallback mechanisms.

</td>
</tr>
</table>

---

## ✨ Key Features

<table>
<tr>
<td width="50%" valign="top">

### 📚 Multi-Subject Support
<ul>
<li><b>6 Pages Total:</b> 1 General Chatbot + 5 Subject-Specific Pages</li>
<li><b>Pre-loaded subjects:</b> AI, DBMS, HCI, WT, CN</li>
<li>Upload your own PDFs for custom RAG sessions</li>
</ul>

### 🧠 Smart RAG Pipeline
<ul>
<li>Vector embeddings stored in FAISS database</li>
<li>Semantic similarity search for accurate retrieval</li>
<li>Context-aware responses using LangChain</li>
<li>Conversation memory throughout the session</li>
</ul>

### 🌐 Intelligent Fallback
<ul>
<li>Automatic Google Search API integration</li>
<li>No more "I don't know" responses</li>
<li>Seamless transition between knowledge base and web search</li>
</ul>

</td>
<td width="50%" valign="top">

### 📝 Interactive Learning Tools
<ul>
<li><b>Auto-Generated Quizzes:</b> Creates MCQs based on your conversation history</li>
<li><b>PYQ Analysis:</b> Extracts and analyzes Previous Year Questions with frequency tracking</li>
<li><b>PDF Export:</b> Download entire chat sessions as formatted study notes</li>
</ul>

### 🎯 User-Friendly Interface
<ul>
<li>Clean, intuitive Streamlit UI</li>
<li>Real-time chat bubbles</li>
<li>Sidebar controls for quick actions</li>
<li>Mobile-responsive design</li>
</ul>

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

<table>
<thead>
<tr>
<th>Component</th>
<th>Technology</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>Framework</b></td>
<td>Streamlit</td>
</tr>
<tr>
<td><b>LLM</b></td>
<td>Meta Llama 3.1 (via HuggingFace)</td>
</tr>
<tr>
<td><b>Orchestration</b></td>
<td>LangChain</td>
</tr>
<tr>
<td><b>Embeddings</b></td>
<td>sentence-transformers/all-MiniLM-L6-v2</td>
</tr>
<tr>
<td><b>Vector DB</b></td>
<td>FAISS</td>
</tr>
<tr>
<td><b>Search API</b></td>
<td>Google Search API</td>
</tr>
<tr>
<td><b>PDF Processing</b></td>
<td>PyPDF, ReportLab</td>
</tr>
<tr>
<td><b>Language</b></td>
<td>Python 3.8+</td>
</tr>
</tbody>
</table>

</div>

---

## 📦 Installation

<details>
<summary><b>📋 Prerequisites</b></summary>
<br>

- Python 3.8 or higher
- pip package manager
- HuggingFace API token
- Google Search API key

</details>

<details open>
<summary><b>🚀 Quick Start Guide</b></summary>
<br>

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/unimate-ai.git
cd unimate-ai
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the root directory:
```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CSE_ID=your_custom_search_engine_id_here
```

### Step 5: Prepare Your Data
Place your subject PDF files in the `pdfs/` directory:
```
pdfs/
├── ai_tb.pdf
├── dbms_tb.pdf
├── hci_tb.pdf
├── wt_tb.pdf
└── cn_tb.pdf
```

### Step 6: Run the Application
```bash
streamlit run Home.py
```

<div align="center">
<b>🎉 The app will open in your browser at <code>http://localhost:8501</code></b>
</div>

</details>

---

## 📂 Project Structure

<details>
<summary><b>📁 Click to expand file structure</b></summary>

```
unimate-ai/
│
├── Home.py                 # Main landing page with general chatbot
├── pages/
│   ├── AI.py              # Artificial Intelligence subject page
│   ├── DBMS.py            # Database Management Systems page
│   ├── HCI.py             # Human-Computer Interaction page
│   ├── WT.py              # Web Technologies page
│   └── CN.py              # Computer Networks page
│
├── pdfs/                  # Textbook PDFs for each subject
│   ├── ai_tb.pdf
│   ├── dbms_tb.pdf
│   └── ...
│
├── pyq_pdfs/              # Previous Year Question papers
│   ├── ai/
│   ├── dbms/
│   └── ...
│
├── PYQs/                  # Processed PYQ JSON files
│   └── pyqs_master_ai.json
│
├── vectordb/              # FAISS vector databases
│   ├── ai_faiss/
│   ├── dbms_faiss/
│   └── ...
│
├── .env                   # Environment variables (not in repo)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License
```

</details>

---

## 🎯 How It Works

<div align="center">

### 🔄 RAG Pipeline Architecture

</div>

<table>
<tr>
<td width="25%" align="center">
<h4>1️⃣ Document Processing</h4>
<ul align="left">
<li>Load PDFs</li>
<li>Split into chunks</li>
<li>Generate embeddings</li>
<li>Store in FAISS</li>
</ul>
</td>
<td width="25%" align="center">
<h4>2️⃣ Query Processing</h4>
<ul align="left">
<li>User asks question</li>
<li>Convert to embedding</li>
<li>Similarity search</li>
<li>Retrieve top-k docs</li>
</ul>
</td>
<td width="25%" align="center">
<h4>3️⃣ Response Generation</h4>
<ul align="left">
<li>Combine context</li>
<li>Add chat history</li>
<li>Send to LLM</li>
<li>Generate answer</li>
</ul>
</td>
<td width="25%" align="center">
<h4>4️⃣ Fallback</h4>
<ul align="left">
<li>Check confidence</li>
<li>Trigger web search</li>
<li>Process results</li>
<li>Return answer</li>
</ul>
</td>
</tr>
</table>

<div align="center">

```
User Query → Embedding → Similarity Search → Context Retrieval → LLM → Response
                                    ↓ (if confidence < threshold)
                              Google Search → LLM → Response
```

</div>

---

## 💡 Usage Examples

<table>
<tr>
<td width="50%">

### 💬 Basic Chat
```
User: "What is normalization in DBMS?"

Bot: [Retrieves from DBMS textbook 
     and explains with examples]
```

### 📝 Quiz Generation
<ol>
<li>Chat about a topic</li>
<li>Click "Generate Quiz from Chat"</li>
<li>Take the auto-generated MCQ quiz</li>
<li>Get instant feedback and score</li>
</ol>

</td>
<td width="50%">

### 📊 PYQ Analysis
<ol>
<li>Navigate to subject page</li>
<li>Click "Analyze PYQ Papers"</li>
<li>View questions by frequency</li>
<li>Focus on high-frequency topics</li>
</ol>

### 📄 PDF Export
<ol>
<li>Have a conversation</li>
<li>Click "Download as PDF"</li>
<li>Save for offline study</li>
</ol>

</td>
</tr>
</table>

---

## 🔧 Configuration

<details>
<summary><b>⚙️ Customization Options</b></summary>
<br>

### Adjusting Chunk Size
```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # Adjust based on your content
    chunk_overlap=250     # Overlap for context continuity
)
```

### Changing LLM Model
```python
repo_id = 'meta-llama/Meta-Llama-3.1-8B-Instruct'  # Change to your preferred model
```

### Adjusting Retrieval Parameters
```python
retriever = vectordb.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}  # Number of documents to retrieve
)
```

</details>

---

## 🐛 Troubleshooting

<table>
<thead>
<tr>
<th>Issue</th>
<th>Solution</th>
</tr>
</thead>
<tbody>
<tr>
<td>Vector database not loading</td>
<td>Delete the <code>vectordb/</code> folder and restart the app</td>
</tr>
<tr>
<td>Google Search not working</td>
<td>Verify your API keys in <code>.env</code> file</td>
</tr>
<tr>
<td>LLM responses are slow</td>
<td>Use a smaller model or adjust <code>temperature</code> parameter</td>
</tr>
<tr>
<td>Out of memory errors</td>
<td>Reduce <code>chunk_size</code> or process fewer documents</td>
</tr>
</tbody>
</table>

---
</div>

<!--
 ## 📸 Screenshots
 
 <table>
 <tr>
 <td width="50%">
 <h3 align="center">🏠 Home Page</h3>
 <img src="screenshots/home.png" alt="Home Page"/>
 </td>
 <td width="50%">
 <h3 align="center">💬 Subject Chat</h3>
 <img src="screenshots/chat.png" alt="Chat Interface"/>
 </td>
 </tr>
 <tr>
 <td width="50%">
 <h3 align="center">📝 Quiz Generation</h3> 
 <img src="screenshots/quiz.png" alt="Quiz Feature"/>
 </td>
 <td width="50%">
 <h3 align="center">📊 PYQ Analysis</h3>
 <img src="screenshots/pyq.png" alt="PYQ Dashboard"/>
 </td>
 </tr>
 </table>
-->

<div align="center">


**If you found this helpful, please consider giving it a ⭐ on GitHub!**

<br>

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/unimate-ai&type=Date)](https://star-history.com/#yourusername/unimate-ai&Date)

</div>
