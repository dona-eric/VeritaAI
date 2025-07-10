from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# create a model ofr the news tables

class News(Base):
    __tablename__="news"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    author = Column(String(100), nullable=True)
    content = Column(Text, nullable=True)
    published_at = Column(DateTime, nullable=False)
    source = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)
    