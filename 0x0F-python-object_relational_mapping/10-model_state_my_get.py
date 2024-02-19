#!/usr/bin/python3
""" A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def print_state_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server, retrieves and prints the State object with the specified name from the database.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state to search

    Returns:
    - None
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state is not None:
        print(state.id)
    else:
        print("Not found")
