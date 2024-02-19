#!/usr/bin/python3
""" A script that creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_state_and_city(username, password, database):
    """
    Connects to the MySQL server, creates the State "California" with the City "San Francisco" in the specified database.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database

    Returns:
    - None
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database, pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    newState = State(name='California')
    newCity = City(name='San Francisco')
    newState.cities.append(newCity)

    session.add(newState)
    session.add(newCity)
    session.commit()
