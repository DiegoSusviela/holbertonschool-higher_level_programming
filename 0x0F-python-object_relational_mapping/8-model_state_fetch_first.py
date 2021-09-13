#!/usr/bin/python3
"""a wopas asd"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    a = sessionmaker(bind=engine)
    a = a()
    try:
        print("{:}: ".format(a.query(State).order_by(
            State.id).first().id), end="")
        print(a.query(State).order_by(State.id).first().name)
    except:
        print("Nothing")
    a.close()
