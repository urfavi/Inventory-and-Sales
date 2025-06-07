from models.database import Database # Make sure this import is at the top
from PyQt5.QtWidgets import QStackedWidget, QWidget, QApplication, QMessageBox # Import QMessageBox for error handling
from gui_classes.UI_ODashboard import Ui_OWNER_DASHBOARD
from gui_classes.UI_OInventory import Ui_OWNER_INVENTORY
from gui_classes.UI_OOrders import Ui_OWNER_ORDERS
from gui_classes.UI_OSales import Ui_OWNER_SALES
from gui_classes.UI_OStockHistory import Ui_OWNER_STOCKHISTORY
from gui_classes.UI_OAccount import Ui_OWNER_ACCOUNT

from controllers.ODashboard_pagecontroller import DashboardPageController
from controllers.OInv_pageController import InventoryPageController
from controllers.OOrders_pageController import OrdersPageController
from controllers.OSales_pageController import SalesPageController
from controllers.OStk_Hstry_controller import StockHistoryPageController
from controllers.OAcc_pageController import AccountPageController
from controllers.date_time import DateTimeController
from models.OStk_Hstry_model import StockHistoryModel

class OwnerController:
    def __init__(self, main_controller, current_user_shop_id=None, current_user_id=None, current_username=None):
        self.main_controller = main_controller
        self.stack = QStackedWidget()
        self.stack.setFixedSize(1921, 1005)
        self.current_active_button = None

        self.current_user_shop_id = current_user_shop_id if current_user_shop_id is not None else 1
        self.current_user_id = current_user_id if current_user_id is not None else 1
        self.current_username = current_username if current_username is not None else "Aaron"

        print(f"DEBUG: OwnerController initialized with Shop ID: {self.current_user_shop_id}, User ID: {self.current_user_id}, Username: {self.current_username}")

        # --- IMPORTANT: Initialize Database here, BEFORE initializing other controllers ---
        self.database = None # Initialize to None first
        try:
            self.database = Database()
            self.database.connect()
            print("DEBUG: Database connection established in OwnerController.")
        except Exception as e:
            error_message = f"Failed to connect to database in OwnerController: {e}. Application may not function correctly."
            print(f"ERROR: {error_message}")
            QMessageBox.critical(None, "Database Connection Error", error_message)
            # You might want to handle this more gracefully, e.g., disable features or exit.
            # For now, we'll let it proceed, but functionality relying on DB will fail.
            # You could also raise the exception again: raise

        # Initialize DateTimeController
        self.date_time_controller = DateTimeController()

          # --- NEW/MODIFIED: Initialize StockHistoryModel and StockHistoryPageController ONCE ---
        self.stock_history_model = StockHistoryModel(self.database)

        self.stock_history_widget = QWidget() # <--- ADD THIS LINE
        self.stock_history_ui = Ui_OWNER_STOCKHISTORY() # <--- ADD THIS LINE (make sure Ui_OWNER_STOCKHISTORY is imported)
        self.stock_history_ui.setupUi(self.stock_history_widget) # <--- ADD THIS LINE

        self.OStk_Hstry_controller = StockHistoryPageController( # <--- Store it as this attribute name!
            history_ui=self.stock_history_ui,           # Your __init__ expects 'history_ui'
            history_widget=self.stock_history_widget,       # Your __init__ expects 'history_widget'
            current_user_shop_id=self.current_user_shop_id,  # Add this line # Your __init__ expects 'current_user_shop_id'
            database_connection=self.database, # Your __init__ expects 'database_connection'
            parent=self,
             # Your __init__ expects 'parent' (optional)
            # DO NOT ADD 'current_user_id=' HERE. Your StockHistoryPageController.__init__ does not accept it.
            # DO NOT ADD 'main_app=' HERE. Your StockHistoryPageController.__init__ does not accept it.
            # DO NOT ADD 'history_model=' HERE. Your StockHistoryPageController.__init__ creates its own model.
        )
        # --- END NEW/MODIFIED ---

        # Initialize all owner pages - ALL WIDGETS ARE CREATED HERE
        # Pass self.database to controllers that need it for their models
        self._init_dashboard()
        self._init_inventory() # This will now have self.database available
        self._init_orders()    # This will now have self.database available
        self._init_sales()     # This will now have self.database available
        self._init_stock_history() # This will now have self.database available
        self._init_account()   # This will now have self.database available

        # Connect date/time labels - these rely on dashboard_ui and account_ui being set
        self.date_time_controller.add_date_time_labels(
            self.dashboard_ui.dateLabel,
            self.dashboard_ui.timeLabel
        )
        self.date_time_controller.add_date_time_labels(
            self.account_ui.dateLabel,
            self.account_ui.timeLabel
        )

        # Connect navigation signals - these rely on all UI widgets and page widgets being set
        self._connect_navigation()

        # Force initial state - now that all widgets are guaranteed to exist
        self.stack.setCurrentIndex(0)
        QApplication.processEvents()
        self.set_active_button('dashboard')
        QApplication.processEvents()
        
    def show(self):
        # CONSISTENT: Now uses dashboard_widget
        self.stack.setCurrentWidget(self.dashboard_widget)
        self.set_active_button('dashboard')
        self.stack.show()  # Make the window visible

    def _init_dashboard(self):
        self.dashboard_widget = QWidget()
        self.dashboard_ui = Ui_OWNER_DASHBOARD()
        self.dashboard_ui.setupUi(self.dashboard_widget)
        self.stack.addWidget(self.dashboard_widget)
        
        # Initialize the dashboard controller
        self.dashboard_controller = DashboardPageController(
            dashboard_ui=self.dashboard_ui,
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            parent=self,
            database_connection=self.database  # Pass the database connection
        )

    def _init_inventory(self):
        # This was already correct and consistent
        self.inventory_ui = Ui_OWNER_INVENTORY()
        self.inventory_widget = QWidget()
        self.inventory_ui.setupUi(self.inventory_widget)

        self.inventory_page_controller = InventoryPageController(
            inventory_ui=self.inventory_ui,
            inventory_widget=self.inventory_widget,
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            parent=self,
            Ostk_Hstry_controller_instance=self.OStk_Hstry_controller, # Pass the instance!
            ODashboard_pagecontroller_instance=self.dashboard_controller  # THIS MUST BE SET
        )
        self.stack.addWidget(self.inventory_widget)

    def _init_orders(self):
        # CONSISTENT: orders_widget created and used correctly
        self.orders_widget = QWidget() # Corrected: used _widget
        self.orders_ui = Ui_OWNER_ORDERS()
        self.orders_ui.setupUi(self.orders_widget) # Corrected: used orders_widget
        self.stack.addWidget(self.orders_widget) # Corrected: used orders_widget (and removed duplicate)

        # Initialize orders controller
        self.orders_page_controller = OrdersPageController(
            orders_ui=self.orders_ui,
            owner_controller=self,
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
        )

    def _init_sales(self):
        # CONSISTENT: sales_widget created and used correctly
        self.sales_widget = QWidget() # Corrected: used _widget
        self.sales_ui = Ui_OWNER_SALES()
        self.sales_ui.setupUi(self.sales_widget) # Corrected: used sales_widget
        self.stack.addWidget(self.sales_widget) # Corrected: used sales_widget

        self.sales_page_controller = SalesPageController(
            sales_ui=self.sales_ui,
            sales_controller=self, # Assuming this is 'self' (the OwnerController instance)
            current_user_shop_id=self.current_user_shop_id,
            current_user_id=self.current_user_id,
            current_username=self.current_username
        )

    def _init_stock_history(self):
        # CONSISTENT: stock_history_widget created and used correctly
        #self.stock_history_widget = QWidget() # Corrected: used _widget
        # self.stock_history_ui = Ui_OWNER_STOCKHISTORY()
        # self.stock_history_ui.setupUi(self.stock_history_widget) # Corrected: used stock_history_widget
        self.stack.addWidget(self.stock_history_widget) # Corrected: used stock_history_widget

        # --- Use the already created controller instance ---
        # Assign the UI and widget to the existing controller
        # (The instance created in OwnerController.__init__ is self.OStk_Hstry_controller)
        # self.OStk_Hstry_controller.ui = self.stock_history_ui
        # self.OStk_Hstry_controller.history_widget = self.stock_history_widget # If your StockHistoryPageController uses this attribute

        # Call a method on the existing controller to set up its view, load data, etc.
        #self.OStk_Hstry_controller.setup_history_view() # Example method call

        # (Optional: If you still want a local variable name for clarity within this method)
        # self.stkhistory_controller = self.OStk_Hstry_controller

    def _init_account(self):
        # CONSISTENT: account_widget created and used correctly
        self.account_widget = QWidget() # Corrected: used _widget
        self.account_ui = Ui_OWNER_ACCOUNT()
        self.account_ui.setupUi(self.account_widget) # Corrected: used account_widget

        # Initialize account controller
        self.account_controller = AccountPageController(self.account_ui, self)

        self.stack.addWidget(self.account_widget) # Corrected: used account_widget

    def _connect_navigation(self):
        # Store all navigation buttons for easy access (this part is fine as it refers to UI elements)
        self.nav_buttons = {
            'dashboard': self.dashboard_ui.pushButton_Dashboard,
            'inventory': self.dashboard_ui.pushButton_Inventory,
            'orders': self.dashboard_ui.pushButton_Orders,
            'sales': self.dashboard_ui.pushButton_Sales,
            'stock_history': self.dashboard_ui.pushButton_Stock_History,
            'account': self.dashboard_ui.pushButton_Account
        }

        # Dashboard navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.dashboard_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.dashboard_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])
        self.dashboard_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                     self.set_active_button('orders')])
        self.dashboard_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])
        self.dashboard_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])
        self.dashboard_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                     self.set_active_button('account')])
        self.dashboard_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

        # Dashboard quick links (ALL setCurrentWidget calls now use _widget suffix)
        self.dashboard_ui.btnViewSalesReport.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])

        self.dashboard_ui.btnViewMore_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])

        # Inventory navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.inventory_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.inventory_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                     self.set_active_button('orders')])
        self.inventory_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])
        self.inventory_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])
        self.inventory_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                     self.set_active_button('account')])
        self.inventory_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

        # Inventory view history button (ALL setCurrentWidget calls now use _widget suffix)
        self.inventory_ui.pushButton_ViewHistory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])

        # Orders navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.orders_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.orders_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])
        self.orders_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])
        self.orders_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])
        self.orders_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                     self.set_active_button('account')])
        self.orders_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

        # Sales navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.sales_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.sales_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])
        self.sales_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                     self.set_active_button('orders')])
        self.sales_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])
        self.sales_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                     self.set_active_button('account')])
        self.sales_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

        # Stock History navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.stock_history_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.stock_history_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])
        self.stock_history_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                     self.set_active_button('orders')])
        self.stock_history_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])
        self.stock_history_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                     self.set_active_button('account')])
        self.stock_history_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

        # Account navigation (ALL setCurrentWidget calls now use _widget suffix)
        self.account_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                     self.set_active_button('dashboard')])
        self.account_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_widget),
                     self.set_active_button('inventory')])
        self.account_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                     self.set_active_button('orders')])
        self.account_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                     self.set_active_button('sales')])
        self.account_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_widget),
                     self.set_active_button('stock_history')])
        self.account_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])

    def set_active_button(self, button_name):
        """Set a single button as active using CSS classes"""
        # Create a dictionary of all navigation buttons on all pages (this part is fine)
        all_nav_buttons = {
            'dashboard': [
                self.dashboard_ui.pushButton_Dashboard,
                self.inventory_ui.pushButton_Dashboard,
                self.orders_ui.pushButton_Dashboard,
                self.sales_ui.pushButton_Dashboard,
                self.stock_history_ui.pushButton_Stock_History,
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
                self.orders_ui.pushButton_Sales,
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

        # Reset all navigation buttons on all pages
        for button_list in all_nav_buttons.values():
            for button in button_list:
                if hasattr(button, 'setProperty'):
                    button.setProperty('class', '')
                    button.style().unpolish(button)
                    button.style().polish(button)
                    button.update()

        # Set active class on all buttons corresponding to the active page
        active_buttons = all_nav_buttons.get(button_name, [])
        for button in active_buttons:
            if hasattr(button, 'setProperty'):
                button.setProperty('class', 'activeButton')
                button.style().unpolish(button)
                button.style().polish(button)
                button.update()

        # Store current active button name
        self.current_active_button = button_name

        # Force application to process all pending events
        QApplication.processEvents()