#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
