import sqlite3

def create_connection():
    """
    Creates a connection to the password db and returns the cursor.
    """

    co = None

    try:
        co = sqlite3.connect('pass.db')
        cur = co.cursor()

    except Exception as e:
        print(e)

    return co, cur





def create_table():
    """
    Creates the password table if doesn't exist.
    """


    conn, cursor = create_connection()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS passwords(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    website TEXT,
    username TEXT,
    email TEXT,
    password TEXT
    )""")

    conn.commit()

    conn.close()

create_table()
