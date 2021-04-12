from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId
from dependencies import PyObjectId


# Модель для работы с документами из базы данных
class Employees(BaseModel):
    # Указываю для id конкретный тип данных, полученный из класса PyObjectId
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    email: str
    age: int
    company: str
    join_date: str
    job_title: str
    gender: str
    salary: int

    # Указывает возможность задания произвольного типа в модели и преобразование произвольного типа в строку
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
