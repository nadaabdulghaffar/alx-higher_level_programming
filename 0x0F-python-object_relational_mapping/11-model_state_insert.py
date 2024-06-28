#!/usr/bin/python3
"""adds the State object “Louisiana” to the database """


import sys
from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.creart_all(engine)
    session = sessionmaker(bind=engine)
    session = Session()
    newState = State("Louisiana")
    session.add(newState)
    session.commit()
    session.close()
