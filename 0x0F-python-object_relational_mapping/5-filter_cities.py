#!/usr/bin/python3
"""a wopas asd"""

import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    b = a.cursor()
    c = "SELECT cities.name FROM cities"
    c = c + " INNER JOIN states ON cities.state_id = states.id"
    c = c + " WHERE states.name = %s ORDER BY cities.id ASC"
    b.execute(c, [sys.argv[4]])
    q = b.fetchall()
    print(", ".join([row[0] for row in q]))
    b.close()
    a.close()
