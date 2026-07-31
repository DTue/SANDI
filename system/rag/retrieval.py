import ollama
from system.config import settings
from vector_db import VECTOR_DB

embedding_model = settings.EMBEDDING_MODEL

def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
  query_embedding = ollama.embed(model=embedding_model, input=query)['embeddings'][0]
  similarities = []
  for chunk, embedding in VECTOR_DB:
    similarity = cosine_similarity(query_embedding, embedding)
    similarities.append((chunk, similarity))
    similarities.sort(key=lambda x: x[1], reverse=True)
  return similarities[:top_n]
