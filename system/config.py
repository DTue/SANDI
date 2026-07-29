#Purpose: Central configuration to read environment variables

import ollama
from dataclasses import dataclass #a decorator that examines a class to find a field
from transformers import Qwen3VLForConditionalGeneration
from sentence_transformers import SentenceTransformer 



@dataclass
class Settings: 
    #Models
    LANGUAGE_MODEL = Qwen3VLForConditionalGeneration.from_pretrained(
        "Qwen/Qwen3-VL-8B-Instruct", dtype="auto", device_map="auto")

    EMBEDDING_MODEL = SentenceTransformer("Qwen/Qwen3-Embedding-8B")


settings = Settings() #Setting object to be called


