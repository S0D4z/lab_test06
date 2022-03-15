from fastapi import FastAPI
from routes.birthday_route import birthday_api_router
from routes.students_route import students_api_router

app = FastAPI()

app.include_router(birthday_api_router)
app.include_router(students_api_router)