#!/usr/bin/python3
"""a wopas asd"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    A = sessionmaker(bind=eng)
    a = A()
    b = State(name="California")
    b.cities = [City(name="San Francisco")]
    a.add(b)
    a.commit()
    a.close()
