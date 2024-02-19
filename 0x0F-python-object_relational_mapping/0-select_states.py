#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa. """ 
import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to the MySQL server and lists all states from the specified database.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database

    Returns:
    - None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id")

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()

