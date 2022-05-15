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
