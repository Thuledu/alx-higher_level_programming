#!/usr/bin/python3
""" A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

def list_states_with_letter_a(username, password, database):
    """
    Connects to the MySQL server, lists all State objects containing the letter 'a' from the specified database, and displays the results.

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

    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
