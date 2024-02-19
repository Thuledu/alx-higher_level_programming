#!/usr/bin/python3
""" A cript that lists all cities from the database hbtn_0e_4_usa. """     
import MySQLdb
import sys

def list_cities(username, password, database):
    """
    Connects to the MySQL server and lists all cities from the specified database.

    Args:
    - username: MySQL username
    - password: MySQL password
    - database: Name of the database

    Returns:
    - None
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM cities ORDER BY id"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
