#!/usr/bin/python3
"""
file that contains the class definition of a State
"""

from sqlalchemy import Columan, String, Integer
from sqlalchemy.esxt.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class of the definition of a State and an instance Base
    states table:
        id:Primary Key
        name: name of the state
    """

    __tablename__ = 'states'
    id = Columan(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Columan(String(128), nullable=False)
