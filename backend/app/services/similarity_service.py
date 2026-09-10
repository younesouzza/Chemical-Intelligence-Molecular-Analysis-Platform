import pickle
import os
from typing import List, Dict
from app.cheminformatics.similarity import calculate_bulk_tanimoto

DATASET_PATH = os.path.join(os.path.dirname(__file__), "../../data/processed_dataset.pkl")
try:
    with open(DATASET_PATH, 'rb') as f:
        DATASET = pickle.load(f)
except FileNotFoundError:
    print(" WARNING: processed_dataset.pkl not found.")
    DATASET = []

def find_similar_molecules(query_smiles: str, threshold: float = 0.3, top_k: int = 10) -> List[Dict]:
    if not DATASET:
        raise ValueError("Dataset not loaded.")
    dataset_fps = [item["fp"] for item in DATASET]
    
    similarities = calculate_bulk_tanimoto(query_smiles, dataset_fps)
    
    results = []
    for i, sim in enumerate(similarities):
        if sim >= threshold:
            results.append({
                "name": DATASET[i]["name"],
                "smiles": DATASET[i]["smiles"],
                "similarity": round(sim, 4)
            })
            
    results.sort(key=lambda x: x["similarity"], reverse=True)
    return results[:top_k]