#!/usr/bin/python3
""" List States By User Input """

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
        com = """
                SELECT * FROM states
                WHERE name = '{}'
                ORDER BY states.id ASC;""".format(argv[4])
        cur.execute(com)
        Result = cur.fetchone()
        print(Result)
        cur.close()
        db.close()
    except Exception as e:
        exit()
