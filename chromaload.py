from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

# Load vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
chroma_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding_model
)

retriever = chroma_db.as_retriever()
results = retriever.get_relevant_documents("Who is Ravana?")
for r in results:
    print(r.page_content[:200])
