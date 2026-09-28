import sqlite3


def get_db():
    conn = sqlite3.connect("shopping.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def view_categories():
    print("\n--- Categories ---")
    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, category_name FROM categories ORDER BY id")
        categories = cursor.fetchall()
        conn.close()

        if categories:
            for cat in categories:
                print(f"ID: {cat[0]} | Name: {cat[1]}")
        else:
            print("No categories found.")
    except sqlite3.Error as e:
        print("Database error:", e)


def add_category():
    print("\n--- Add Category ---")
    category_name = input("Enter category name: ").strip()

    if not category_name:
        print("Category name cannot be empty!")
        return

    try:
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categories(category_name) VALUES(?)", (category_name,))
        conn.commit()
        conn.close()
        print(f"Category '{category_name}' added successfully!")
    except sqlite3.IntegrityError:
        print("Category already exists!")
    except sqlite3.Error as e:
        print("Database error:", e)


def view_products():
    print("\n--- Products ---")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT products.id,
                           products.product_name,
                           products.price,
                           products.stock,
                           categories.category_name
                    FROM products
                    JOIN categories
                    ON products.category_id = categories.id
                   ''')

    products = cursor.fetchall()
    conn.close()

    if products:
        for product in products:
            print(f"ID: {product[0]}")
            print(f"Name: {product[1]}")
            print(f"Price: {product[2]}")
            print(f"Stock: {product[3]}")
            print(f"Category: {product[4]}")
            print("-------------------")
    else:
        print("No products available.")


def add_product():
    print("\n--- Add Product ---")

    try:
        product_name = input("Enter product name: ").strip()

        if not product_name:
            print("Product name cannot be empty!")
            return

        price = float(input("Enter price: "))
        stock = int(input("Enter stock: "))

        if price < 0:
            print("Price cannot be negative!")
            return

        if stock < 0:
            print("Stock cannot be negative!")
            return

        # Show available categories so user doesn't have to guess
        view_categories()
        category_id = int(input("\nEnter category id: "))

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT id
                        FROM categories
                        WHERE id = ?
                       ''', (category_id,))

        category = cursor.fetchone()

        if category is None:
            print("Invalid category id!")
            conn.close()
            return

        cursor.execute('''
                        INSERT INTO products(product_name, price, stock, category_id)
                        VALUES(?,?,?,?)
                       ''',
                       (product_name, price, stock, category_id))

        conn.commit()
        conn.close()

        print("Product added successfully!")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as e:
        print("Database error:", e)


def update_product():
    print("\n--- Update Product ---")

    try:
        product_id = int(input("Enter product id: "))

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT id
                        FROM products
                        WHERE id = ?
                       ''', (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found!")
            conn.close()
            return

        product_name = input("Enter new product name: ").strip()

        if not product_name:
            print("Product name cannot be empty!")
            conn.close()
            return

        price = float(input("Enter new price: "))
        stock = int(input("Enter new stock: "))

        if price < 0:
            print("Price cannot be negative!")
            conn.close()
            return

        if stock < 0:
            print("Stock cannot be negative!")
            conn.close()
            return

        # Show categories
        view_categories()
        category_id = int(input("\nEnter new category id: "))

        cursor.execute('''
                        SELECT id
                        FROM categories
                        WHERE id = ?
                       ''', (category_id,))

        category = cursor.fetchone()

        if category is None:
            print("Invalid category id!")
            conn.close()
            return

        cursor.execute('''
                        UPDATE products
                        SET product_name = ?,
                            price = ?,
                            stock = ?,
                            category_id = ?
                        WHERE id = ?
                       ''',
                       (product_name, price, stock, category_id, product_id))

        conn.commit()
        conn.close()

        print("Product updated successfully!")

    except ValueError:
        print("Please enter valid numbers!")

    except sqlite3.Error as e:
        print("Database error:", e)


def delete_product():
    print("\n--- Delete Product ---")

    try:
        product_id = int(input("Enter product id: "))

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT id
                        FROM products
                        WHERE id = ?
                       ''', (product_id,))

        product = cursor.fetchone()

        if product is None:
            print("Product not found!")
            conn.close()
            return

        ch = input("Are you sure you want to delete this product? (Y/N): ").lower()

        if ch == "y":
            cursor.execute('''
                            DELETE FROM products
                            WHERE id = ?
                           ''', (product_id,))

            conn.commit()
            print("Product deleted successfully!")

        else:
            print("Product not deleted!")

        conn.close()

    except ValueError:
        print("Please enter a valid product id!")

    except sqlite3.Error as e:
        print("Database error:", e)


def view_all_orders():
    print("\n--- All Orders ---")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
                    SELECT orders.id,
                           user.username,
                           orders.order_date,
                           orders.status,
                           orders.total_amount
                    FROM orders
                    JOIN user
                    ON orders.user_id = user.id
                   ''')

    orders = cursor.fetchall()
    conn.close()

    if orders:
        for order in orders:
            print(f"Order ID: {order[0]}")
            print(f"Customer: {order[1]}")
            print(f"Date: {order[2]}")
            print(f"Status: {order[3]}")
            print(f"Total: Rs.{order[4]}")
            print("-------------------")
    else:
        print("No orders available.")


def update_order_status():
    print("\n--- Update Order Status ---")

    try:
        view_all_orders()
        order_id = int(input("\nEnter Order ID to update: "))

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("SELECT id, status FROM orders WHERE id = ?", (order_id,))
        order = cursor.fetchone()

        if not order:
            print("Order not found!")
            conn.close()
            return

        print(f"Current Status: {order[1]}")
        print("Select new status:")
        print("1. Processing")
        print("2. Shipped")
        print("3. Delivered")
        print("4. Cancelled")
        print("5. Custom Status")

        choice = input("Enter choice (1-5): ").strip()
        status_map = {
            "1": "Processing",
            "2": "Shipped",
            "3": "Delivered",
            "4": "Cancelled"
        }

        if choice in status_map:
            new_status = status_map[choice]
        elif choice == "5":
            new_status = input("Enter custom status: ").strip()
            if not new_status:
                print("Status cannot be empty!")
                conn.close()
                return
        else:
            print("Invalid choice!")
            conn.close()
            return

        cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, order_id))
        conn.commit()
        conn.close()

        print(f"Order #{order_id} status updated to '{new_status}' successfully!")

    except ValueError:
        print("Please enter a valid Order ID!")
    except sqlite3.Error as e:
        print("Database error:", e)


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. View Categories")
        print("6. Add Category")
        print("7. View All Orders")
        print("8. Update Order Status")
        print("9. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            update_product()

        elif choice == "4":
            delete_product()

        elif choice == "5":
            view_categories()

        elif choice == "6":
            add_category()

        elif choice == "7":
            view_all_orders()

        elif choice == "8":
            update_order_status()

        elif choice == "9":
            print("Logged out successfully!")
            break

        else:
            print("Invalid choice!")
