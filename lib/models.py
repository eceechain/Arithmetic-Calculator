from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CalculationHistory(Base):
    __tablename__ = 'calculation_history'
    id = Column(Integer, primary_key=True)
    expression = Column(String, nullable=False)
    result = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

engine = create_engine('sqlite:///calculator.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
