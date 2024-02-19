#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa """
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def fetch_cities_by_state(username, password, database):
    """
    Connects to the MySQL server, retrieves and prints all City objects from the database hbtn_0e_14_usa.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database

    Returns:
    - None
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State).filter(State.id == city.state_id).first().name
        print("{}: ({}) {}".format(state_name, city.id, city.name))
