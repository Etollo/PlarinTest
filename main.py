from fastapi import FastAPI, HTTPException

from config.config import DB
from models import Employees

# Инициализация фреймворка
app = FastAPI()


# Метод получения данных из корня программы
@app.get("/")
async def root():
    return {"message": "Hello"}


# Метод получения данных о всех работниках из базы данных
@app.get('/employees/')
async def employees():
    list_employees = []
    for employ in DB.employees.find():
        list_employees.append(Employees(**employ))
    if not list_employees:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'list_employees': list_employees}
