from models.database import Database

class AccountPageModel:
    def __init__(self, database):
        """
        Initializes the AccountPageModel with a database connection.

        Args:
            database: An instance of the Database class for database operations.
        """
        self.database = database
        # Ensure the database connection is established if not already.
        # This check might be redundant if the parent controller ensures connection,
        # but it acts as a safeguard.
        if not self.database.connection:
            self.database.connect()

    def get_user_details(self, user_id):
        """
        Retrieves detailed information for a specific user from the database.

        Args:
            user_id: The unique identifier of the user whose details are to be fetched.

        Returns:
            A dictionary containing 'user_acc_id', 'user_acc_role', and 'user_acc_username'
            if the user is found, otherwise None. Returns None on database error.
        """
        query = """
            SELECT 
                user_acc_id,
                user_acc_role,
                user_acc_username
            FROM user_account
            WHERE user_acc_id = %s
        """
        try:
            # Assuming self.database.fetch_one executes the query and returns
            # the first row as a dictionary (or None if no rows).
            result = self.database.fetch_one(query, (user_id,))
            return result
        except Exception as e:
            # Print any database errors for debugging purposes.
            print(f"Database error in get_user_details for user_id {user_id}: {e}")
            return None

