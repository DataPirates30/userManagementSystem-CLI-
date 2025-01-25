import sqlite3
from file_handling import log_activity
#connect to the database(of create if it doesn't exist) 
def get_db_connection():
    conn = sqlite3.connect('user_database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the users table
def create_users_table():
    conn = get_db_connection()
    conn.execute('DROP TABLE IF EXISTS users')
    conn.execute("""
    CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                age INTEGER NOT NULL
                )""")
    conn.commit()
    conn.close()

# insert data into the users table
def create_user(name,email,age):
    conn = get_db_connection()
    conn.execute("INSERT INTO users(name,email,age) VALUES(?,?,?)",(name,email,age))
    conn.commit()
    conn.close()
    log_activity(f"User created: {name}, {email}, {age}")

#get the data from the users table
def get_all_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    
    return users

    # Update the users table
def update_user(id,name=None,email=None,age=None):
    conn  = get_db_connection()
    if name:
        conn.execute("UPDATE users SET name=? WHERE id=?",(name,id))
    if email:
        conn.execute("UPDATE users SET email = ? WHERE id = ?",(email,id))
    if age:
        conn.execute("UPDATE users SET age = ? WHERE id = ?",(age,id))
    conn.commit()
    conn.close()
    log_activity(f"User updated: ID {id}")

# Delete the users table from the database
def delete_user(id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM users WHERE id = ?",(id,)
    )
    conn.commit()
    conn.close()
    log_activity(f"User deleted: ID {id}")

create_users_table()





