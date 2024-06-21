#!/usr/bin/python3
""" List States Starting With N """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name\
                    LIKE BINARY 'N%' ORDER BY states.id ASC")
        Result = cur.fetchall()
        for row in Result:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        exit()
