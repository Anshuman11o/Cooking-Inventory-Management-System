import sqlite3 #importing sqlite3-Database

def connect():
    conn = sqlite3.connect("app.db") #connecting with sqlite and making a new DB file
    cur = conn.cursor()
    #creating 4 tables and setting primary key for each table (making use of DDL)
    cur.execute("CREATE TABLE IF NOT EXISTS inventory (rm TEXT Primary KEY, al integer, cpm integer, au integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS orders (oid INTEGER Primary KEY, cn text, dno text, qo integer, od text)")
    cur.execute("CREATE TABLE IF NOT EXISTS menu (dnm TEXT Primary KEY, pn integer)")
    cur.execute("CREATE TABLE IF NOT EXISTS reports (id INTEGER Primary KEY, tc integer, tr integer, tp integer)")
    conn.commit()
    conn.close()

#insert_reports function for the reports table to calculate and update attributes (making use of DML)
def insert_report():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    #carrying out calculations from inventory table to get the calculated data and store it in cost variable
    cur.execute("SELECT SUM(cpm * au) FROM inventory") 
    cost = cur.fetchall()[0][0]
    #selecting similar records from menu and orders table to calculate the revenue variable below
    cur.execute("SELECT SUM(orders.qo * menu.pn) FROM orders INNER JOIN menu ON orders.dno = menu.dnm") 
    revenue = cur.fetchall()[0][0]
    profit = revenue - cost
    cur.execute("UPDATE reports SET tc=?, tr=?, tp=? WHERE id=1",(cost,revenue,profit))
    conn.commit()
    conn.close()   

#view function to view the tuples from the report table
def view_report():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM reports")
    rows=cur.fetchall()
    conn.close()
    return rows

#insert function to add values in the menu table through user input
def insert_men(dnm,pn): #assigning parameters for user input
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO menu VALUES (?,?)",(dnm,pn)) #inserting values stored in the variables to every attribute in the table
    conn.commit()
    conn.close()
#view function to get the tuples from the menu table
def view_men():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM menu")
    rows=cur.fetchall()
    conn.close()
    return rows
#delete function to delete selected records from the menu table
def delete_men(dnm):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM menu WHERE dnm=?",(dnm,))
    conn.commit()
    conn.close()
#update function to update values of a selected record in the menu table
def update_men(dnm,pn):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("UPDATE menu SET pn=? WHERE dnm=?",(pn,dnm))
    conn.commit()
    conn.close()

#similar insert, view, delete, and update function for the orders table
def insert_ord(cn,dno,qo,od):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO orders VALUES (NULL,?,?,?,?)",(cn,dno,qo,od))
    conn.commit()
    conn.close()

def view_ord():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_ord(oid):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM orders WHERE oid=?",(oid,))
    conn.commit()
    conn.close()

def update_ord(oid,cn,dno,qo,od):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("UPDATE orders SET cn=?, dno=?, qo=?, od=? WHERE oid=?",(cn,dno,qo,od,oid))
    conn.commit()
    conn.close()


#similar insert, view, delete, and update function for the inventory table
def insert(rm,al,cpm,au):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO inventory VALUES (?,?,?,?)",(rm,al,cpm,au))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM inventory")
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(rm):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM inventory WHERE rm=?",(rm,))
    conn.commit()
    conn.close()

def update(rm,al,cpm,au):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute("UPDATE inventory SET al=?, cpm=?, au=? WHERE rm=?",(al,cpm,au,rm))
    conn.commit()
    conn.close()
    


connect() #calling the connect method to run the backend



#print(view_men())
#print(view_ord())
#print(view())
#print(view_report())