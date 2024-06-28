#!/usr/bin/python3
"""prints the first State object from the database"""

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
    state = session.query(State).first()
    print("{}: {}".format(state.id, state.name) if state else "Nothing")
    session.close()
