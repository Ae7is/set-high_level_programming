#!/usr/bin/python3
"""Defines the City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """Represents a city in the cities table."""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(
        Integer, ForeignKey("states.id"), nullable=False
    )

    state = relationship("State", back_populates="cities")
