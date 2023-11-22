from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.models.base import Base


class Sensor(Base):
    __tablename__ = 'sensors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    site_id = Column(Integer, ForeignKey('sites.id'))
    site = relationship("Site", back_populates="sensors")
    metrics = relationship("Metric", back_populates="sensor")
