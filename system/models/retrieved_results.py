"""
File Name: retrieved_results.py
Purpose: Ranking search results to compare against knowledged items
Goals: 
- Contains results of comparing against SANDI information from knowledge,py
Architecture Decision:
@dataclass(frozen=True): represents structured and immutable/frozen data for predictable typed object 
"""
from dataclasses import dataclass
from system.models.knowledge_items import KnowledgeItem

@dataclass(frozen=True)
class RetrievedResults:
    items: KnowledgeItem
    similarity_score: float
    rank: int
