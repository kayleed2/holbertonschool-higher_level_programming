#!/usr/bin/python3
""" Connects to db using SQLalchemy, contains class State and instance """

from sqlalchemy import (create_engine, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqldb://root:root@localhost:3306/mydb")
Base = declarative_base()


class State(Base):
    """Defines State Class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))

    def __repr__(self):
        """Defines representation"""
        return """<User(name='%s',
        fullname='%s',
        nickname='%s')>""" % (self.name, self.fullname, self.nickname)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
