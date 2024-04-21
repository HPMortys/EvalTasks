from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

Base = declarative_base()


class UserDTO(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_orm = True
        validate_assignment = True
        from_attributes = True


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, unique=True)
    email = Column(String, index=True, unique=True)
