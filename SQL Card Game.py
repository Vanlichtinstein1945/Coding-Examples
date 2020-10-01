import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite3 database """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None

def select_all_names(conn, sql):
    """ Query all rows in the tasks table """
    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()

    ar=[r[0] for r in rows]

    for entry in ar:
        print(entry)

def write_an_entry(conn, sql):
    """ Write an entry into the table """
    cur = conn.cursor()
    cur.execute(sql)

def create_a_table(conn, sql):
    """ Create a table using a comment """
    cur = conn.cursor()
    cur.execute(sql)

sql_create_table = """ CREATE TABLE IF NOT EXISTS SLUG_CARDS (
                           id INTEGER PRIMARY KEY,
                           name TEXT); """

sql_select_name = """ SELECT SLUG_CARDS.name FROM SLUG_CARDS; """

sql_slug_entry = """ INSERT INTO SLUG_CARDS (name) VALUES ("Slug"); """

def main():
    database = "SLUG_CARDS.db"

    # Create a database connection
    conn = create_connection(database)
    conn.text_factory = str
    with conn:
        print("1. Create a database by name:")
        create_a_table(conn, sql_create_table)

        print("2. Writing an entry into the database:")
        write_an_entry(conn, sql_slug_entry)

        print("3. Query the database for all information:")
        select_all_names(conn, sql_select_name)

if __name__ == "__main__":
    main()
