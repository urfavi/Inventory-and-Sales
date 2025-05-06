# controllers/inventory_controller.py
from db.database import connect_db

def view_inventory():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    inventory = cur.fetchall()
    conn.close()
    return inventory

def add_stock(name, quantity, price):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)", 
                (name, quantity, price))
    conn.commit()
    conn.close()
