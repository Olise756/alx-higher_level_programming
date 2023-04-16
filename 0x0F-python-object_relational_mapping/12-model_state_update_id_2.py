#!/usr/bin/python3

"""
This script updates the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    """
    Updates a State object on the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    session = Session()

    new_name = session.query(State).filter(State.id == '2').first()
    new_name.name = 'New Mexico'
    session.commit()
    session.close()
