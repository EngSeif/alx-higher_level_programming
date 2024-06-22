#!/usr/bin/python3
""" Show ALL """
from sys import argv
from model_state import Base, State
from model_city import City


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    R = session.query(State.name, City.id, City.name)
    Q = R.filter(City.state_id == State.id).order_by(City.id).all()
    for r in Q:
        print("{}: ({}) {}".format(r[0], r[1], r[2]))
    session.close()
