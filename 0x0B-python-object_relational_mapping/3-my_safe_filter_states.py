#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states"""

import MySQLdb
import sys

conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = conn.cursor()

cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY states.id ASC",
            [format(sys.argv[4])])

rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
