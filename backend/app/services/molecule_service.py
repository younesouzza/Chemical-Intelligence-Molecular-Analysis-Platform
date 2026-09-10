from rdkit import Chem
from app.schemas.molecule import MoleculeProperties, LipinskiAnalysis
from app.cheminformatics.molecule import calculate_descriptors 

def calculate_molecule_properties(smiles: str) -> MoleculeProperties:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES string: {smiles}")
        
    desc_dict = calculate_descriptors(mol)
    return MoleculeProperties(**desc_dict)

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