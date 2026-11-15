
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from config import LLM_MODEL, TEMPERATURE
from vector_store import retrieve_documents


# Initialize Gemini
def get_llm():

    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        temperature=TEMPERATURE
    )

    return llm


# Build conversation history
def format_chat_history(chat_history):

    history = ""

    for message in chat_history[-6:]:

        role = message["role"]
        content = message["content"]

        history += f"{role}: {content}\n"

    return history


# Extract clean text from Gemini response
def extract_response_text(response):

    content = response.content

    # Case 1: Gemini returns a normal string
    if isinstance(content, str):
        return content.strip()

    # Case 2: Gemini returns a list of content blocks
    if isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text = block.get("text", "")

                    if text:
                        text_parts.append(text)

            elif isinstance(block, str):
                text_parts.append(block)

        return "\n".join(text_parts).strip()

    return str(content).strip()


# Generate RAG response
def generate_response(vector_store, question, chat_history):

    # Retrieve relevant document chunks
    relevant_docs = retrieve_documents(
        vector_store,
        question
    )

    # Build context
    context = ""

    for i, doc in enumerate(relevant_docs):

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "Unknown")

        context += f"""
Document Chunk {i + 1}
Source: {source}
Page: {page}
Content: {doc.page_content}
"""

    # Format previous conversation
    history = format_chat_history(chat_history)

    # Define prompt
    prompt = ChatPromptTemplate.from_template("""
You are DocuMind AI, an intelligent document
question-answering assistant.

Your task is to answer questions using the
provided document context.

Rules:
1. Answer only using the provided document context.
2. Do not invent facts or information.
3. If the answer is unavailable, clearly say:
   "I couldn't find this information in the uploaded documents."
4. Use conversation history to understand follow-up questions.
5. Provide clear, structured, and readable answers.
6. Never output raw metadata, dictionaries, JSON,
   internal document chunk information, or signatures.
7. Do not generate source citations yourself.
   The application displays source references separately.
8. Use Markdown formatting when appropriate.

Previous Conversation:
{history}

Retrieved Document Context:
{context}

Current Question:
{question}

Answer:
""")

    # Generate response
    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke({
        "history": history,
        "context": context,
        "question": question
    })

    # Extract only clean answer text
    answer = extract_response_text(response)

    # Prepare source references separately
    sources = []

    for doc in relevant_docs:

        source_info = {
            "source": doc.metadata.get("source", "Unknown"),
            "page": doc.metadata.get("page", "Unknown")
        }

        if source_info not in sources:
            sources.append(source_info)

    return {
        "answer": answer,
        "sources": sources
    }
