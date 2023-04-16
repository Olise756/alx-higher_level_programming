#!/usr/bin/python3

"""
This script prints out all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_url)
    Session = sessionmaker(bind=eng)

    session = Session()

    query = session.query(City, State).join(State)

    for c, s in query.all():
        print("{}: ({:d}) {}".format(s.name, c.id, c.name))

    session.commit()
    session.close()
