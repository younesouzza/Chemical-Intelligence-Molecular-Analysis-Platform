from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors
from app.schemas.molecule import MoleculeProperties

def calculate_molecule_properties(smiles: str) -> MoleculeProperties:
    # 1. Parse the SMILES
    mol = Chem.MolFromSmiles(smiles)
    
    # 2. Validate
    if mol is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")
        
    # 3. Calculate properties
    return MoleculeProperties(
        molecular_weight=Descriptors.MolWt(mol),
        logp=Descriptors.MolLogP(mol),
        tpsa=rdMolDescriptors.CalcTPSA(mol),
        hbd=Descriptors.NumHDonors(mol),
        hba=Descriptors.NumHAcceptors(mol),
        rotatable_bonds=Descriptors.NumRotatableBonds(mol),
        heavy_atom_count=mol.GetNumHeavyAtoms(),
        ring_count=Descriptors.RingCount(mol),
        aromatic_ring_count=Descriptors.NumAromaticRings(mol),
        fraction_csp3=rdMolDescriptors.CalcFractionCSP3(mol),
        formal_charge=Chem.GetFormalCharge(mol)
    )