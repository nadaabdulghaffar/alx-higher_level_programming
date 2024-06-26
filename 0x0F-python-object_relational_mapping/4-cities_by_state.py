#!/usr/bin/python3
""" lists all cities from the database """

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

    cur.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC""")

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
