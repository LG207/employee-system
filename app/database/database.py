from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = "postgresql://employee_db_21cv_user:0MRiollSNYGUKff3FmjKST6wf1x1m85A@dpg-d7065hv5gffc73dmko20-a/employee_db_21cv"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()