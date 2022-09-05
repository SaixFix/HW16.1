from sqlalchemy import Column, INTEGER, String
from main import db


class Offer(db.Model):
    __tablename__ = "offer"

    id = Column(INTEGER, primary_key=True)
    order_id = Column(INTEGER)
    executor_id = Column(INTEGER)



