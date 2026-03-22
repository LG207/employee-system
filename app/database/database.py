import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("postgresql://employee_db_21cv_user:0MRiollSNYGUKff3FmjKST6wf1x1m85A@dpg-d7065hv5gffc73dmko20-a/employee_db_21cv")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()