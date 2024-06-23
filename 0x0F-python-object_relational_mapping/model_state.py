#!/usr/bin/python3
""" State Module """

from sqlalchemy import Column, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        State Class
    """
    __tablename__ = "states"
    id = Column(
                "id", INTEGER,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )
    name = Column(
        "name",
        VARCHAR(128),
        nullable=False
        )
