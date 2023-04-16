#!/usr/bin/python3

"""
This script prints out the State object id
with the name passed as an arg from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """
    Access to the database and get a state
    from the there.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    session = Session()
    instances = session.query(State).filter(State.name == argv[4]).first()

    if instances is None:
        print('Not found')
    else:
        print('{0}'.format(instances.id))
