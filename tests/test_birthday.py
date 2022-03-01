from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, 'C:/Users/user/Desktop/TDD/lab_test06')        
from main import app

client = TestClient(app)

def test_call_get_data_api():
    year = "2540"
    output = 25
    response = client.get("/service/getage?year="+year)
    assert response.status_code == 200
    assert response.json() == {"age": output}
    
#status code 422      
# def test_input_is_number():
#     year = "test"
#     output = "Year should be number"
#     response = client.get("/service/getage?year="+year)
#     assert response.status_code == 200
#     assert response.json() == {"msg": output}
    
def test_input_is_positive():
    year = "-1"
    output = "Year should be positive number"
    response = client.get("/service/getage?year="+year)
    assert response.status_code == 200
    assert response.json() == {"msg": output}
    
def test_input_is_under_2565():
    year = "2566"
    output = "Year should not more than 2564"
    response = client.get("/service/getage?year="+year)
    assert response.status_code == 200
    assert response.json() == {"msg": output}

#status code 422    
# def test_input_is_not_null():
#     year = ""
#     output = "Please enter year"
#     response = client.get("/service/getage?year="+year)
#     assert response.status_code == 200
#     assert response.json() == {"msg": output}
    
def test_input_is_not_0():
    year = "0"
    output = "Year should not be 0"
    response = client.get("/service/getage?year="+year)
    assert response.status_code == 200
    assert response.json() == {"msg": output}