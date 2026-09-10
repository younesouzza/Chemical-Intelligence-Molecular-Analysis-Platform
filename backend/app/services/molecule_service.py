from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors, AllChem
from app.schemas.molecule import MoleculeProperties, LipinskiAnalysis

def calculate_molecule_properties(smiles: str) -> MoleculeProperties:
    mol = Chem.MolFromSmiles(smiles)
    
    if mol is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")

    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048)
    fp_list = list(fp)

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
        formal_charge=Chem.GetFormalCharge(mol),
        fingerprint=fp_list
    )

def evaluate_lipinski(props: MoleculeProperties) -> LipinskiAnalysis:
    violations = 0
    
    mw_pass = props.molecular_weight <= 500
    if not mw_pass: violations += 1
    
    logp_pass = props.logp <= 5
    if not logp_pass: violations += 1
    
    hbd_pass = props.hbd <= 5
    if not hbd_pass: violations += 1
    
    hba_pass = props.hba <= 10
    if not hba_pass: violations += 1
        
    summary = "PASS (<=1 violation)" if violations <= 1 else "FAIL (>1 violation)"
    
    return LipinskiAnalysis(
        mw_pass=mw_pass,
        logp_pass=logp_pass,
        hbd_pass=hbd_pass,
        hba_pass=hba_pass,
        violations=violations,
        summary=summary
    )