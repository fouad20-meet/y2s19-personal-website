from model import Base, Rating

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///students.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_rating(rating):
	rating_object = Rating(
		rating = rating)
	session.add(rating_object)
	session.commit()

def average():
	ratings = session.query(Rating).all()
	if len(ratings) == 0:
		return 0
	avg = 0
	for i in ratings:
		avg += i.rating
	return int(avg/len(ratings))
