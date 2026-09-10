from pydantic import BaseModel
from typing import List

class SimilaritySearchRequest(BaseModel):
    smiles: str
    threshold: float = 0.3
    top_k: int = 10

class SimilarityResult(BaseModel):
    name: str
    smiles: str
    similarity: float

class SimilaritySearchResponse(BaseModel):
    query_smiles: str
    results: List[SimilarityResult]