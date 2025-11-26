<<<<<<< HEAD
🌟 UniMate AI
Your Intelligent Academic Companion — Chat, Analyze PDFs, Generate Quizzes & More
<p align="center"> <img src="https://img.shields.io/badge/Python-3.10%2B-blue" /> <img src="https://img.shields.io/badge/AI-Powered-yellow" /> <img src="https://img.shields.io/badge/FAISS-Vector%20Search-blueviolet" /> <img src="https://img.shields.io/badge/HuggingFace-Models-orange" /> <img src="https://img.shields.io/badge/License-MIT-green" /> </p>
🎯 What is UniMate AI?

UniMate AI is a smart, AI-powered academic assistant designed to enhance student productivity and learning.
It helps users:

Ask general questions

Analyze & extract information from PDFs

Use retrieval-based answering (RAG)

Perform web-assisted searches

Generate quizzes from conversation history

Export full conversations as beautifully formatted PDFs

Chat naturally with context-aware memory

Whether you're studying, researching, or revising — UniMate AI acts as your personal academic companion.

🚀 Features Overview
🔍 1. Intelligent PDF Question Answering (RAG)

Upload any PDF and ask contextual questions about its content.
The system automatically:

Extracts & cleans text from the PDF

Splits it into manageable chunks

Embeds using HuggingFace sentence-transformers

Stores vectors using FAISS

Retrieves relevant sections to answer your queries

✨ Perfect for textbooks, notes, assignments & academic papers.

💬 2. Contextual Conversational AI

Ask anything — UniMate AI provides:

Friendly and natural responses

Structured, concise explanations

Memory-aware conversation flow

Domain knowledge via LLMs

✨ Designed to feel like a personal tutor.

🌐 3. Smart Web Search Fallback

If the model doesn't know something:

Google Custom Search API is triggered

Relevant results are summarized

AI blends results into a clean, structured answer

✨ Ensures accurate and up-to-date responses.

📝 4. Automated Quiz Generator

From your recent chat:

Generates 5 MCQs

Includes 4 options each

Returns correct answers

Great for quick revision

✨ Convert learning into active practice instantly.

📄 5. Export Chat as PDF

Download the entire conversation:

Styled layout

Timestamps

Clean formatting using ReportLab

User vs Assistant message design

✨ Useful for revision, sharing, or saving study notes.

🎨 6. Clean and User-Friendly Interface

Sidebar tools

PDF upload panel

Chat layout with colored message bubbles

Quiz section

Helpful utilities such as clearing chat or exporting

✨ Optimized for simplicity and smooth experience.

🧠 Tech Stack
AI & NLP

LangChain (chains, prompts, runnables)

HuggingFace Inference Models

sentence-transformers embeddings

Vector Search

FAISS (efficient similarity search)

Document Processing

pypdf for PDF text extraction

ReportLab for generating PDF exports

APIs

Google Custom Search API for reliable fallback answers

HuggingFace Hub for LLMs & embeddings

Environment Management

dotenv

Python 3.10+

📂 Folder Structure
/
├── Home.py                    # Main application script
├── pages/                     # Optional additional pages
├── vectordb/                  # Vector database files (if stored locally)
├── requirements.txt           # Project dependencies
├── runtime.txt                # Python version pin (e.g., python-3.10.13)
├── .env.example               # Template for environment variables
└── README.md                  # Project documentation

🔧 Installation Guide
1️⃣ Clone the repository
git clone <repo-url>
cd <project-folder>

2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add environment variables

Create a .env file:

HUGGINGFACEHUB_API_TOKEN=your_token_here
GOOGLE_API_KEY=your_google_key
GOOGLE_CSE_ID=your_search_engine_id

▶️ How to Run
python Home.py


Then open the provided local URL in your browser.

📝 Usage Guide
📥 Upload a PDF

Load any academic or informational PDF.

❓ Ask Questions

Use natural language to ask questions about:

The PDF

General knowledge

Academic concepts

🔎 View AI Responses

Responses are:

Friendly

Structured

Context-aware

🎯 Generate Quizzes

Convert your recent conversation into multiple-choice questions.

📄 Export Conversation

Download a PDF summary of your entire session.

🧩 Troubleshooting
❗ Missing Embeddings / FAISS Errors

Ensure sentence-transformers & FAISS are installed correctly.

❗ No PDF Text Extracted

The PDF may contain only images; ensure it's text-based.

❗ Web Search Not Working

Double-check:

GOOGLE_API_KEY
GOOGLE_CSE_ID

❗ LLM Not Responding

Ensure your:

HUGGINGFACEHUB_API_TOKEN


is valid and active.

🌱 Roadmap

 Multi-PDF processing

 Conversation bookmarking

 Document summarization mode

 Themed UI (light/dark/custom themes)

 Multi-language support

 Integration with online storage for PDFs
=======

# 💻 Tech Stack:
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white) ![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![mlflow](https://img.shields.io/badge/mlflow-%23d9ead3.svg?style=for-the-badge&logo=numpy&logoColor=blue) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Scipy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows Terminal](https://img.shields.io/badge/Windows%20Terminal-%234D4D4D.svg?style=for-the-badge&logo=windows-terminal&logoColor=white)
# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=vedantkk14&theme=dark&hide_border=false&include_all_commits=false&count_private=false)<br/>
![](https://nirzak-streak-stats.vercel.app/?user=vedantkk14&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=vedantkk14&theme=dark&hide_border=false&include_all_commits=false&count_private=false&layout=compact)

## 🏆 GitHub Trophies
![](https://github-profile-trophy.vercel.app/?username=vedantkk14&theme=radical&no-frame=false&no-bg=true&margin-w=4)

### ✍️ Random Dev Quote
![](https://quotes-github-readme.vercel.app/api?type=horizontal&theme=radical)

---
[![](https://visitcount.itsvg.in/api?id=vedantkk14&icon=0&color=0)](https://visitcount.itsvg.in)

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->
>>>>>>> a9b1a95 (some changes)
