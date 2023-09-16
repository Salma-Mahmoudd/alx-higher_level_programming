#!/usr/bin/python3
"""script that lists all State objects that contain the letter a"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_state = session.query(State).filter(State.name.contains('a%'))
    for i in a_state.order_by(State.id):
        print(f"{i.id}: {i.name}")
