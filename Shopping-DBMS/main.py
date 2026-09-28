import sqlite3
from admin import admin_menu
from customer import customer_menu


def init_db():
    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(20) UNIQUE,
                    password TEXT,
                    role VARCHAR(20)
                    )
                    ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS categories(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category_name VARCHAR(50) UNIQUE
                    )
                    ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_name VARCHAR(50),
                    price REAL,
                    stock INTEGER,
                    category_id INTEGER,
                    FOREIGN KEY (category_id) REFERENCES categories(id)
                    )
                    ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS orders(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    order_date TEXT,
                    status VARCHAR(20),
                    total_amount REAL,
                    FOREIGN KEY (user_id) REFERENCES user(id)
                    )
                    ''')

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS order_items(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    order_id INTEGER,
                    product_id INTEGER,
                    quantity INTEGER,
                    price REAL,
                    FOREIGN KEY (order_id) REFERENCES orders(id),
                    FOREIGN KEY (product_id) REFERENCES products(id)
                    )
                    ''')

    # Seed default categories
    cursor.execute('''
                    INSERT OR IGNORE INTO categories(id, category_name)
                    VALUES(1, 'Electronics'), (2, 'Clothing')
                   ''')

    # Seed default admin account
    cursor.execute('''
                    INSERT OR IGNORE INTO user(username, password, role)
                    VALUES(?, ?, ?)
                   ''', ("admin", "admin123", "admin"))

    conn.commit()
    conn.close()


def register():
    print("\n--- Registration ---")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if not username:
        print("Username cannot be empty!")
        return

    if not password:
        print("Password cannot be empty!")
        return

    conn = sqlite3.connect("shopping.db")
    cursor = conn.cursor()

    try:
        cursor.execute('''
                        INSERT INTO user(username, password, role)
                        VALUES(?,?,?)
                       ''', (username, password, "customer"))

        conn.commit()
        print("Registration successful!")

    except sqlite3.IntegrityError:
        print("Username already exists!")

    except sqlite3.Error as e:
        print("Database error:", e)

    finally:
        conn.close()


def login():
    print("\n--- Login ---")

    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if not username:
            print("Username cannot be empty!")
            return None

        if not password:
            print("Password cannot be empty!")
            return None

        conn = sqlite3.connect("shopping.db")
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT * FROM user
                        WHERE username = ? AND password = ?
                       ''',
                       (username, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            print("Login successful!")
            print(f"Welcome {user[1]}")

            if user[3] == "admin":
                admin_menu()

            elif user[3] == "customer":
                customer_menu(user)

            return user

        else:
            print("Invalid username or password!")
            return None

    except sqlite3.Error as e:
        print("Database error:", e)
        return None


def main():
    init_db()

    while True:
        print("\n==============================")
        print("   ONLINE SHOPPING SYSTEM")
        print("==============================")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
