#!/usr/bin/python3
'''
script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter_by(name=argv[4]).first():
        if state:
            print(state.id)
        else:
            print("Not found")
    session.close()
