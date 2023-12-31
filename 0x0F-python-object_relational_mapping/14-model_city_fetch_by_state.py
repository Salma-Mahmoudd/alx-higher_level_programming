#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State, City).filter(State.id == City.state_id)
    for i, j in q.order_by(City.id):
        print(f"{i.name}: ({j.id}) {j.name}")
