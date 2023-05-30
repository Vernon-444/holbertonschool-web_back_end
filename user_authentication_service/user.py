#!/usr/bin/env python3
"""
Create SQLAlchemy Model for User
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base() # Base Class for SQLAlchemy model declaration


class User(Base):
    """
    User Class Definition
    """
    __tablename__ = 'users' # MySQL table name

    id = Column(Integer, primary_key=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
