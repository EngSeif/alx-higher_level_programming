#!/usr/bin/python3
""" List States Starting With N """

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
    try:
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    except Exception as e:
        exit(1)
    Result = cur.fetchall()
    for row in Result:
        print(row)

    cur.close()
    db.close()
