from .database import Base
from sqlalchemy import Boolean, Integer, String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


# 'Base' vem do database

class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship("User", back_populates="blogs")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship("Blog", back_populates="author")

