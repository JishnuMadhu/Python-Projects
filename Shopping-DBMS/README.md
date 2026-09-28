# Online Shopping Management System

A simple command-line online shopping system built with Python and SQLite.

## Features

- User registration and login
- Role-based access (Admin and Customer)
- Admin can add, view, update, and delete products
- Admin can view all customer orders
- Customer can view products, place orders, and view order history
- Stock automatically decreases when an order is placed
- Input validation and error handling

## Technologies Used

- Python 3
- SQLite3 (built-in with Python)

## Database Tables

The system uses 5 tables with the following relationships:

1. **user** - Stores registered users (id, username, password, role)
2. **categories** - Stores product categories (id, category_name)
3. **products** - Stores products (id, product_name, price, stock, category_id → categories)
4. **orders** - Stores orders (id, user_id → user, order_date, status, total_amount)
5. **order_items** - Stores order details (id, order_id → orders, product_id → products, quantity, price)

Foreign key relationships:
- products.category_id → categories.id
- orders.user_id → user.id
- order_items.order_id → orders.id
- order_items.product_id → products.id

## How to Run

1. Make sure Python 3 is installed on your computer
2. Open a terminal and navigate to the project folder
3. Run the program:

```
python main.py
```

The database (shopping.db) is created automatically on first run.

## Default Admin Account

- Username: admin
- Password: admin123

## Customer Registration

1. Choose "Register" from the main menu
2. Enter a username and password
3. You will be registered as a customer
4. Use "Login" to access the customer menu

## Project Structure

```
Online Shopping Management System/
├── main.py          - Main program, database setup, authentication
├── admin.py         - Admin menu and product/order management
├── customer.py      - Customer menu, ordering, and order history
├── shopping.db      - SQLite database (auto-created)
└── README.md        - Project documentation
```
