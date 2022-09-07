from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from utils import load_users, load_offers, load_orders

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


# Создаем таблицу User
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    firs_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(20))


# Создаем таблицу Offer
class Offer(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    executor_id = db.Column(db.Integer)


# Создаем таблицу Order
class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    start_date = db.Column(db.String(10))
    end_date = db.Column(db.String(10))
    address = db.Column(db.String(100))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey(User.id))
    executor_id = db.Column(db.Integer, db.ForeignKey(User.id))


db.drop_all()
db.create_all()

# получаем данные из users.json
users = load_users()

# создаем экземпляры user
list_users = []
for user in users:
    user["id"] = User(firs_name=user["first_name"],
                      last_name=user["last_name"],
                      age=user["age"],
                      email=user["email"],
                      role=user["role"],
                      phone=user["phone"]
                      )
    list_users.append(user["id"])

# получаем данные из offers.json
offers = load_offers()

# создаем экземпляры offer
list_offers = []
for offer in offers:
    offer["id"] = Offer(order_id=offer["order_id"],
                        executor_id=offer["executor_id"]
                        )
    list_offers.append(offer["id"])

# получаем данные из orders.json
orders = load_orders()

# создаем экземпляры order
list_orders = []
for order in orders:
    order["id"] = Order(name=order["name"],
                        description=order["description"],
                        start_date=order["start_date"],
                        end_date=order["end_date"],
                        address=order["address"],
                        price=order["price"],
                        customer_id=order["customer_id"],
                        executor_id=order["executor_id"]
                        )
    list_orders.append(order["id"])

db.session.add_all(list_users)
db.session.add_all(list_offers)
db.session.add_all(list_orders)

db.session.commit()


@app.route('/users')
def get_all_users():
    """Выводим всех юзеров"""
    users_list = User.query.all()

    user_response = []

    for user in users_list:
        user_response.append({
            "id": user.id,
            "first_name": user.firs_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        })
    return jsonify(user_response)


@app.route('/users/<int:id>')
def get_chose_user(id):
    """Выводим юзера по номеру"""
    user = User.query.get(id)
    user_spec = {
        "id": user.id,
        "first_name": user.firs_name,
        "last_name": user.last_name,
        "age": user.age,
        "email": user.email,
        "role": user.role,
        "phone": user.phone
    }
    return jsonify(user_spec)


@app.route('/orders')
def get_all_orders():
    """Выводим все заказы"""
    orders_list = Order.query.all()

    order_response = []

    for order in orders_list:
        order_response.append({
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    })
    return jsonify(order_response)


@app.route('/orders/<int:id>')
def get_chose_order(id):
    """Выводим заказ по номеру"""
    order = Order.query.get(id)
    order_spec = {
        "id": order.id,
        "name": order.name,
        "description": order.description,
        "start_date": order.start_date,
        "end_date": order.end_date,
        "address": order.address,
        "price": order.price,
        "customer_id": order.customer_id,
        "executor_id": order.executor_id
    }
    return jsonify(order_spec)


if __name__ == "__main__":
    app.run(debug=True)
