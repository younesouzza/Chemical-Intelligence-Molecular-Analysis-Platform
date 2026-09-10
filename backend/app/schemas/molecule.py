from pydantic import BaseModel
from typing import List


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
    fingerprint: List[int]

class LipinskiAnalysis(BaseModel):
    mw_pass: bool
    logp_pass: bool
    hbd_pass: bool
    hba_pass: bool
    violations: int

    summary : str


class MoleculeResponse(BaseModel):
    canonical_smiles: str
    properties: MoleculeProperties
    lipinski: LipinskiAnalysis  