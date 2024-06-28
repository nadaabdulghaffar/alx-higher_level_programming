#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""

import sys
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    StateName = sys.argv[4]

    statepassed = session.query(State).filter(State.name == StateName).first()
    print("{}".format(statepassed.id) if statepassed else "Not found")
    session.close()
