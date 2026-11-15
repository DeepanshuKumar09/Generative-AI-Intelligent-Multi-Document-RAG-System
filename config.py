
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please configure it in your .env file."
    )

# LLM Configuration
LLM_MODEL = "gemini-3.6-flash"
TEMPERATURE = 0.2

# Embedding Configuration
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Text Splitting Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Retrieval Configuration
TOP_K = 4
