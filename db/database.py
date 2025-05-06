# db/database.py
import psycopg2

def connect_db():
    try:
        conn = psycopg2.connect(
            host="localhost", dbname="InventorySalesSystem", user="gaile", password="gaile"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None