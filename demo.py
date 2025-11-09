from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint, HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader

# ✅ LLM Model (HuggingFace Endpoint)
def chat_model():
    llm = HuggingFaceEndpoint(
        repo_id="openai/gpt-oss-20b",
        task="text-generation",
        temperature=0.5,
        max_new_tokens=512
    )
    return ChatHuggingFace(llm=llm)

# ✅ Embedding model
def get_embeddings():
    return HuggingFaceEmbeddings(
        model='sentence-transformers/all-MiniLM-L6-v2'
    )

# ✅ MAIN APP
def main():
    load_dotenv()
    st.set_page_config(page_title="Home Page")
    st.set_page_config(page_title="Ask your PDF 💬", layout="wide")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "knowledge_base" not in st.session_state:
        st.session_state.knowledge_base = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    st.header("📄 PDF Chatbot")
    
    # Sidebar with PDF upload and controls
    with st.sidebar:
        
        # PDF Upload Section
        st.markdown("### 📁 Upload Document")
        pdf = st.file_uploader("Upload your PDF:", type=["pdf"], label_visibility="collapsed")
        
        st.markdown("---")
        
        # Chat Controls Section
        st.markdown("### 🎛️ Chat Controls")
        
        if st.button("🗑️ Clear Chat History", use_container_width=True):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()
        
        if st.button("🔄 Reset (Upload New PDF)", use_container_width=True):
            st.session_state.messages = []
            st.session_state.knowledge_base = None
            st.session_state.chat_history = []
            st.rerun()
        
        st.markdown("---")
        
        # Footer
        st.markdown("""
        <div style='text-align: center; padding: 10px 0; color: #666; font-size: 12px;'>
            <p>💡 Powered by LangChain & HuggingFace</p>
        </div>
        """, unsafe_allow_html=True)
    
    if pdf is not None:
        # Process PDF only if not already processed
        if st.session_state.knowledge_base is None:
            with st.spinner("Processing PDF..."):
                pdf_reader = PdfReader(pdf)
                
                # Extract text
                text = ""
                for page in pdf_reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted
                
                # Split into chunks
                text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1000,
                    chunk_overlap=200,
                    length_function=len
                )
                chunks = text_splitter.split_text(text)
                
                # Generate embeddings + Vector DB
                embeddings = get_embeddings()
                st.session_state.knowledge_base = FAISS.from_texts(chunks, embeddings)
                st.success("PDF processed successfully!")
        
        # User input at the bottom (placed before chat display)
        user_question = st.chat_input("Ask a question about your PDF:")
        
        if user_question:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": user_question})
            
            # Capture chat history before building the chain
            current_chat_history = st.session_state.chat_history.copy()
            
            # ✅ Define the RAG prompt with MessagesPlaceholder
            prompt = ChatPromptTemplate.from_messages([
                ("system", """You are a helpful and highly knowledgeable assistant. 
Your task is to answer the user's question using the context extracted from the PDF and the previous conversation.

Guidelines for your response:
- Provide a **detailed yet concise** explanation.
- Use **clear, simple, and structured** language.
- If the answer is **not present** in the PDF context, respond only with: "I cannot find that in the document."
- Do not add unrelated information beyond what is asked.

--- 
PDF Context:
{context}"""),
                MessagesPlaceholder(variable_name="chat_history"),
                ("human", "{question}")
            ])
            
            # ✅ Build LCEL RAG Chain
            retriever = st.session_state.knowledge_base.as_retriever()
            rag_chain = (
                {
                    "context": retriever | (lambda docs: "\n\n".join(d.page_content for d in docs)),
                    "chat_history": lambda _: current_chat_history,
                    "question": RunnablePassthrough()
                }
                | prompt
                | chat_model()
            )
            
            # ✅ Get response
            with st.spinner("Thinking..."):
                response = rag_chain.invoke(user_question)
                answer = response.content
            
            # Add to chat_history as LangChain message objects
            st.session_state.chat_history.append(HumanMessage(content=user_question))
            st.session_state.chat_history.append(AIMessage(content=answer))
            
            # Add assistant response to display messages
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
            # Rerun to update chat display
            st.rerun()
        
        # Display chat history
        st.markdown("---")
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.messages:
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
    else:
        st.info("👈 Please upload a PDF from the sidebar to start chatting!")

if __name__ == "__main__":
    main()