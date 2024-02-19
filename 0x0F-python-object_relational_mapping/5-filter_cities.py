#!/usr/bin/python3
""" A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa."""
import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    """
    Connects to the MySQL server and lists all cities of the specified state from the database using parameterized queries to prevent SQL injection.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state for which cities are to be listed

    Returns:
    - None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
