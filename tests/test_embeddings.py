from system.rag.embeddings import EmbeddingService
from data.mock import mock_document, mock_query

embedding_service = EmbeddingService()

documents = embedding_service.embed_documents(mock_document.documents)
print("Embedding Service Testing: Documents")
print(documents)
print(documents.shape) #.shape() checks dimensions of a data structure
query = embedding_service.embed_query(mock_query.query)

print("Embedding Service Testing: Query")
print(query)
print(query.shape)


