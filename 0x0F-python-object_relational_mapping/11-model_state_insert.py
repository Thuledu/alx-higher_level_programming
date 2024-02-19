#!/usr/bin/python3
""" A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def add_state(username, password, database):
    """
    Connects to the MySQL server, adds the State object "Louisiana" to the specified database, and prints the new states.id after creation.

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

    new_state = State(name='Louisiana')

    session.add(new_state)

    new_instance = session.query(State).filter_by(name='Louisiana').first()

    print(new_instance.id)

    session.commit()
