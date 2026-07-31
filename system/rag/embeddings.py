"""
Goals:
-initialize BGEM3FlagModel - load model
-embed document chunks
-embed queries
-ormalize vectors
-expose a clean interface
"""

from system.config import EMBEDDING_MODEL
from sentence_transformers import SentenceTransformer


#Lazy Loading
def __init__(self, model_name: str | None = None) -> None: 
    self.embedding_model = model_name
    if self.embedding_mode is None:
        self.embedding_model = _get_embedding_model()



def _get_embedding_model(self):
    embedding_model_name = SentenceTransformer("Qwen/Qwen3-Embedding-8B")
    return embedding_model_name





