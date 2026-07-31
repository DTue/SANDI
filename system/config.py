#Purpose: Central configuration to read environment variables
"""
Goals:
- Hold names and paths
- Stay lightweight

"""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings): 

    #Project Information
    PROJECT_NAME: str = "SANDI"

    #Models: What model objects to use? 
    LANGUAGE_MODEL: str = "qwen3:8b"  
    EMBEDDING_MODEL: str = "Qwen/Qwen3-Embedding-8B" 

    #RAG
    TOP_K: int = 5 #Number of relavant text chunks to be trieved from database
    CHUNK_SIZE: int = 500 #Max number of units into a single text segment
    CHUNK_OVERLAP: int = 75 #Max number of units consecutive chunks share - preventing loss of data

    #Data Directory
    RAW_DATA_DIR: str = "data/raw"
    PROCESSED_DATA_DIR: str = "data/processed"

    #Vector DB
    VECTOR_DB_DIR: str = "rag/vector_db"

    #Development
    OLLAMA_HOST: str = "http://localhost:11434"


settings = Settings() #Setting object to be called


