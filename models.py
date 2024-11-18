from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    __table_args__ = (UniqueConstraint('email', name='unique_email'),)