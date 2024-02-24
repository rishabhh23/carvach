from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

DATABASE_URL = "postgresql://postgres:R!shabh8@localhost:5432/Cars"

engine  = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base : DeclarativeMeta = declarative_base()

