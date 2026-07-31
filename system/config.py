#Purpose: Central configuration to read environment variables
"""
Goals:
- Hold names and paths
- Stay lightweight

"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from dataclasses import dataclass #a decorator that examines a class to find a field

@dataclass
class Settings(BaseSettings): 

    #Project Information
    PROJECT_NAME = "SANDI"

    #Models: What model objects to use? 
    LANGUAGE_MODEL = "qwen3:8b"  
    EMBEDDING_MODEL = "BAAI/bge-m3" 

    #RAG
    TOP_K = 5 #Number of relavant text chunks to be trieved from database
    CHUNK_SIZE = 500 #Max number of units into a single text segment
    CHUNK_OVERLAP = 75 #Max number of units consecutive chunks share - preventing loss of data

    #Data Directory
    RAW_DATA_DIR = "data/raw"
    PROCESSED_DATA_DIR = "data/processed"

    #Vector DB
    VECTOR_DB_DIR = "rag/vector_db"

    #Development
    OLLAMA_HOST = "http://localhost:11434"




settings = Settings() #Setting object to be called


