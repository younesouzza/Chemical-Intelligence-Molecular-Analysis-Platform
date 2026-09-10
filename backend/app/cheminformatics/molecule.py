from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem

def get_canonical_smiles(smiles: str) -> str:
    mol = Chem.MolFromSmiles(smiles)
    return Chem.MolToSmiles(mol)

def calculate_descriptors(mol: Chem.Mol) -> dict:
    """Pure function: Takes an RDKit mol, returns a dictionary of numbers."""
    return {
        "molecular_weight": Descriptors.MolWt(mol),
        "logp": Descriptors.MolLogP(mol),
        "tpsa": rdMolDescriptors.CalcTPSA(mol),
        "hbd": Descriptors.NumHDonors(mol),
        "hba": Descriptors.NumHAcceptors(mol),
        "rotatable_bonds": Descriptors.NumRotatableBonds(mol),
        "heavy_atom_count": mol.GetNumHeavyAtoms(),
        "ring_count": Descriptors.RingCount(mol),
        "aromatic_ring_count": Descriptors.NumAromaticRings(mol),
        "fraction_csp3": rdMolDescriptors.CalcFractionCSP3(mol),
        "formal_charge": Chem.GetFormalCharge(mol),
        "fingerprint": list(AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048))
    }