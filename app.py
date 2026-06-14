import os
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
import json
import re
from dotenv import load_dotenv


load_dotenv()


# Embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing FAISS vector store
db = FAISS.load_local(
    r"faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

print("FAISS Loaded Successfully")

# Create retriever
retriever = db.as_retriever(
    search_kwargs={"k": 3}
)


template="""You are a LangChain documentation assistant.

Context:
{context}

Question:
{question}

Instructions:
- Answer only from the context.
- If the answer is not present in the context, say:
  "I don't have information about that in my knowledge base."
- Do not use external knowledge."""


prompt= PromptTemplate(input_variables=["context", "question"], template=template)  



llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0
    )


chain=RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff", chain_type_kwargs={"prompt": prompt},return_source_documents=True)    

# ==========================================
# Page Config
# ==========================================
st.set_page_config(
    page_title="LangBot",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# Sidebar
# ==========================================
st.sidebar.title("📚 Topics")



# Fetch the Topics 
with open(r"data/langchain_rag_docs.json", 'r',encoding="utf-8") as file:
    data=json.load(file)

options=["All Topics"]
for i in data:
    url=i["url"]
    matches = re.search(r"https://docs\.langchain\.com/(.*?)\.md",url)
    if matches:
        options.append(matches.group(1))

topic = st.sidebar.radio(
    "Select a Topic",
    list(set(options))
)

# ==========================================
# Example Questions
# ==========================================

topic_name = (
    topic.split("/")[-1]
    .replace("-", " ")
    .replace("_", " ")
    .title()
)

examples = [
    f"What is {topic_name}?",
    f"How does {topic_name} work?",
    f"When should I use {topic_name}?",
    f"Explain {topic_name}.",
    f"Give an example of {topic_name}."
]
# ==========================================
# Main Page
# ==========================================
st.title("🤖 LangBot")

st.markdown(
    """
    Ask questions about LangChain concepts and documentation.
    """
)

st.divider()

# ==========================================
# Selected Topic
# ==========================================
col1, col2 = st.columns([1, 3])

with col1:
    st.info(f"📌 Selected Topic: **{topic}**")

with col2:
    if topic != "All Topics":
        st.markdown("### Suggested Questions")

        for q in examples:
            st.markdown(f"- {q}")

st.divider()

# ==========================================
# User Query
# ==========================================
user_query = st.text_input(
    "Ask a Question",
    placeholder="Example: What are embeddings?"
)

ask_button = st.button(
    "🚀 Ask",
    use_container_width=True
)

# ==========================================
# Response Section
# ==========================================
if ask_button:

    if not user_query.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching documentation..."):

            # ======================================
            # YOUR RAG LOGIC HERE
            # ======================================

            response = chain.invoke(
                {
                    "query": user_query
                }
            )

            answer = response["result"]

            sources = [
                doc.metadata["source"]
                for doc in response["source_documents"]
            ]



        # ======================================
        # Answer
        # ======================================
        st.subheader("💡 Answer")

        st.success(answer)

        # ======================================
        # Sources
        # ======================================
        st.subheader("📚 Sources Used")

        unique_sources = list(set(sources))

        for source in unique_sources:
            st.markdown(f"- {source}")

        

# ==========================================
# Footer
# ==========================================
st.divider()

st.caption(
    "Built using LangChain, FAISS, Gemini and Streamlit"
)