
from sqlalchemy import Integer, String, Column
from database.base import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    