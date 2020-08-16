import sys
import sqlite3
import eel

eel.init('web')

@eel.expose
def search_db(dummy_param):
    print("Searching DB with value (" + str(dummy_param) + " ) ...")
    return "this is my result"


def init_db():
    conn = sqlite3.connect('data/cellar.db')
    c = conn.cursor()

    c.execute(""" --begin-sql
        CREATE TABLE IF NOT EXISTS red_wine (

        );
    """)

    c.execute(""" --begin-sql
        CREATE TABLE IF NOT EXISTS WHITE_wINE (

        );
    """)


def test_db():
    #Connect to a database
    conn = sqlite3.connect(':memory:')

    #Create a cursor
    c = conn.cursor()

    #sqllist3 datatypes:
    #NULL, INTEGER, REAL, TEXT, BLOB

    #Create a Table
    c.execute(""" --begin-sql
        CREATE TABLE customers ( 
            first_name text, 
            last_name text, 
            email text 
        );
    """)

    c.execute(""" --begin-sql
        INSERT INTO customers VALUES (
            'John', 'Elder', 'john@thismann.com'
        );
    """)

    many_customers = [
        ('Big', 'Ben', 'tower@mail.com'), 
        ('Jerry', 'Seinfled', 'jerry@sienfeld.com'), 
        ('Hillary', 'Clinton', 'clinton@mail.gov'),
    ]

    c.executemany(""" --begin-sql
        INSERT INTO customers VALUES (?,?,?);
    """, many_customers)

    #Commit changes to the db
    conn.commit()

    c.execute(""" --begin-sql
        SELECT * FROM customers WHERE last_name = 'Clinton';
    """)

    #fetchall returns a python object
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()

    #Close the connection
    conn.close()

def on_close(page, sockets):
    print(page, 'closed')
    print('Still have sockets open to', sockets)

def run():
    eel.start('home.html', size=(1000,600), close_callback=(lambda page, sockets: sys.exit()))


if __name__ == '__main__':
    run()