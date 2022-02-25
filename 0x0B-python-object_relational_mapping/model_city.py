#!/usr/bin/python3
""" Connects to db using SQLalchemy, contains class State and instance """

from sqlalchemy import (create_engine, Column, String, Integer, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """Defines State Class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
