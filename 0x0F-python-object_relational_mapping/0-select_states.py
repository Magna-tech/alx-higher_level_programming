#!/usr/bin/python3
"""Script to list all states in the database"""


import sys
import MySQLdb

# Connect to the database
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
