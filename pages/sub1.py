import os
import re
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import streamlit as st


def chat_model():
    llm = HuggingFaceEndpoint(
        repo_id='Qwen/Qwen2.5-7B-Instruct',
        task='text-generation',
        temperature=0.8,
        max_new_tokens=512
    )
    return ChatHuggingFace(llm=llm)

def get_embeddings():
    return HuggingFaceEmbeddings(
        model='sentence-transformers/all-MiniLM-L6-v2',
    )

def clean_text(text):
    """Clean text while preserving SQL-relevant characters"""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s.,!?:;\-=<>()\'"*/+]', '', text)
    text = re.sub(r'(.)\1{3,}', r'\1', text)
    return text.strip()

def load_and_create_vectordb():
    """Load PDF, clean text, create chunks, and build FAISS vector database"""
    loader = PyPDFLoader(file_path='dbms_tb.pdf')
    docs = loader.load()
    
    for doc in docs:
        doc.page_content = clean_text(doc.page_content)
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=250
    )
    chunks = splitter.split_documents(docs)
    
    embeddings = get_embeddings()
    vectordb = FAISS.from_documents(chunks, embeddings)
    
    return vectordb

def main():
    load_dotenv()
    st.set_page_config(page_title="DBMS Chatbot 🤖", layout="wide")
    st.title("📘 DBMS Chatbot")

    with st.sidebar:

        st.markdown("### 🎛️ Chat Controls")
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()

    # Initialize session state with page-specific keys
    if "dbms_messages" not in st.session_state:
        st.session_state.dbms_messages = []
    if "dbms_chat_history" not in st.session_state:
        st.session_state.dbms_chat_history = []
    if "dbms_vectordb" not in st.session_state:
        with st.spinner("Loading DBMS knowledge base..."):
            st.session_state.dbms_vectordb = load_and_create_vectordb()
        st.success("Knowledge base loaded!")

    # User input at the bottom (placed before chat display)
    user_input = st.chat_input("Ask anything about DBMS")

    if user_input:
        # Add user message to messages
        st.session_state.dbms_messages.append({"role": "user", "content": user_input})
        
        # Capture chat history before building the chain
        current_chat_history = st.session_state.dbms_chat_history.copy()
        
        # Check if it's a casual greeting
        casual_greetings = ['hi', 'hello', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening']
        is_casual = any(greeting in user_input.lower().strip() for greeting in casual_greetings)
        
        if is_casual and len(user_input.split()) <= 3:
            # Handle casual conversation without RAG
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a friendly DBMS expert assistant. Respond warmly to greetings."),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}")
            ])
            
            chain = (
                {
                    "chat_history": lambda _: current_chat_history,
                    "question": RunnablePassthrough()
                }
                | prompt
                | chat_model()
            )
            
            with st.spinner("Thinking..."):
                response = chain.invoke(user_input)
                answer = response.content
        else:
            # Use RAG for DBMS-related questions
            retriever = st.session_state.dbms_vectordb.as_retriever(
                search_type="similarity",
                search_kwargs={"k": 3}
            )
            
            prompt = ChatPromptTemplate.from_messages([
                ("system", """You are an expert AI assistant who has mastered Database Management Systems (DBMS).
Answer the question using the context extracted from the DBMS textbook and the previous conversation.

Guidelines for your response:
- Provide a **detailed yet concise** explanation.
- Use **clear, simple, and structured** language.
- If the answer is **not present** in the context, respond only with: "I don't have enough information in the knowledge base to answer this question."
- Do not add unrelated information beyond what is asked.

--- 
DBMS Context:
{context}"""),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}")
            ])
            
            rag_chain = (
                {
                    "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
                    "chat_history": lambda _: current_chat_history,
                    "question": RunnablePassthrough()
                }
                | prompt
                | chat_model()
            )

            with st.spinner("Thinking..."):
                response = rag_chain.invoke(user_input)
                answer = response.content
        
        # Add to chat_history as LangChain message objects
        st.session_state.dbms_chat_history.append(HumanMessage(content=user_input))
        st.session_state.dbms_chat_history.append(AIMessage(content=answer))
        
        # Add assistant response to display messages
        st.session_state.dbms_messages.append({"role": "assistant", "content": answer})
        
        # Rerun to update chat display
        st.rerun()

    # Display chat history with custom UI
    st.markdown("---")
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.dbms_messages:
            if message["role"] == "user":
                st.markdown(f"""
                <div style='text-align: right; margin: 10px 0;'>
                    <div style='color: #666; font-size: 12px; margin-bottom: 5px;'>👤 You</div>
                    <span style='background-color: #007bff; color: white; padding: 10px 15px; 
                    border-radius: 15px; display: inline-block; max-width: 70%;'>
                        {message["content"]}
                    </span>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style='text-align: left; margin: 10px 0;'>
                    <div style='color: #666; font-size: 12px; margin-bottom: 5px;'>🤖 Assistant</div>
                    <span style='background-color: #f1f1f1; color: black; padding: 10px 15px; 
                    border-radius: 15px; display: inline-block; max-width: 70%;'>
                        {message["content"]}
                    </span>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()