from fastapi import APIRouter, HTTPException
from app.schemas.search import SimilaritySearchRequest, SimilaritySearchResponse, SimilarityResult
from app.services.similarity_service import find_similar_molecules

router = APIRouter(prefix="/api/v1/search", tags=["search"])

@router.post("/similarity", response_model=SimilaritySearchResponse)
def search_similar_molecules(request: SimilaritySearchRequest):
    """
    Search for molecules structurally similar to the query SMILES.
    """
    try:
        # 1. Call the service layer
        raw_results = find_similar_molecules(
            query_smiles=request.smiles, 
            threshold=request.threshold, 
            top_k=request.top_k
        )
        
        results = [SimilarityResult(**res) for res in raw_results]
        
        # 3. Return the formatted JSON
        return SimilaritySearchResponse(
            query_smiles=request.smiles,
            results=results
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))