from sqlalchemy.orm import Session
from app.models.employee import Employee

def create_employee(db: Session, data):
    employee = Employee(**data.dict())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_all_employees(db: Session):
    return db.query(Employee).all()