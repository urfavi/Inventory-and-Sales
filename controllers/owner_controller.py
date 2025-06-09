import sys
import logging
from PyQt5.QtWidgets import QStackedWidget, QWidget, QApplication, QMessageBox

# Ensure these imports are correct based on your file structure
from models.database import Database

# GUI Classes (from .ui files)
from gui_classes.UI_ODashboard import Ui_OWNER_DASHBOARD
from gui_classes.UI_OInventory import Ui_OWNER_INVENTORY
from gui_classes.UI_OOrders import Ui_OWNER_ORDERS
from gui_classes.UI_OSales import Ui_OWNER_SALES # Corrected typo: Ui_OWNER_SALES
from gui_classes.UI_OStockHistory import Ui_OWNER_STOCKHISTORY
from gui_classes.UI_OAccount import Ui_OWNER_ACCOUNT

# Controller Classes
from controllers.ODashboard_pagecontroller import DashboardPageController
from controllers.OInv_pageController import InventoryPageController
from controllers.OOrders_pageController import OrdersPageController
from controllers.OSales_pageController import SalesPageController
from controllers.OStk_Hstry_controller import StockHistoryPageController
from controllers.OAcc_pageController import AccountPageController
from controllers.date_time import DateTimeController


class OwnerController:
    def __init__(self, main_controller, current_user_shop_id=None, current_user_id=None, current_username=None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG) # Set to DEBUG for more detailed logging

        self.main_controller = main_controller
        self.stack = QStackedWidget()
        self.stack.setFixedSize(1921, 1005)
        self.current_active_button = None

        self.current_user_shop_id = current_user_shop_id if current_user_shop_id is not None else 1
        self.current_user_id = current_user_id if current_user_id is not None else 1
        self.current_username = current_username if current_username is not None else "Aaron"
        self.logger.debug(f"OwnerController initialized with Shop ID: {self.current_user_shop_id}, User ID: {self.current_user_id}, Username: {self.current_username}")

        # --- IMPORTANT: Initialize Database here, BEFORE initializing other controllers ---
        self.database = None
        try:
            self.database = Database()
            self.database.connect()
            self.logger.info("Database connection established in OwnerController.")
        except Exception as e:
            error_message = f"Failed to connect to database in OwnerController: {e}. Application may not function correctly."
            self.logger.critical(f"ERROR: {error_message}", exc_info=True)
            QMessageBox.critical(None, "Database Connection Error", error_message)
            sys.exit(1) # Exit if critical database connection fails

        # Initialize DateTimeController
        self.date_time_controller = DateTimeController()

        # --- Initialize all UI widgets and add them to the QStackedWidget first ---
        # This ensures all UI objects and their corresponding QWidget containers exist
        # before any controller tries to access them or add them to the stack.

        # Dashboard
        self.dashboard_widget = QWidget()
        self.dashboard_ui = Ui_OWNER_DASHBOARD()
        self.dashboard_ui.setupUi(self.dashboard_widget)
        self.stack.addWidget(self.dashboard_widget)

        # Inventory
        self.inventory_widget = QWidget()
        self.inventory_ui = Ui_OWNER_INVENTORY()
        self.inventory_ui.setupUi(self.inventory_widget)
        self.stack.addWidget(self.inventory_widget)

        # Orders
        self.orders_widget = QWidget()
        self.orders_ui = Ui_OWNER_ORDERS()
        self.orders_ui.setupUi(self.orders_widget)
        self.stack.addWidget(self.orders_widget)

        # Sales
        self.sales_widget = QWidget()
        self.sales_ui = Ui_OWNER_SALES()
        self.sales_ui.setupUi(self.sales_widget)
        self.stack.addWidget(self.sales_widget)

        # Stock History
        self.stock_history_widget = QWidget()
        self.stock_history_ui = Ui_OWNER_STOCKHISTORY()
        self.stock_history_ui.setupUi(self.stock_history_widget)
        self.stack.addWidget(self.stock_history_widget)

        # Account
        self.account_widget = QWidget()
        self.account_ui = Ui_OWNER_ACCOUNT()
        self.account_ui.setupUi(self.account_widget)
        self.stack.addWidget(self.account_widget)


        # --- Now initialize the controllers, passing the prepared UI objects and DB connection ---
        # Initialize StockHistoryPageController first because InventoryPageController needs it.
        self.OStk_Hstry_controller = StockHistoryPageController(
            history_ui=self.stock_history_ui,
            history_widget=self.stock_history_widget,
            current_user_shop_id=self.current_user_shop_id,
            database_connection=self.database,
            parent=self,
        )
        self.logger.debug("StockHistoryPageController initialized.")

        # Dashboard Controller (This is where the main focus is)
        self.dashboard_controller = DashboardPageController(
            dashboard_ui=self.dashboard_ui,
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            parent=self,
            database_connection=self.database
        )
        self.logger.debug("DashboardPageController initialized.")

        # Inventory Controller
        self.inventory_page_controller = InventoryPageController(
            inventory_ui=self.inventory_ui,
            inventory_widget=self.inventory_widget,
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            parent=self,
            Ostk_Hstry_controller_instance=self.OStk_Hstry_controller,
            ODashboard_pagecontroller_instance=self.dashboard_controller,
           
        )
        self.logger.debug("InventoryPageController initialized.")

        # Orders Controller
        self.orders_page_controller = OrdersPageController(
            orders_ui=self.orders_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_shop_id=self.current_user_shop_id,
            database_connection=self.database
        )
        self.logger.debug("OrdersPageController initialized.")

        # Sales Controller
        self.sales_page_controller = SalesPageController(
            sales_ui=self.sales_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_shop_id=self.current_user_shop_id,
            database_connection=self.database
        )
        self.logger.debug("SalesPageController initialized.")


        # Account Controller
        self.account_controller = AccountPageController(
            account_ui=self.account_ui,
            account_widget=self.account_widget,
            parent=self,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            database_connection=self.database
        )
        self.logger.debug("AccountPageController initialized.")

        # Connect date/time labels
        if hasattr(self.dashboard_ui, 'dateLabel') and hasattr(self.dashboard_ui, 'timeLabel'):
            self.date_time_controller.add_date_time_labels(
                self.dashboard_ui.dateLabel,
                self.dashboard_ui.timeLabel
            )
            self.logger.debug("DateTimeController added labels for Dashboard.")

        if hasattr(self.account_ui, 'dateLabel') and hasattr(self.account_ui, 'timeLabel'):
            self.date_time_controller.add_date_time_labels(
                self.account_ui.dateLabel,
                self.account_ui.timeLabel
            )
            self.logger.debug("DateTimeController added labels for Account.")

        # Connect navigation signals
        self._connect_navigation()
        self.logger.debug("Navigation signals connected.")

        # Set initial state
        self.stack.setCurrentWidget(self.dashboard_widget)
        self.set_active_button('dashboard')
        # THIS IS THE CRITICAL LINE THAT WAS MISSED IN THE PREVIOUS RUN!
        self.dashboard_controller.load_dashboard_data()
        QApplication.processEvents()


    def show(self):
        """Make the QStackedWidget visible."""
        self.stack.show()
        self.logger.info("OwnerController stack is now visible.")

    # Keeping _init_ methods as placeholders as requested, though their content is now in __init__
    def _init_dashboard(self): pass
    def _init_inventory(self): pass
    def _init_orders(self): pass
    def _init_sales(self): pass
    def _init_stock_history(self): pass
    def _init_account(self): pass


    def _connect_navigation(self):
        self.logger.debug("Connecting navigation buttons...")

        # Consolidate navigation connections using a helper method
        # This makes the code cleaner and less repetitive for each page
        self._connect_page_navigation(self.dashboard_ui)
        self._connect_page_navigation(self.inventory_ui)
        self._connect_page_navigation(self.orders_ui)
        self._connect_page_navigation(self.sales_ui)
        self._connect_page_navigation(self.stock_history_ui)
        self._connect_page_navigation(self.account_ui)

        # Specific quick links for Dashboard
        if hasattr(self.dashboard_ui, 'btnViewSalesReport'):
            self.dashboard_ui.btnViewSalesReport.clicked.connect(lambda: self.switch_page('sales'))
        if hasattr(self.dashboard_ui, 'btnViewMore_Inventory'):
            self.dashboard_ui.btnViewMore_Inventory.clicked.connect(lambda: self.switch_page('inventory'))

        # Specific button for Inventory to Stock History
        if hasattr(self.inventory_ui, 'pushButton_ViewHistory'):
            self.inventory_ui.pushButton_ViewHistory.clicked.connect(lambda: self.switch_page('stock_history'))

        self.logger.debug("All navigation buttons connected.")

    def _connect_page_navigation(self, ui_object):
        """Helper to connect common navigation buttons for a given UI object."""
        if hasattr(ui_object, 'pushButton_Dashboard'):
            ui_object.pushButton_Dashboard.clicked.connect(lambda: self.switch_page('dashboard'))
        if hasattr(ui_object, 'pushButton_Inventory'):
            ui_object.pushButton_Inventory.clicked.connect(lambda: self.switch_page('inventory'))
        if hasattr(ui_object, 'pushButton_Orders'):
            ui_object.pushButton_Orders.clicked.connect(lambda: self.switch_page('orders'))
        if hasattr(ui_object, 'pushButton_Sales'):
            ui_object.pushButton_Sales.clicked.connect(lambda: self.switch_page('sales'))
        if hasattr(ui_object, 'pushButton_Stock_History'):
            ui_object.pushButton_Stock_History.clicked.connect(lambda: self.switch_page('stock_history'))
        if hasattr(ui_object, 'pushButton_Account'):
            ui_object.pushButton_Account.clicked.connect(lambda: self.switch_page('account'))
        if hasattr(ui_object, 'pushButton_LogOut'):
            ui_object.pushButton_LogOut.clicked.connect(self.logout)


    def switch_page(self, page_name):
        """Switches to the specified page and updates active button style."""
        page_map = {
            'dashboard': self.dashboard_widget,
            'inventory': self.inventory_widget,
            'orders': self.orders_widget,
            'sales': self.sales_widget,
            'stock_history': self.stock_history_widget,
            'account': self.account_widget
        }
        target_widget = page_map.get(page_name)

        if target_widget:
            current_index = self.stack.indexOf(target_widget)
            if self.stack.currentIndex() != current_index:
                self.stack.setCurrentWidget(target_widget)
                self.set_active_button(page_name)
                self.logger.info(f"Switched to page: {page_name}")
                # Trigger data reload for the switched page if necessary
                self._reload_page_data(page_name)
        else:
            self.logger.warning(f"Attempted to switch to unknown page: {page_name}")

    def _reload_page_data(self, page_name):
        """Triggers data loading for the currently displayed page."""
        self.logger.debug(f"Attempting to reload data for {page_name}...")
        if page_name == 'dashboard':
            if hasattr(self, 'dashboard_controller'):
                self.dashboard_controller.load_dashboard_data()
            else:
                self.logger.warning("Dashboard controller not initialized, cannot reload data.")
        elif page_name == 'inventory':
            if hasattr(self, 'inventory_page_controller'):
                # The correct way to reload inventory is to call its dedicated method.
                # This method already knows which table to load and what data to fetch.
                self.inventory_page_controller.load_all_inventory_products() # <--- REVERT TO THIS!
                self.logger.debug("Inventory data reload triggered via inventory_page_controller.load_all_inventory_products().")
            else:
                self.logger.warning("Inventory controller not initialized, cannot reload data.")
        elif page_name == 'orders':
            if hasattr(self, 'orders_page_controller'):
                self.orders_page_controller.load_order_history()
            else:
                self.logger.warning("Orders controller not initialized, cannot reload data.")
        elif page_name == 'sales':
            if hasattr(self, 'sales_page_controller'):
                self.sales_page_controller.load_sales_data()
            else:
                self.logger.warning("Sales controller not initialized, cannot reload data.")
        elif page_name == 'stock_history':
            if hasattr(self, 'OStk_Hstry_controller'):
                self.OStk_Hstry_controller.load_stock_history()
            else:
                self.logger.warning("Stock History controller not initialized, cannot reload data.")
        elif page_name == 'account':
            if hasattr(self, 'account_controller'):
                self.account_controller.view_owner_account() # <--- CHANGE THIS LINE!
            else:
                self.logger.warning("Account controller not initialized, cannot reload data.")
        self.logger.debug(f"Triggered data reload for {page_name}.")


    def set_active_button(self, button_name):
        """Set a single button as active using CSS classes across all navigation menus."""
        # ... (rest of this method remains the same)
        self.logger.debug(f"Setting active button to: {button_name}")

        # Create a dictionary of all navigation buttons on all pages
        all_nav_buttons = {
            'dashboard': [
                self.dashboard_ui.pushButton_Dashboard,
                self.inventory_ui.pushButton_Dashboard,
                self.orders_ui.pushButton_Dashboard,
                self.sales_ui.pushButton_Dashboard,
                self.stock_history_ui.pushButton_Dashboard,
                self.account_ui.pushButton_Dashboard
            ],
            'inventory': [
                self.dashboard_ui.pushButton_Inventory,
                self.inventory_ui.pushButton_Inventory,
                self.orders_ui.pushButton_Inventory,
                self.sales_ui.pushButton_Inventory,
                self.stock_history_ui.pushButton_Inventory,
                self.account_ui.pushButton_Inventory
            ],
            'orders': [
                self.dashboard_ui.pushButton_Orders,
                self.inventory_ui.pushButton_Orders,
                self.orders_ui.pushButton_Orders,
                self.sales_ui.pushButton_Orders,
                self.stock_history_ui.pushButton_Orders,
                self.account_ui.pushButton_Orders
            ],
            'sales': [
                self.dashboard_ui.pushButton_Sales,
                self.inventory_ui.pushButton_Sales,
                self.orders_ui.pushButton_Sales, # Corrected this from pushButton_Orders
                self.sales_ui.pushButton_Sales,
                self.stock_history_ui.pushButton_Sales,
                self.account_ui.pushButton_Sales
            ],
            'stock_history': [
                self.dashboard_ui.pushButton_Stock_History,
                self.inventory_ui.pushButton_Stock_History,
                self.orders_ui.pushButton_Stock_History,
                self.sales_ui.pushButton_Stock_History,
                self.stock_history_ui.pushButton_Stock_History,
                self.account_ui.pushButton_Stock_History
            ],
            'account': [
                self.dashboard_ui.pushButton_Account,
                self.inventory_ui.pushButton_Account,
                self.orders_ui.pushButton_Account,
                self.sales_ui.pushButton_Account,
                self.stock_history_ui.pushButton_Account,
                self.account_ui.pushButton_Account
            ]
        }

        # Define styles
        active_style = "QPushButton { background-color:#c25b55; color:black; font-weight: 700; border-radius: 25px; padding: 9px; text-align: left; }"
        default_style = "QPushButton { background-color: white; color: black; border-radius: 25px; padding: 9px; text-align: left; }"

        # Reset all navigation buttons on all pages
        for key, button_list in all_nav_buttons.items():
            for button in button_list:
                if button is not None:
                    button.setStyleSheet(default_style)
                    if hasattr(button, 'setProperty'): # Used for CSS styling via QSS
                        button.setProperty('class', '')
                        button.style().unpolish(button)
                        button.style().polish(button)
                    button.update()

        # Set active style on all buttons corresponding to the active page
        active_buttons = all_nav_buttons.get(button_name, [])
        for button in active_buttons:
            if button is not None:
                button.setStyleSheet(active_style)
                if hasattr(button, 'setProperty'):
                    button.setProperty('class', 'activeButton')
                    button.style().unpolish(button)
                    button.style().polish(button)
                button.update()

        self.current_active_button = button_name
        QApplication.processEvents()

    def logout(self):
        """Handle logout functionality."""
        self.logger.info("Logout button clicked.")
        reply = QMessageBox.question(self.stack, 'Logout', 'Are you sure you want to log out?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.logger.info("User confirmed logout. Closing database connection.")
            if self.database:
                self.database.disconnect()
            self.stack.hide()
            # Ensure main_controller has a logout method and it correctly handles
            # returning to the login page or closing the application.
            self.main_controller.logout()
        else:
            self.logger.info("Logout cancelled by user.")

# (Optional) Example MainApp for local testing, remove if you have a top-level app.py
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    from PyQt5 import QtWidgets

    class MainApp(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Owner Dashboard Application")
            self.setGeometry(100, 100, 1921, 1005) # Match QStackedWidget size

            # Initialize OwnerController, passing self as main_controller
            self.owner_controller = OwnerController(main_controller=self, current_user_shop_id=1, current_user_id=1, current_username="TestOwner")
            self.setCentralWidget(self.owner_controller.stack)
            self.owner_controller.show() # Make the stacked widget visible

        def logout(self):
            """Placeholder for the main application's logout logic."""
            print("MainApp: Logging out and returning to login/closing application.")
            QMessageBox.information(self, "Logged Out", "You have been logged out.")
            self.close() # Close the main window


    app = QApplication(sys.argv)
    main_window = MainApp()
    sys.exit(app.exec_())