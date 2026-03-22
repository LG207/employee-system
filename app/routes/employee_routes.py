from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate
from fastapi import HTTPException
from app.services.dependencies import get_current_user
from fastapi import Depends
from app.services.dependencies import require_admin
from app.services.employee_service import create_employee as create_employee_service

router = APIRouter()

@router.post("/employees")
def create_employee(employee: EmployeeCreate, user: str = Depends(require_admin)):
    db: Session = SessionLocal()

    new_employee = Employee(
        name=employee.name,
        cpf=employee.cpf,
        position=employee.position,
        salary=employee.salary
    )

    result = create_employee_service(db, employee)
    db.refresh(new_employee)

    db.close()

    return {"message": "Funcionário criado com sucesso"}

@router.get("/employees")
def get_employees(user: str = Depends(get_current_user)):
    db: Session = SessionLocal()

    employees = db.query(Employee).all()

    db.close()

    return employees

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, user: str = Depends(get_current_user)):
    db: Session = SessionLocal()

    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    db.close()

    if not employee:
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    return employee


@router.put("/employees/{employee_id}")
def update_employee(employee_id: int, updated_data: EmployeeCreate, user: str = Depends(get_current_user)):
    db: Session = SessionLocal()

    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        db.close()
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    employee.name = updated_data.name
    employee.cpf = updated_data.cpf
    employee.position = updated_data.position
    employee.salary = updated_data.salary

    db.commit()
    db.refresh(employee)

    db.close()

    return {"message": "Funcionário atualizado com sucesso"}


@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, user: str = Depends(get_current_user)):
    db: Session = SessionLocal()

    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        db.close()
        raise HTTPException(status_code=404, detail="Funcionário não encontrado")

    db.delete(employee)
    db.commit()
    db.close()

    return {"message": "Funcionário deletado com sucesso"}