from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time
from sqlalchemy.exc import OperationalError

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def wait_for_db():
    """Wait for database to be available"""
    max_retries = 30
    retry_count = 0

    while retry_count < max_retries:
        try:
            # Try to connect to the database
            connection = engine.connect()
            connection.close()
            print("Database connection successful!")
            return True
        except OperationalError:
            retry_count += 1
            print(f"Database not ready, retrying... ({retry_count}/{max_retries})")
            time.sleep(2)

    raise Exception("Could not connect to database after maximum retries")

def get_db():
    db = SessionLocal()