from datetime import datetime
from pytz import timezone

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(tz=timezone('America/Sao_Paulo')))
    updated_at = Column(DateTime, nullable=True)

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        return self

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


