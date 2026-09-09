from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "project": "ChemIntel"}

def test_analyze_molecule():
    """Test the POST /api/v1/molecules/analyze endpoint."""
    payload = {"smiles": "CCO"}
    
    # Simulate a POST request
    response = client.post("/api/v1/molecules/analyze", json=payload)
    
    # Check the response
    assert response.status_code == 200
    data = response.json()
    
    # Verify the structure of the response
    assert "canonical_smiles" in data
    assert "properties" in data
    assert data["properties"]["hbd"] == 1

def test_analyze_invalid_molecule():
    payload = {"smiles": "invalid"}
    response = client.post("/api/v1/molecules/analyze", json=payload)
    
    assert response.status_code == 400