#!/usr/bin/python3
"""
takes an argument and displays all values in
the table that matches the argument.
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
        .format(args[4]))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
