import sqlite3
conn=sqlite3.connect('customer.db')
# create a database table
# create a cursor
cursor=conn.cursor()
# create a table
cursor.execute("""CREATE TABLE customers (
    first_name text,
    last_name text,
    email_address text
    )""")
# Data types in sqlite
# NULL
# INTEGER 456,6789
# REAL 09.9999
# TEXT
# BLOB IMAGEFILE, MP3 FILE

# insert one record into the table.
        # cursor.execute("INSERT INTO customers VALUES ('surender','pal','surender.pal@groundtruth.com')")
        # cursor.execute("INSERT INTO customers VALUES ('rahul','yadav','rahul.yadav@groundtruth.com')") 
        # cursor.execute("INSERT INTO customers VALUES ('upika','pal','upika.pal@outlook.com')")
        # cursor.execute("INSERT INTO customers VALUES ('surender','kuman','surender.kumar@outlook.com')")
        # cursor.execute("INSERT INTO customers VALUES ('roopa','pal','roopa.pal@gmail.com')")


# insert many record into the table
many_customer=[
                ('surender','pal','surender@pal.com'),
                ('rahul','pal','rahul@pal.com'),
                ('upika','pal','upika@pal.com'),
                ('roopa','pal','roop@pal.com'),
                ('mansi','kumari','mansi@kumari.com'),
            ]
cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customer) # ? is placeholder and list of tuples is passed as mutliple values


# Query and fetch all 
        # cursor.execute("SELECT * FROM customers")
        # # cursor.fetchone() #fetch first item from the table
        # # cursor.fetchmany(3) #fetch no of items passes as parameter
        # # cursor.fetchall() #fetch all from table
        # # print(cursor.fetchone())
        # # print(cursor.fetchmany(5))
        # items=cursor.fetchall()
        # # print(items)
        # print('FName' + '\t\tLName'+ "\t\tEmail")
        # print('-----' + '\t\t-----'+ '\t\t-----')
        # for row in items:
        #     print(row[0] + " \t\t " + row[1] + " \t\t " + row[2])


# Primary key Id
        # cursor.execute("SELECT rowid, * FROM customers") #rowid is the primary key
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)


# Where clause with LIKE WILDCARD
        # cursor.execute("SELECT * FROM customers WHERE last_name='kumari'")
        # cursor.execute("SELECT * FROM customers WHERE last_name LIKE 'ku%' ")
        # cursor.execute("SELECT * FROM customers WHERE email_address LIKE '%outlook.com' ")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# Update records 
        # cursor.execute("SELECT rowid, * FROM customers")
        # cursor.execute("""UPDATE customers SET first_name= 'sure'
        #                   WHERE first_name = 'surender'
        # """)
        # cursor.execute("SELECT rowid,* FROM customers")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# Delete records 
        # cursor.execute("DELETE FROM customers WHERE rowid BETWEEN 4 AND 6")
        # cursor.execute('SELECT rowid, * FROM customers')
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# Order result by
        # cursor.execute("SELECT rowid, * FROM customers ORDER BY first_name DESC")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)


# And or Or 
        # cursor.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'up%' OR rowid =3 ")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# Limit 
        # cursor.execute("select rowid, * from customers order by rowid desc limit 4")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# Delete a table
        # cursor.execute("drop table customers")
        # items=cursor.fetchall()
        # for row in items:
        #     print(row)

# commit our command
conn.commit()
# close our connection
conn.close()



