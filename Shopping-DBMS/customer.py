import sqlite3
from admin import view_products, get_db


def place_order(user):
    print("\n--- Place Order ---")

    try:
        view_products()

        product_id = int(input("\nEnter product id: "))

        conn = get_db()
        cursor = conn.cursor()

        # Check whether product exists
        cursor.execute('''
                        SELECT id, product_name, price, stock
                        FROM products
                        WHERE id = ?
                       ''', (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found!")
            conn.close()
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0!")
            conn.close()
            return

        if quantity > product[3]:
            print("Not enough stock!")
            conn.close()
            return

        total_amount = product[2] * quantity

        cursor.execute('''
                        INSERT INTO orders(user_id, order_date, status, total_amount)
                        VALUES(?, date('now'), ?, ?)
                       ''',
                       (user[0], "Placed", total_amount))

        order_id = cursor.lastrowid

        cursor.execute('''
                        INSERT INTO order_items(order_id, product_id, quantity, price)
                        VALUES(?,?,?,?)
                       ''',
                       (order_id, product_id, quantity, product[2]))

        cursor.execute('''
                        UPDATE products
                        SET stock = stock - ?
                        WHERE id = ?
                       ''',
                       (quantity, product_id))

        conn.commit()
        conn.close()

        print("Order placed successfully!")
        print(f"Total amount: Rs.{total_amount}")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_my_orders(user):
    print("\n--- My Orders ---")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT id, order_date, status, total_amount
                    FROM orders
                    WHERE user_id = ?
                   ''', (user[0],))

    orders = cursor.fetchall()
    conn.close()

    if orders:
        for order in orders:
            print(f"Order ID: {order[0]}")
            print(f"Date: {order[1]}")
            print(f"Status: {order[2]}")
            print(f"Total: Rs.{order[3]}")
            print("-------------------")
    else:
        print("You have no orders.")


def customer_menu(user):
    while True:
        print("\n--- Customer Menu ---")
        print("1. View Products")
        print("2. Place Order")
        print("3. View My Orders")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            place_order(user)

        elif choice == "3":
            view_my_orders(user)

        elif choice == "4":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")
