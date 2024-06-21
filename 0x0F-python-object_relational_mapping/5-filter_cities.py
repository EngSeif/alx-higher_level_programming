#!/usr/bin/python3
""" List Cities """

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
    com = """
            SELECT cities.name FROM cities
            JOIN states ON cities.state_id =
            states.id WHERE states.name = %s
            ORDER BY cities.id ASC
        """
    cur.execute(com, (argv[4], ))
    Result = cur.fetchall()
    print(", ".join(row[0] for row in Result))
    cur.close()
    db.close()
