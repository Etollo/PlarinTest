from typing import Optional

from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel, Field
from bson import ObjectId

employers = MongoClient('0.0.0.0', 55001)
db = employers['employees']

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)


class Employees(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


app = FastAPI()


@app.get('/employers')
async def list_employees():
    employers = []
    for employees in db.employees.find():
        employers.append(Employees(**employees))
    return {'employers': employers}