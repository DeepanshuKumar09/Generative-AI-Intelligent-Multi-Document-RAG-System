
import streamlit as st

from document_processor import (
    extract_text_from_pdfs,
    split_documents
)

from vector_store import create_vector_store

from rag_pipeline import generate_response


# Page configuration
st.set_page_config(
    page_title="Generative AI – Intelligent Multi-Document RAG System",
    page_icon="📚",
    layout="wide"
)


# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "processed_files" not in st.session_state:
    st.session_state.processed_files = []


# Application title
st.title("📚 Generative AI – Intelligent Multi-Document RAG System")

st.markdown(
    "### Intelligent Multi-Document RAG System"
)

st.write(
    "Upload multiple PDF documents and ask questions "
    "using natural language."
)


# Sidebar
with st.sidebar:

    st.header("📂 Document Management")

    uploaded_files = st.file_uploader(
        "Upload PDF documents",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button(
        "Process Documents",
        use_container_width=True
    ):

        if not uploaded_files:

            st.warning("Please upload PDF documents.")

        else:

            with st.spinner(
                "Processing documents..."
            ):

                documents = extract_text_from_pdfs(
                    uploaded_files
                )

                chunks = split_documents(documents)

                vector_store = create_vector_store(
                    chunks
                )

                st.session_state.vector_store = vector_store

                st.session_state.processed_files = [
                    file.name for file in uploaded_files
                ]

                st.session_state.chat_history = []

            st.success(
                f"Successfully processed {len(uploaded_files)} PDFs!"
            )

            st.write(
                f"Total pages: {len(documents)}"
            )

            st.write(
                f"Total chunks: {len(chunks)}"
            )

    st.divider()

    st.subheader("Processed Documents")

    for filename in st.session_state.processed_files:

        st.write(f"📄 {filename}")

    if st.button(
        "Clear Chat",
        use_container_width=True
    ):

        st.session_state.chat_history = []

        st.rerun()


# Main chat interface
st.subheader("💬 Chat with Your Documents")


if st.session_state.vector_store is None:

    st.info(
        "Upload and process PDF documents to start chatting."
    )


# Display conversation
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message.get("sources"):

            with st.expander("📚 View Sources"):

                for source in message["sources"]:

                    st.write(
                        f"📄 {source['source']} | "
                        f"Page: {source['page']}"
                    )


# Chat input
question = st.chat_input(
    "Ask something about your documents..."
)


if question:

    if st.session_state.vector_store is None:

        st.warning(
            "Please upload and process documents first."
        )

    else:

        # Display user question
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):

            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    result = generate_response(
                        st.session_state.vector_store,
                        question,
                        st.session_state.chat_history[:-1]
                    )

                    answer = result["answer"]

                    sources = result["sources"]

                    st.markdown(answer)

                    if sources:

                        with st.expander("📚 View Sources"):

                            for source in sources:

                                st.write(
                                    f"📄 {source['source']} | "
                                    f"Page: {source['page']}"
                                )

                    # Save assistant response
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": sources
                    })

                except Exception as e:

                    st.error(
                        f"An error occurred: {str(e)}"
                    )
