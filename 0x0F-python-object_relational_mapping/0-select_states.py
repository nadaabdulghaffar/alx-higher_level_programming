#!/usr/bin/python3
""" lists all states from the passed database """

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
