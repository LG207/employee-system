import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = os.getenv("postgresql://employee_db_lrp3_user:7sPNoDibxTvd52XEAOnJB56OA99PyyCC@dpg-d7075fmuk2gs73955fog-a/employee_db_lrp3")

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