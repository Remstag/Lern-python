import sqlite3

DB_NAME = "Database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        key TEXT NOT NULL
    )
    ''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kho (
            file_id INTEGER PRIMARY KEY AUTOINCREMENT,
            link TEXT NOT NULL,
            id_user INTEGER,
            FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE
    )
    ''')
    conn.commit()
    conn.close()