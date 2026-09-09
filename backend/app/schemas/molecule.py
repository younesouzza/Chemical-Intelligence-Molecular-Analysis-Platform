from pydantic import BaseModel

class MoleculeRequest(BaseModel):
    smiles: str

class MoleculeProperties(BaseModel):
    molecular_weight: float
    logp: float
    tpsa: float
    hbd: int
    hba: int
    rotatable_bonds: int
    heavy_atom_count: int
    ring_count: int
    aromatic_ring_count: int
    fraction_csp3: float
    formal_charge: int

class MoleculeResponse(BaseModel):
    canonical_smiles: str
    properties: MoleculeProperties