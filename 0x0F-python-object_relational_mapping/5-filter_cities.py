#!/usr/bin/python3
"""
script that takes in the name of
a state as an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
            "SELECT cities.name FROM cities JOIN states\
            ON states.id = cities.state_id WHERE states.name=%s\
            ORDER BY cities.id", (sys.argv[4],)
    )
    print(', '.join([i[0] for i in cur.fetchall()]))
    cur.close()
    db.close()
