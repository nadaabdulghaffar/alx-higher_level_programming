#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database"""

import sys
import MySQLdb


args = sys.argv
db = MySQLdb.connect("localhost",args[1],args[2],args[3])
cur = db.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'n%' ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
db.close()
