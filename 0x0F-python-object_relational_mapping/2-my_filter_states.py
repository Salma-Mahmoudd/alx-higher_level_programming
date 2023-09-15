#!/usr/bin/python3
"""
script that takes in an argument
displays all values in the states table
of database where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}'".format(argv[4]))
    for i in cur.fetchall():
        print(i)
    cur.close()
    db.close()
