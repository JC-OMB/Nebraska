from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from api.models.base import Base


class Dataset(Base):
    __tablename__ = 'datasets'

    id = Column(Integer, primary_key=True)
    # fields representing dataset attributes
    metric_id = Column(Integer, ForeignKey('metrics.id'))
    metric = relationship("Metric", back_populates="datasets")
