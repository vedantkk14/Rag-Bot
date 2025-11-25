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
