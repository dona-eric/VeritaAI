import psycopg2, os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from model import Base, News
from sqlalchemy.ext.declarative import declarative_base
# Load environment variables from .env
load_dotenv()

# Fetch variables
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

db_url = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

try:
    engine = create_engine(db_url)
    inspector = inspect(engine)
    if 'news' in inspector.get_table_names():
        print("Table 'news' already exists.")
    else:
        Base.metadata.create_all(engine)
        print("Table 'news' created successfully.")
    print("Database connection established successfully.")
except Exception as e:
    print(f"An error occurred while connecting to the database: {e}")