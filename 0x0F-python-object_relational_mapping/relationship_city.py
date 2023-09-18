#!/usr/bin/python3
"""
python file that contains the class
definition of a City and an instance Base = declarative_base():
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """class represent table for database"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
