#!/usr/bin/python3
"""script that lists all State objects, and corresponding City objects"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id):
        print(f"{s.id}: {s.name}")
        for c in s.cities:
            print(f"\t{c.id}: {c.name}")
