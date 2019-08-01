from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Rating(Base):
	__tablename__ = 'rating'
	rating_id = Column(Integer, primary_key=True)
	rating = Column(Integer)
