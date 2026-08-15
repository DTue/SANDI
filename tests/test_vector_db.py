"""
File Name: test_vector_db.py
Purpose: Mock test cases for unit test 
"""
import numpy as np
from system.rag.vector_db import VectorDatabase
from system.models.knowledge_items import KnowledgeItem
from data.mock.mock_knowledge_items import mock_knowledge_items
from data.mock.mock_embedding_matrix import mock_embeddings
#Test case
new_knowledge_items =[
   KnowledgeItem(
        id="SSA-001",
        name="Social Security Card Replacement",
        program="Social Security",
        category="Identification",
        source="Synthetic test data",
        summary="A replacement Social Security card can be requested through the Social Security Administration.",
    ), 
]
new_embeddings = np.array([
     [0.15, 0.25, 0.35, 0.45],
])

vector_db = VectorDatabase()
vector_db.add(mock_knowledge_items, mock_embeddings)
vector_db.add(new_knowledge_items, new_embeddings)
