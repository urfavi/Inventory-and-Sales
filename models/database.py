import psycopg2

class Database:
    def __init__(self, dbname="inventory_sales_system", user="postgres", password="Agjc101404!", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        print("DEBUG: Database __init__ called - using the LATEST database.py file!") # Debug print

    def connect(self):
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port
                )
                # Keep autocommit OFF by default for explicit transaction management in models
                self.connection.autocommit = False # Ensure this is explicitly set if you want models to control transactions

                print("Connection to the database established successfully.")
            except Exception as e:
                print(f"Error connecting to the database: {str(e)}")
                self.connection = None
                raise # Re-raise the exception to propagate connection failure
        elif self.connection.closed: # Reconnect if connection was previously closed
            self.connection = None
            self.connect() # Recursive call to reconnect

    def execute_query(self, query, params=None, fetch_all=True):
        """
        Executes a query. For SELECT statements, it fetches data.
        Manages its own cursor and potentially commits if autocommit is True.
        """
        if not self.connection or self.connection.closed:
            try:
                self.connect()
            except Exception:
                print("Failed to connect to the database for query execution.")
                return None

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                if query.strip().upper().startswith(('SELECT', 'SHOW')):
                    if fetch_all:
                        rows = cursor.fetchall()
                        colnames = [desc[0] for desc in cursor.description]
                        return [dict(zip(colnames, row)) for row in rows]
                    else:
                        row = cursor.fetchone()
                        if row:
                            colnames = [desc[0] for desc in cursor.description]
                            return dict(zip(colnames, row))
                        else:
                            return None
                else:
                    # Only commit if the connection is in autocommit mode.
                    # This prevents execute_query from committing ongoing transactions
                    # that are explicitly managed by model methods (like delete_product_by_id).
                    if self.connection.autocommit:
                        self.connection.commit()
                    return cursor.rowcount
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            # Do NOT rollback here if autocommit is False, as the calling method
            # (like delete_product_by_id) is responsible for transaction management.
            if self.connection and not self.connection.autocommit:
                pass # The caller (like model methods) handles rollback
            return None

    def execute(self, query, params=None):
        """
        Executes a non-SELECT query. Useful when the calling method needs to manage the commit/rollback.
        Raises an exception on failure.
        """
        if not self.connection or self.connection.closed:
            try:
                self.connect()
            except Exception:
                print("Failed to connect to the database for execution.")
                raise # Re-raise to propagate

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
            # No commit here; the caller (model method) is responsible for commit/rollback
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            raise # Re-raise the exception

    def fetch_one(self, query, params=None):
        """
        Fetches a single row from a SELECT query as a dictionary.
        Uses execute_query internally.
        """
        return self.execute_query(query, params, fetch_all=False)

    def fetch_all(self, query, params=None):
        """
        Fetches all rows from a SELECT query as a list of dictionaries.
        Uses execute_query internally.
        """
        return self.execute_query(query, params, fetch_all=True)

    def close_connection(self):
        """
        Closes the database connection.
        Performs a rollback if there are pending transactions.
        """
        if self.connection and not self.connection.autocommit:
            try:
                self.connection.rollback() # Rollback any pending transactions before closing
                print("Rolled back pending transaction before closing connection.")
            except Exception as e:
                print(f"Error rolling back before close: {e}")

        if self.connection:
            try:
                self.connection.close()
                self.connection = None # Set to None after closing
                print("Database connection closed.")
            except Exception as e:
                print(f"Error closing database connection: {e}")