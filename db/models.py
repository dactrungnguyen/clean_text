from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, String

engine = create_engine('db/clean_text.db')
Base = declarative_base()


class Run(Base):
    __tablename__ = 'runs'
    id = Column(String, primary_key=True)
    input = Column(String)
    output = Column(String)