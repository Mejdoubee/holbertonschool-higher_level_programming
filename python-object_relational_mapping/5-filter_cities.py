#!/usr/bin/python3
'''
Write a script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
'''
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )
    cur = db.cursor()
    query = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
