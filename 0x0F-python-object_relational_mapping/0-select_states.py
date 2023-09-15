#!/usr/bin/python3
"""script that lists all states table from the given database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    for i in cur.fetchall():
        print(i)
    cur.close()
    db.close()
