#!/usr/bin/python3
"""
This script deletes all objects with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the database.
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_url)
    Session = sessionmaker(bind=eng)

    session = Session()

    for instances in session.query(State).filter(State.name.contains('a')):
        session.delete(instances)

    session.commit()
    session.close()
