from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
from typing import List

def calculate_bulk_tanimoto(query_smiles: str, dataset_fps: List) -> List[float]:
    query_mol = Chem.MolFromSmiles(query_smiles)
    if not query_mol:
        raise ValueError("Invalid query SMILES")
        
    query_fp = AllChem.GetMorganFingerprintAsBitVect(query_mol, radius=2, nBits=2048)
    
    return DataStructs.BulkTanimotoSimilarity(query_fp, dataset_fps)