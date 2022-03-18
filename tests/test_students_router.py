from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../lab_test06')
from main import app

client = TestClient(app)

def test_student_insert(db):
    response = client.post(
        "/students/",
        json={
        "name": "4242424",
        "description": "string",
        "completed": "true",
        "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "4242424"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_student_update(db):
    response = client.put(
        "/students/6233fa3a668ecc5ad1d3e9ef",
        json={
        "name": "update",
        "description": "string",
        "completed": "true",
        "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"
    
def test_student_delete(db):
    response = client.delete(
        "/students/6233fa3a668ecc5ad1d3e9ef"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
