import sqlite3
# Query the database and return all records
def show_all():
    # connect to database
    conn=sqlite3.connect('customer.db')
    # create a cursor
    cursor=conn.cursor()
    # Query the database
    cursor.execute(" select rowid, * from customers ")
    item=cursor.fetchall()
    for row in item:
        print(row)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()
# Add a new record to the table
def add_one(first,last,email):
    conn=sqlite3.connect('customer.db')
    cursor=conn.cursor()
    cursor.execute("insert into customers values (?,?,?)",(first,last,email))
    conn.commit()
    conn.close()
# Delete a record from the table
def delete_one(id):
    conn=sqlite3.connect('customer.db')
    cursor=conn.cursor()
    cursor.execute("delete from customers where rowid =(?)",(id,))
    item=cursor.fetchall()
    for row in item:
        print(row)
    conn.commit()
    conn.close()
# Add many record function
def add_many(list):
    conn=sqlite3.connect('customer.db')
    cursor=conn.cursor()
    cursor.executemany("insert into customers values (?,?,?)",list)
    conn.commit()
    conn.close()
# Where clause function
def email_lookup(email):
    conn=sqlite3.connect('customer.db')
    cursor=conn.cursor()
    cursor.execute("select * from customers where email_address = (?)",(email,))
    item=cursor.fetchall()
    for row in item:
        print(row)
    conn.commit()
    conn.close()
