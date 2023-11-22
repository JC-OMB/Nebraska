# api/models.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from api.models.base import Base


class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    # other site-specific fields
    sensors = relationship("Sensor", back_populates="site")
