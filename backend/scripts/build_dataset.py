# backend/scripts/build_dataset.py
import pandas as pd
import pickle
import os
from rdkit import Chem
from rdkit.Chem import AllChem
import urllib.request

RAW_URL = "https://raw.githubusercontent.com/deepchem/deepchem/master/datasets/delaney-processed.csv"
RAW_FILE = "data/raw_esol.csv"
PROCESSED_FILE = "data/processed_dataset.pkl"

def download_data():
    """Download the raw dataset if it doesn't exist."""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(RAW_FILE):
        print(f"Downloading dataset from {RAW_URL}...")
        urllib.request.urlretrieve(RAW_URL, RAW_FILE)
        print("Download complete.")
    else:
        print("Raw dataset already exists.")

def process_data():
    """Clean, validate, and generate fingerprints."""
    print("Loading raw data...")
    df = pd.read_csv(RAW_FILE)
    
    # The Delaney dataset uses 'smiles' and 'Compound ID'
    df = df[['Compound ID', 'smiles']].drop_duplicates(subset=['smiles'])
    print(f"Total rows after deduplication: {len(df)}")
    
    processed_molecules = []
    invalid_count = 0
    
    print("Validating SMILES and generating fingerprints (this may take a minute)...")
    for index, row in df.iterrows():
        smiles = row['smiles']
        name = row['Compound ID']
        
        # Validate SMILES
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            invalid_count += 1
            continue
            
        # Generate Morgan Fingerprint (ECFP4)
        fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
        
        processed_molecules.append({
            "name": str(name),
            "smiles": smiles,
            "fp": fp
        })
        
    print(f"Processing complete. Valid molecules: {len(processed_molecules)}. Invalid SMILES skipped: {invalid_count}")
    
    # Save the processed dataset
    with open(PROCESSED_FILE, 'wb') as f:
        pickle.dump(processed_molecules, f)
    print(f"Processed dataset saved to {PROCESSED_FILE}")

if __name__ == "__main__":
    download_data()
    process_data()