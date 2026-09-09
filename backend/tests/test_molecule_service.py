import pytest
from app.services.molecule_service import calculate_molecule_properties

def test_valid_smiles():
    """Test that a valid SMILES returns the correct properties."""
    # Ethanol: CCO
    props = calculate_molecule_properties("CCO")
    
    assert props.molecular_weight > 40 and props.molecular_weight < 50
    assert props.hbd == 1  # Ethanol has 1 Hydrogen Bond Donor (the OH group)
    assert props.heavy_atom_count == 3 # Carbon and Oxygen

def test_invalid_smiles():
    with pytest.raises(ValueError):
        calculate_molecule_properties("not_a_real_molecule")