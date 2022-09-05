CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firs_name varchar(50),
    last_name varchar(50),
    age INTEGER,
    email VARCHAR(100),
    role VARCHAR(50),
    phone VARCHAR(20)
);

CREATE TABLE Offer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    executor_id INTEGER
);

CREATE TABLE Order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    description VARCHAR(100),
    start_date DATE,
    end_date DATE,
    address VARCHAR(100),
    price INTEGER,
    customer_id INTEGER,
    executor_id INTEGER
)