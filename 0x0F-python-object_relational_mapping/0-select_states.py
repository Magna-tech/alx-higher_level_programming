#!/usr/bin/python3
"""Script to list all states in the database"""


import sys
import MySQLdb


def main():
    """contains the whole script"""
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


if __name__ == "__main__":
    main()
