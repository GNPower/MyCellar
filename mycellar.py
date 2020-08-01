import sqlite3
import eel

eel.init('web')

@eel.expose
def search_db(dummy_param):
    print("Searching DB with value (" + str(dummy_param) + " ) ...")
    return "this is my result"


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

eel.start('home.html', size=(1000,600))