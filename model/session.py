import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()
DB_USER = os.getenv("DB_USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DB = os.getenv("DB")

POSTGRES_URL = f"postgresql://{DB_USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
engine = create_engine(POSTGRES_URL)