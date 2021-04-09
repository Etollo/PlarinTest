from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from dependencies import PyObjectId


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
