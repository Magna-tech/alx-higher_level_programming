#!/usr/bin/python3
""" list all states where the name begins with N"""


import sys
import MySQLdb


def main():
    """code is executed inside the main function"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
        )
    cursor = db.cursor()

    q = ("SELECT * FROM states WHERE binary name='{}'".format(sys.argv[4]) +
         "ORDER BY id ASC")
    cursor.execute(q)

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
