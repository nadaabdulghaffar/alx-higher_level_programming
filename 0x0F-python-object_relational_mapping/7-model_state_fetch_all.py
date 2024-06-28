8-model_state_fetch_first.py
""" lists all State objects from the database"""


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
    States = session.query(State).order_by(State.id)

    for state in States:
        print("{}: {}".format(state.id, state.name))
    session.close()
