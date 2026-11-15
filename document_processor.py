
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

from config import CHUNK_SIZE, CHUNK_OVERLAP


def extract_text_from_pdfs(pdf_files):
    """
    Extract text from multiple PDF files.

    Args:
        pdf_files: List of uploaded PDF files.

    Returns:
        List of LangChain Document objects.
    """

    documents = []

    for pdf_file in pdf_files:

        pdf_reader = PdfReader(pdf_file)

        filename = pdf_file.name

        for page_number, page in enumerate(pdf_reader.pages, start=1):

            text = page.extract_text()

            if not text or not text.strip():
                continue

            document = Document(
                page_content=text,
                metadata={
                    "source": filename,
                    "page": page_number
                }
            )

            documents.append(document)

    if not documents:
        raise ValueError(
            "No readable text found in the uploaded PDF documents."
        )

    return documents


def split_documents(documents):
    """
    Split extracted documents into smaller chunks.

    Args:
        documents: List of extracted Document objects.

    Returns:
        List of chunked Document objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
