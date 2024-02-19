#!/usr/bin/python3
""" A script that lists all City objects from the database hbtn_0e_101_usa """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def list_cities(username, password, database):
    """
    Connects to the MySQL server, retrieves and prints all City objects from the database hbtn_0e_101_usa.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database

    Returns:
    - None
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for state in session.query(State).order_by(State.id):
        for city in state.cities:
            print(city.id, city.name, sep=": ", end="")
            print(" -> " + state.name)
