#!/usr/bin/python3
""" A script that changes the name of a State object from the database hbtn_0e_6_usa. """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def change_state_name(username, password, database):
    """
    Connects to the MySQL server, changes the name of the State object where id = 2 to "New Mexico" in the specified database.

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

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
        print(state.id)
    else:
        print("Not found")
