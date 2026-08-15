"""
File Name: retrieved_results.py
Purpose: Ranking search results to compare against knowledged items
Goals: 
- Contains results of comparing against SANDI information from knowledge,py
Architecture Decision:
@dataclass(frozen=True): represents structured and immutable/frozen data for predictable typed object 
"""
from dataclasses import dataclass
from knowledge import Knowledge

@dataclass(fron=True)
class RetrievedResults:
    info: Knowledge
    similarity_score: float
    rank: int
