import sqlite3

def create_database():
    # Create a SQLite database connection
    conn = sqlite3.connect('project.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')

    # Create products table
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL NOT NULL
                    )''')

    # Insert sample data into users table
    cursor.execute("INSERT INTO users (username, password) VALUES ('rk0107', 'pass')")
    cursor.execute("INSERT INTO users (username, password) VALUES ('rohu', 'pass')")

    # Insert sample data into products table
    cursor.execute("INSERT INTO products (name, price) VALUES ('Product 1', 20.99)")
    cursor.execute("INSERT INTO products (name, price) VALUES ('Product 2', 20.49)")

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")
