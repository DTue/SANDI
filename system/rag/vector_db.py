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
#from models.retrieved_results import RetrievedResults
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

        #Error and Risk Validation: Knowledge Items
        if not knowledge_items: #VALIDATION: Empty knowledge item list - Should be initially empty
            raise ValueError ("VALUE ERROR: knowledge items list is empty")
        
        if embedding_matrix is None: #VALIDATION: NULL or invalid  embedding matrix
            raise ValueError("VALUE ERROR: embedding matrix is invalid or empty")

        if np.ndim(embedding_matrix) != 2: #VALIDATION: Non-2D Embedding Matrix
            raise ValueError("VALUE ERROR: Embedding matrix's dimension is not 2D")

        #VALIDATION PASSED
        if len(knowledge_items) != embedding_matrix.shape[0]: #VALIDATION: Unequal vectors by comparing rows
            raise ValueError("VALUE ERROR: Knowledge items list and embedding matrix is inequal")
    
        #for-loop for set comprehension to create a new set containing id of every list object - automatically remove duplicates   
        
        existing_knowledge_ids = {item.id for item in self._knowledge_items} 
        print(f"Existing Knowledge IDs: {existing_knowledge_ids}")
        incoming_knowledge_ids = {item.id for item in knowledge_items}
        print(f"Incoming Knowledge IDs: {incoming_knowledge_ids}")
        knowledge_id_duplicate = existing_knowledge_ids.intersection(incoming_knowledge_ids) #checks for common ids
        print(f"Knowledge ID Duplicate: {knowledge_id_duplicate}")

        #VALIDATION PASSED
        if knowledge_id_duplicate: #VALIDATION: if there are duplicate ids
            raise ValueError(f"VALUE ERROR: Duplicate ids between existing and incoming knowledge items{knowledge_id_duplicate}")
        
        if len(knowledge_items) != len(incoming_knowledge_ids): #VALIDATION if there duplicate ids within incoming items
            raise ValueError("VALUE ERROR: There are duplicate ids within the incoming knowledge items")
        
        print("CHECK POINT: All incoming knowledge item ids should be valid.")

        if not self._knowledge_items: # if knowledge items list is empty
                self._knowledge_items = knowledge_items  
                self._embedding_matrix = embedding_matrix
                return

        #Error and Validation: Embedding Matrix  - checking embedding dimension

        #All vectors in the same vector should have the same embedding dimension
        existing_embedding_dimension = self._embedding_matrix.shape[1] #return an int for embedding dimension
        incoming_embedding_dimension = embedding_matrix.shape[1]

        if existing_embedding_dimension!= incoming_embedding_dimension: #VALIDATION: inequal embedding dimension
            raise ValueError("VALUE ERROR: existing and incoming embedding dimensions do not match")

        print("CHECK POINT: All incoming knowledge ids and corresponding embedding dimension should be valid.")

        #Append operation
        self._knowledge_items.extend(knowledge_items)
        print(f"Length of Knowledge Items List: {len(self._knowledge_items)}")
        self._embedding_matrix = np.vstack((self._embedding_matrix, embedding_matrix)) #vertical stack
        print(f"Embedding Dimension: {self._embedding_matrix.shape[1]}")
        print(f"Full Matrix Shape:{len(self._knowledge_items), self._embedding_matrix.shape[1]}")

    #TODO: def count():
    """
    def count(): returns number of stored KnowledgeItem object
    """
    #VALIDATION PASSED
    def count(self):
        return len(self._knowledge_items)

    #TODO: def clear(): 
    """
    def clear_db(): reset the vector database into its original and clean state
    """
    def clear_db(self):
        self._knowledge_items.clear() #removes all items
        self._embedding_matrix = np.array([]) #reassign to an empty array
        

