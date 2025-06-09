from PyQt5.QtWidgets import QMessageBox
from models.CAcc_pageModel import AccountPageModel 

class AccountPageController:
    def __init__(self, account_ui, parent_controller=None, current_user_id=None, 
                 current_username=None, current_shop_id=None):
        """
        Initializes the AccountPageController.

        This controller manages the interactions and data display for the
        cashier's account page. It fetches user details and populates
        the corresponding UI elements.

        Args:
            account_ui: The UI object for the account page (e.g., Ui_CASHIER_ACCOUNT).
            parent_controller: The main controller (e.g., CashierController) that
                               instantiated this controller. Used to access shared
                               resources like the database connection.
            current_user_id: The ID of the currently logged-in user.
            current_username: The username of the currently logged-in user.
            current_shop_id: The ID of the current shop.
        """
        self.ui = account_ui
        self.parent_controller = parent_controller
        
        # Safely get database and user info, preferring parent_controller for consistency.
        if parent_controller is not None:
            self.database = parent_controller.database
            # These can be redundant if passed explicitly, but ensure consistency.
            self.current_user_id = parent_controller.current_user_id
            self.current_username = parent_controller.current_username
            self.current_shop_id = parent_controller.current_user_shop_id
        else:
            # Fallback if parent_controller is not provided (should ideally not happen
            # with current system architecture but good for robustness).
            self.database = None 
            self.current_user_id = current_user_id
            self.current_username = current_username
            self.current_shop_id = current_shop_id

        # Crucial check: ensure database is available before proceeding.
        if not self.database:
            QMessageBox.critical(None, "Initialization Error", 
                                 "Database connection not provided to AccountPageController.")
            return

        # Initialize the model responsible for database interactions.
        self.model = AccountPageModel(self.database)
        
        # Load user information into the UI immediately upon controller initialization.
        self.load_user_info()

    def load_user_info(self):
        """
        Fetches the current user's information from the model and updates
        the corresponding QLabel elements in the UI.
        
        It sets the text for cashierID, cashierRole, and cashierName based
        on the retrieved data.
        """
        if not self.current_user_id:
            # If user ID is not available, set default N/A values.
            print("Current user ID is not set. Cannot load account information.")
            self.ui.cashierID.setText("N/A")
            self.ui.cashierRole.setText("N/A")
            self.ui.cashierName.setText("N/A")
            return

        # Attempt to retrieve user details from the model.
        user_info = self.model.get_user_details(self.current_user_id)

        if user_info:
            # If user details are successfully fetched, populate the UI labels.
            # Using .get() with a default 'N/A' to prevent KeyError if a column is missing.
            self.ui.cashierID.setText(str(user_info.get('user_acc_id', 'N/A')))
            self.ui.cashierRole.setText(user_info.get('user_acc_role', 'N/A'))
            self.ui.cashierName.setText(user_info.get('user_acc_username', 'N/A'))
        else:
            # If no user info is found or an error occurred during fetch,
            # display an error message and set error states in UI.
            QMessageBox.warning(None, "Account Info Error", "Could not load user account details.")
            self.ui.cashierID.setText("Error")
            self.ui.cashierRole.setText("Error")
            self.ui.cashierName.setText("Error")

