#Purpose: Store and search for vectors
"""
Goals:
-add chunks and embeddings
-save metadata
-search by query vector
-return top-k matching chunks
"""

import ollama
from ingestion import calfresh_information
from system.config import settings

VECTOR_DB = []
embedding_model = settings.EMBEDDING_MODEL


def add_chunk_to_db(chunk):
    embedding = ollama.embed(model= embedding_model, input=chunk)
    print(embedding['embeddings'])
    VECTOR_DB.append(chunk, embedding)

for i, chunk in enumerate(calfresh_information):
    add_chunk_to_db(chunk)
    print(f'Added chunk {i+1}/{len(calfresh_information)} to the database')


