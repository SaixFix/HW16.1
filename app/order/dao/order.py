from sqlalchemy import Column, INTEGER, String, Date, Numeric
from main import db


class Order(db.Model):
    __tablename__ = "offer"

    id = Column(INTEGER, primary_key=True)
    name = Column(String(50))
    description = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)
    address = Column(String(100))
    price = Column(Numeric)
    customer_id = Column(INTEGER)
    executor_id = Column(INTEGER)
