#!/usr/bin/python3
""" lists all State objects that contain the letter a from the database"""

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
    states = session.query(State) \
        .filter(State.name.like("%a%")) \
        .order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
