
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL, TOP_K


# Initialize embedding model
def get_embedding_model():

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )

    return embeddings


# Create FAISS vector database
def create_vector_store(chunks):

    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    return vector_store


# Retrieve relevant document chunks
def retrieve_documents(vector_store, query):

    results = vector_store.similarity_search(
        query,
        k=TOP_K
    )

    return results
