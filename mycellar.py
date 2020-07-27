import sqlite3

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
    SELECT * FROM customers;
""")

#fetchall returns a python object
print(c.fetchall())

conn.commit()

#Close the connection
conn.close()