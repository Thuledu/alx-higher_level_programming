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
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    california = State(name='California', cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()
