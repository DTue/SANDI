"""
File Name: vector_db.py
Purpose: Storing knowledge information with embeddings and return the most similar for a query vector
Goals: 
- Hold Knowledge info and embedding matrix
- Similarity score => Calculated during search by comparing embedding matrix(stored knowledge representation) x query vector
- support , add(), search(), count(), and clear() methods
- sort scores
- take top k indices
- build retrieval objects
Architecture Decision:
- VectorStore object to store knowledge object and embedding matrix of document vectors instead of VECTOR_DB[] that stores raw chunks
"""

from system.models.knowledge_items import KnowledgeItem
from models.retrieved_results import RetrievedResults
import numpy as np


class VectorDatabase:
    
    def __init__(self) -> None: #initialization + stores list of knowledge objects and embedding matrix of document vectors
        self._knowledge_items: list[KnowledgeItem] = [ ]  #Initialize list of knowledge items objects
        self._embedding_matrix : np.ndarray | None = None #Initalize n-dimension array for embedding matrix

    """
    def add():takes knowledge objects and corresponding vectors to verify match and store together

    add() behaviors:
    - initialize storage if empty
    - append if data already exists
    - numbers of knowledge info must match number of vector rows

    add() Error and Risk Validation
    - Empty list
    - Missing list
    - Invalid list
    - Unequal vectors
    - Vectors might not be 2D
    - New vectors might need different embedding dimentsion

    add() note:     
    - cannot combine vectors from different embedding spaces
    """
    def add(self, knowledge_items: list[KnowledgeItem], embedding_matrix: np.ndarray) -> None:

        #add() Error and Risk Validation for incoming elements
        if not knowledge_items: #VALIDATION: Empty knowledge item list - Should be initially empty
            raise ValueError ("VALUE ERROR: knowledge items list is empty")

        if embedding_matrix is None: #VALIDATION: NULL or invalid  embedding matrix
            raise ValueError("VALUE ERROR: embedding matrix is invalid or empty")

        if embedding_matrix.ndim != 2: #VALIDATION: Non-2D Embedding Matrix
            raise ValueError("VALUE ERROR: Embedding matrix's dimension is not 2D")
        
        if len(knowledge_items) != embedding_matrix.shape[0]: #VALIDATION: Unequal vectors by comparing rows
            raise RuntimeError("RUNTIME ERROR: Knowledge items list and embedding matrix is inequal")

        if not self._knowledge_items: # if knowledge items list is empty
            self._knowledge_items.extend(knowledge_items) #add new knowledge items/all elements of an iterable to the end of the list
            self._embedding_matrix = embedding_matrix  #add new embedding matrix
        
                            



                
                

            



    
            



    #TODO: def search():
    #TODO: def count():
    #TODO: def clear(): 

