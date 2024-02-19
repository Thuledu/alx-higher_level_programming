#!/usr/bin/python3
""" A cript that lists all State objects, and corresponding City objects, contained in the database hbtn_0e_101_usa """
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def list_states_and_cities(username, password, database):
    """
    Connects to the MySQL server, retrieves and prints all State objects and their corresponding City objects from the database hbtn_0e_101_usa.

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

    states = session.query(State).order_by(State.id).all()

    for state in session.query(State).order_by(State.id):
        print(state.id, state.name, sep=": ")
        for city in state.cities:
            print("    ", end="")
            print(city.id, city.name, sep=": ")
