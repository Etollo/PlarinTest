from Models import Employees, PyObjectId
from fastapi import FastAPI
from pymongo import MongoClient
import pymongo

employers = MongoClient('0.0.0.0', 55001)
db = employers['employees']
series_collection = db['series']

app = FastAPI()


@app.get('/employers')
async def list_employees():
    employers = []
    for employees in db.employees.find():
        employers.append(Employees(**employees))
    return {'employers': employers}


@app.get('/employers/{id}')
async def employees(id):
    employees = []
    for employ in db.employees.find_document(series_collection):
        # print(employ)
        print(type(employ))
        if employ == {id}:
            employees.append(employ)
    return {"employees": employees}
