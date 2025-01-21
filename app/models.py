from pydantic import BaseModel
from typing import List

class Employee(BaseModel):
    name: str
    position: str

class Company(BaseModel):
    name: str
    size: str
    industry: str
    employees: List[Employee]
