from sqlalchemy import Column, INTEGER, String
from main import db


class User(db.Model):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True)
    firs_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(INTEGER)
    email = Column(String(100))
    role = Column(String(50))
    phone = Column(String(20))
