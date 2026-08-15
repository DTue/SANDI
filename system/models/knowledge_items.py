"""
File Name: knowledged_items.py
Purpose: Python class mode that contains searchable information of SANDI knowledge
Goals:
- Contain data we know
Architecture Decision:
@dataclass(frozen=True): represents structured and immutable/frozen data for predictable typed object 
"""

from dataclasses import dataclass

@dataclass(frozen=True) 
class KnowledgeItem:
    id: str
    name: str
    prorgam_title: str
    category: str
    source: str
    program_url: str
    summary: str

    