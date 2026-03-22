from fastapi import FastAPI
from app.database.database import engine, Base
from app.routes.employee_routes import router as employee_router
from app.models.user import User
from app.routes.auth_routes import router as auth_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(employee_router)

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Sistema rodando 🚀"}