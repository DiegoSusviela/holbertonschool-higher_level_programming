#!/usr/bin/python3
"""a wopas asd"""

import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    b = a.cursor()
    b.execute("SELECT * FROM states WHERE Name =  %s ORDER BY id ASC",
              [sys.argv[4]])
    q = b.fetchall()
    for row in q:
        print(row)
    b.close()
    a.close()
