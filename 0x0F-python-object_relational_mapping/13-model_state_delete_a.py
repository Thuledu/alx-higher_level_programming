#!/usr/bin/python3
""" A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def delete_states_with_letter_a(username, password, database):
    """
    Connects to the MySQL server, deletes all State objects with a name containing the letter 'a' from the specified database.

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

    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
