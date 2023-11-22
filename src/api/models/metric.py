from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.models.base import Base


class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sensor_id = Column(Integer, ForeignKey('sensors.id'))
    sensor = relationship("Sensor", back_populates="metrics")
    datasets = relationship("Dataset", back_populates="metric")
