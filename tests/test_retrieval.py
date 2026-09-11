import numpy as np
from system.rag.retrieval import Retrieval
from system.rag.embeddings import EmbeddingService
from system.rag.vector_db import VectorDatabase
from data.mock.mock_knowledge_items import mock_knowledge_items
from data.mock.mock_embedding_matrix import mock_embeddings

vector_db = VectorDatabase()
embedding_service = EmbeddingService()

retrieval = Retrieval(embedding_service=embedding_service, vector_db=vector_db)
documents_text = [item.summary for item in mock_knowledge_items]
embedded_documents = embedding_service.embed_documents(texts=documents_text)

print(f"Vector DB - Knowledge Items Count: {vector_db.count()}")
vector_db.add(knowledge_items=mock_knowledge_items, embedding_matrix=embedded_documents)
print(f"Vector DB - Knowledge Items Count: {vector_db.count()}")
user_query = input()
embedded_query = retrieval.embed_query(user_input=user_query)
retrieval.retrieve(embedded_query)



