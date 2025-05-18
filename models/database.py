import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname="inventory_sales_system", user="postgres", password="Agjc101404!", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    # Method to connect to the database
    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connection to the database established successfully.")
        except Exception as e:
            print(f"Error connecting to the database: {str(e)}")

    # Method to execute a query
    def execute_query(self, query, params=None, fetch_all=True):
        if not self.connection:
            print("No active database connection.")
            return None
        
        try:
            self.cursor.execute(query, params)
            if query.strip().upper().startswith(('SELECT', 'SHOW')):
                if fetch_all:
                    return self.cursor.fetchall()
                else:
                    return self.cursor.fetchone()
            else:
                self.connection.commit()
                return self.cursor.rowcount
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None

    # Close the connection
    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")
