from fastapi import APIRouter, HTTPException
from rdkit import Chem
from app.schemas.molecule import MoleculeRequest, MoleculeResponse
from app.services.molecule_service import calculate_molecule_properties, evaluate_lipinski

router = APIRouter(prefix="/api/v1/molecules", tags=["molecules"])

@router.post("/analyze", response_model=MoleculeResponse)
def analyze_molecule(request: MoleculeRequest):
    """
    Analyze a molecule by its SMILES string and return its properties.
    """
    try:
        properties = calculate_molecule_properties(request.smiles)
        
        lipinski_analysis = evaluate_lipinski(properties)
        mol = Chem.MolFromSmiles(request.smiles)
        canonical_smiles = Chem.MolToSmiles(mol)
        
        return MoleculeResponse(
            canonical_smiles=canonical_smiles,
            properties=properties,
            lipinski=lipinski_analysis
        )
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))