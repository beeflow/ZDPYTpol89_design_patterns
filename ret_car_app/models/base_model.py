import re
from typing import Optional

from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, joinedload

from ret_car_app.settings import SessionLocal

Base = declarative_base()


class QueryManager:
    """Zbugowany QueryManager!!!! ;P """

    def __init__(self, model, session=SessionLocal):
        self.model = model
        self.session = session()

    def create(self, **kwargs):
        obj = self.model(**kwargs)
        self.session.add(obj)
        self.session.commit()
        self.session.refresh()
        self.session.flush(obj)

        return obj

    def get_or_create(self, **kwargs):
        created = False

        if not (obj := self.get(**kwargs)):
            obj = self.create(**kwargs)
            created = True

        return created, obj

    def filter(self, **kwargs):
        return self.select_related().filter_by(**kwargs)

    def get(self, **kwargs):
        return self.select_related().filter_by(**kwargs).one_or_none()

    def select_related(self, *relations):
        query = self.session.query(self.model)

        for rel in relations:
            query = query.options(joinedload(getattr(self.model, rel)))

        return query


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    objects: Optional[QueryManager] = None  # placeholder

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if not hasattr(cls, "__tablename__"):
            cls.__tablename__ = re.sub(r'(?<!^)(?=[A-Z])', '_', cls.__name__).lower()

        if cls.objects is None:
            cls.objects = QueryManager(cls)
