from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
import os

# 1. Load and chunk the document
loader = PyMuPDFLoader("/home/roosterpro/Downloads/Ramayana.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 2. Setup Hugging Face Embedding
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 3. Create and persist Chroma vector store
chroma_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
)

chroma_db.persist()  # Saves to disk
