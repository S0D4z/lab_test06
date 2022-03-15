from fastapi import APIRouter
import datetime

birthday_api_router = APIRouter()

@birthday_api_router.get("/service/getage")
async def get_test(year: int):
    if year == "":
        return {"msg": "Please enter year"}
    else:
        return check_number(year)
    
def calculate(year):
    now = datetime.datetime.now()
    age = int(now.year + 543 ) - year  
    return {"age": age}

def check_number(year):
    if type(year) == int:
        return check_out_of_range(year)
    else:
        return {"msg": "Year should be number"}
    
def check_out_of_range(year):
    if year > 0 and year <= 2564:
        return calculate(year)
    elif year == 0:
        return {"msg": "Year should not be 0"}
    elif year > 2564:
        return {"msg": "Year should not more than 2564"}
    else:
        return {"msg": "Year should be positive number"}
    
    
    
    
    
    
      
    