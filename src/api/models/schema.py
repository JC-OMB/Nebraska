from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from api.models.base import Base


class Schema(Base):
    __tablename__ = 'schemas'

    id = Column(Integer, primary_key=True)
    # Other schema-specific fields
    dataset_id = Column(Integer, ForeignKey('datasets.id'))
    dataset = relationship("Dataset", back_populates="schema")
