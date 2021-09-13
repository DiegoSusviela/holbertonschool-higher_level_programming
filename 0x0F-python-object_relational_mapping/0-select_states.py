#!/usr/bin/python3
"""aa wopa necesito score"""

import sys
import MySQLdb

if __name__ == "__main__":
    a = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    b = a.cursor()
    b.execute("SELECT * FROM states ORDER BY id ASC")
    q = b.fetchall()
    for row in q:
        print(row)
    b.close()
    a.close()
