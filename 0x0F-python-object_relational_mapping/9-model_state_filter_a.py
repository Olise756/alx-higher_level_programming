#!/usr/bin/python3

"""
This script displays all State objects
that has the letter `a`
from the database `hbtn_0e_6_usa`.
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

    for instances in session.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instances.id, instances.name))
