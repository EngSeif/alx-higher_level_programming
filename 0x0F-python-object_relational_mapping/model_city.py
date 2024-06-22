#!/usr/bin/python3
""" City Module """

from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
        City Class
    """
    __tablename__ = "cities"
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
    state_id = Column(
        INTEGER,
        ForeignKey('states.id'),
        nullable=False
        )
