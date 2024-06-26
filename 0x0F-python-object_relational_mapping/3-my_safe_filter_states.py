#!/usr/bin/python3
"""lists all states where name matches the argument (safe from SQL injection)"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()

    State = args[4]
    Qury = " SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(Qury, (State, ))

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
