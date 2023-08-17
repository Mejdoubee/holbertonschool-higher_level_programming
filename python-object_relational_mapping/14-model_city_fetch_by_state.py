#!/usr/bin/python3
'''
script that lists all City objects from the database hbtn_0e_14_usa
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
