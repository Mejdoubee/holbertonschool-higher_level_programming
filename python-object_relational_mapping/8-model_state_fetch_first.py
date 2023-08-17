#!/usr/bin/python3
'''
script that prints the first State object from the database hbtn_0e_6_usa
'''
from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')
    session.close()
