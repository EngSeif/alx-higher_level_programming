#!/usr/bin/python3
""" List States By User Input """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    com = "SELECT * FROM states WHERE name = %s\
        ORDER BY states.id ASC"
    cur.execute(com, (argv[4], ))
    Result = cur.fetchall()
    for row in Result:
        print(row)
    cur.close()
    db.close()
