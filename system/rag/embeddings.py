"""
Goals:
-initialize BGEM3FlagModel - load model
-embed document chunks
-embed queries
-ormalize vectors
-expose a clean interface
"""

from system.config import settings
from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingService: 
        
        #Lazy Initilization: Load once to reuse every call
        def __init__(self, model_name: str | None = None) -> None: 
            # store private embedding_model_name - default to settings.EMBEDDING_MODEL
            self._embedding_model_name = model_name or settings.EMBEDDING_MODEL
            # Create an instance variable with type hint - never initialized
            self._embedding_model: SentenceTransformer | None = None
         

        def _get_embedding_model(self) -> SentenceTransformer:
              #if the model is not initalized yet
              if self._embedding_model is None: 
                    self._embedding_model = SentenceTransformer(self._embedding_model_name)
                    return self._embedding_model
              else:
                   return self._embedding_model

        #Semantic Vectorization
        #Use normalize_embeddings=True in encode(). SentenceTransformer returns NumPy arrays
        def embed_documents(self, texts: list[str]) -> np.ndarray:
              #Goal: takes texts and turns into numerical coordinates of its semantic meanings

              # Text Validation
              if texts is None:
                    raise ValueError("EmbeddingService: Empty texts") #Returning None breaks downstream NumPy math silently
              if not texts: 
                    raise ValueError("EmbeddingService: Invalid texts")
                  
            # conver documents into high-dimension vector
              self.document_embeddings = self._get_embedding_model().encode(texts, normalize_embeddings=True, convert_to_numpy=True)
      
            # return 2D numpy array - type explicit 
              return np.asarray(self.document_embeddings, dtype=np.float32)


        #Query Vectorization
        def embed_query(self, query: str) -> np.ndarray:
              #Goals: takes a user query into the exact same mathematical vector space as stored documents

              # Query Validation
              if query is None:
                    raise ValueError("EmbeddingService: Empty query")
              if not query: 
                    raise ValueError("EmbeddingService: Invalid query")

              #Query Cleaning
              cleaned_query = query.strip() #remove leading and trailing whitespace

              if not cleaned_query:
                    raise ValueError("EmbeddingService: Uncleaned query - whitespace")

               
              # model.encode([query], prompt_name="query", normalize_embeddings=True)
              self.query_embeddings = self._get_embedding_model().encode_query([cleaned_query], normalize_embeddings=True, convert_to_numpy=True) 
              # return 1D numpy array (first row)
              return  np.asarray(self.query_embeddings[0], dtype=np.float32)
              
              
            





