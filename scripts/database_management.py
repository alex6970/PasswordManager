import sqlite3

def create_connection():
    """
    Creates a connection to the password db and returns the cursor.
    """

    co = None
    cur = None

    try:
        co = sqlite3.connect('database/pass.db')
        cur = co.cursor()

    except Exception as e:
        print(e)

    return co, cur





def close_connection(co):
    """
    Closes the current a connection to the password db.
    """

    try:
        co.commit()
        co.close()

    except Exception as e:
        print(e)






def create_pw_table():
    """
    Creates the Password Table if doesn't exist.
    """


    conn, cursor = create_connection()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS passwords(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    website TEXT,
    username TEXT,
    email TEXT,
    password TEXT
    )""")

    close_connection(conn)

 # Create the database when used for the first time
# create_pw_table()
