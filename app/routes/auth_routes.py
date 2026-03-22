from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate, UserLogin
from app.services.auth import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    db: Session = SessionLocal()

    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        db.close()
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = User(
        username=user.username,
        password=hash_password(user.password),
        role="admin"
    )

    db.add(new_user)
    db.commit()
    db.close()

    return {"message": "Usuário criado com sucesso"}

@router.post("/login")
def login(user: UserLogin):
    db: Session = SessionLocal()

    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user or not verify_password(user.password, db_user.password):
        db.close()
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_token({
        "sub": user.username,
        "role": db_user.role})

    db.close()

    return {"access_token": token, "token_type": "bearer"}

