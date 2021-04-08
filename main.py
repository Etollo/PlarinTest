from models import Employees
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import connections

employers = connections()
db = employers['employees']

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.get('/employees/')
async def employees():
    list_employees = []
    for employ in db.employees.find():
        list_employees.append(Employees(**employ))
    if not list_employees:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'list_employees': list_employees}
