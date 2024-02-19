#!/usr/bin/python3
""" A script that takes in arguments and an SQL injection to delete all records of a table. """
import MySQLdb
import sys

def safe_filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL server and filters states based on the provided state name from the specified database using parameterized queries to prevent SQL injection.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database
    - state_name: Name of the state to be searched

    Returns:
    - None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
