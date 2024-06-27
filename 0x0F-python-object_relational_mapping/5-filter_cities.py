#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state

"""

import sys
import MySQLdb

if __name__ == '__main__':
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3308,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)

    cur = db.cursor()

    state = sys.argv[4]
    query = """
            SELECT citices.name FROM cities
            JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s ORDER BY cities.id ASC
            """

    cur.execute(query, (state, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
