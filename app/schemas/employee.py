from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    cpf: str
    position: str
    salary: float