from PyQt5.QtWidgets import QStackedWidget, QWidget, QMessageBox
from gui_classes.UI_CDashboard import Ui_CASHIER_DASHBOARD
from gui_classes.UI_COrders import Ui_CASHIER_ORDERS 
from gui_classes.UI_COrder_History import Ui_CASHIER_ORDER_HISTORY
from gui_classes.UI_CSales import Ui_CASHIER_SALES
from gui_classes.UI_CAccount import Ui_CASHIER_ACCOUNT 

from controllers.CDashboard_pageController import DashboardPageController
from controllers.COrders_pageController import OrdersPageController
from controllers.COrderHistory_pageController import OrderHistoryPageController
from controllers.CSales_pageController import SalesPageController
from controllers.date_time import DateTimeController

class CashierController:
    def __init__(self, main_controller, database, user_id, username=None, shop_id=None):
        self.main_controller = main_controller
        self.current_user_id = user_id
        self.current_username = username if username is not None else "Cashier"
        self.current_user_shop_id = shop_id if shop_id is not None else 1
        
        try:
            self.database = database
            # Remove the is_connected check and just try to use the database
            print(f"DEBUG: CashierController initialized for {self.current_username}")
            
            # Test the connection by making a simple query
            test_query = "SELECT 1"
            self.database.fetch_one(test_query)
            print("DEBUG: Database connection test successful")
        except Exception as e:
            error_msg = f"Database connection failed: {str(e)}"
            print(f"ERROR: {error_msg}")
            QMessageBox.critical(None, "Database Error", error_msg)
            raise

        self.stack = QStackedWidget()
        self.stack.setFixedSize(1921, 1005)
        
        self.date_time_controller = DateTimeController()
        
        # Initialize all pages
        self._init_dashboard()
        self._init_orders()
        self._init_order_history()
        self._init_sales()
        self._init_account()
        
        # Setup date/time labels
        self._setup_datetime_labels()
        
        # Connect navigation and set initial state
        self._connect_navigation()
        self.stack.setCurrentIndex(0)
        self.set_active_button('dashboard')
        
    def _setup_datetime_labels(self):
        """Centralized setup for date/time labels"""
        self.date_time_controller.add_date_time_labels(
            self.dashboard_ui.dateLabel,
            self.dashboard_ui.timeLabel
        )
        self.date_time_controller.add_date_time_labels(
            self.account_ui.dateLabel,
            self.account_ui.timeLabel
        )
    
    def _init_dashboard(self):
        self.dashboard_widget = QWidget()
        self.dashboard_ui = Ui_CASHIER_DASHBOARD()
        self.dashboard_ui.setupUi(self.dashboard_widget)
        self.stack.addWidget(self.dashboard_widget)
        
        self.dashboard_controller = DashboardPageController(
            dashboard_ui=self.dashboard_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_username=self.current_username,
            current_shop_id=self.current_user_shop_id
        )
    
    def _init_orders(self):
        self.orders_widget = QWidget()
        self.orders_ui = Ui_CASHIER_ORDERS()
        self.orders_ui.setupUi(self.orders_widget)
        self.stack.addWidget(self.orders_widget)
        
        self.orders_controller = OrdersPageController(
            orders_ui=self.orders_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_shop_id=self.current_user_shop_id
        )
    
    def _init_order_history(self):
        self.order_history_widget = QWidget()
        self.order_history_ui = Ui_CASHIER_ORDER_HISTORY()
        self.order_history_ui.setupUi(self.order_history_widget)
        self.stack.addWidget(self.order_history_widget)
        
        self.orderHistory_controller = OrderHistoryPageController(
            history_ui=self.order_history_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_shop_id=self.current_user_shop_id
        )
    
    def _init_sales(self):
        self.sales_widget = QWidget()
        self.sales_ui = Ui_CASHIER_SALES()
        self.sales_ui.setupUi(self.sales_widget)
        self.stack.addWidget(self.sales_widget)
        
        self.sales_controller = SalesPageController(
            sales_ui=self.sales_ui,
            parent_controller=self,
            current_user_id=self.current_user_id,
            current_shop_id=self.current_user_shop_id
        )
    
    def _init_account(self):
        self.account_widget = QWidget()
        self.account_ui = Ui_CASHIER_ACCOUNT()
        self.account_ui.setupUi(self.account_widget)
        self.stack.addWidget(self.account_widget)
        
    def _connect_navigation(self):
        """Connect all navigation buttons consistently"""
        # Dashboard navigation
        self.dashboard_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                    self.set_active_button('dashboard')])
        self.dashboard_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                    self.set_active_button('orders')])
        self.dashboard_ui.pushButton_Order_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.order_history_widget),
                    self.set_active_button('order_history')])
        self.dashboard_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                    self.set_active_button('sales')])
        self.dashboard_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                    self.set_active_button('account')])
        self.dashboard_ui.pushButton_LogOut.clicked.connect(self.handle_logout)
        
        # Dashboard quick links
        self.dashboard_ui.btnViewSalesReport.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                    self.set_active_button('sales')])
        self.dashboard_ui.btnProcess_Order.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                    self.set_active_button('orders')])
        
        # Orders navigation
        self.orders_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                    self.set_active_button('dashboard')])
        self.orders_ui.pushButton_Order_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.order_history_widget),
                    self.set_active_button('order_history')])
        self.orders_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                    self.set_active_button('sales')])
        self.orders_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                    self.set_active_button('account')])
        self.orders_ui.pushButton_LogOut.clicked.connect(self.handle_logout)
        
        # Order History navigation
        self.order_history_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                    self.set_active_button('dashboard')])
        self.order_history_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                    self.set_active_button('orders')])
        self.order_history_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                    self.set_active_button('sales')])
        self.order_history_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                    self.set_active_button('account')])
        self.order_history_ui.pushButton_LogOut.clicked.connect(self.handle_logout)

        # Sales navigation
        self.sales_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                    self.set_active_button('dashboard')])
        self.sales_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                    self.set_active_button('orders')])
        self.sales_ui.pushButton_Order_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.order_history_widget),
                    self.set_active_button('order_history')])
        self.sales_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_widget),
                    self.set_active_button('account')])
        self.sales_ui.pushButton_LogOut.clicked.connect(self.handle_logout)

        # Account navigation
        self.account_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_widget),
                    self.set_active_button('dashboard')])
        self.account_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_widget),
                    self.set_active_button('orders')])
        self.account_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_widget),
                    self.set_active_button('sales')])
        self.account_ui.pushButton_Order_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.order_history_widget),
                    self.set_active_button('order_history')])
        self.account_ui.pushButton_LogOut.clicked.connect(self.handle_logout)
    
    def handle_logout(self):
        """Centralized logout handling"""
        self.stack.hide()
        self.main_controller.logout()
    
    def set_active_button(self, button_name):
        """Set active navigation button state consistently"""
        all_nav_buttons = {
            'dashboard': [
                self.dashboard_ui.pushButton_Dashboard,
                self.orders_ui.pushButton_Dashboard,
                self.order_history_ui.pushButton_Dashboard,
                self.sales_ui.pushButton_Dashboard,
                self.account_ui.pushButton_Dashboard
            ],
            'orders': [
                self.dashboard_ui.pushButton_Orders,
                self.orders_ui.pushButton_Orders,
                self.order_history_ui.pushButton_Orders,
                self.sales_ui.pushButton_Orders,
                self.account_ui.pushButton_Orders
            ],
            'order_history': [
                self.dashboard_ui.pushButton_Order_History,
                self.orders_ui.pushButton_Order_History,
                self.order_history_ui.pushButton_Order_History,
                self.sales_ui.pushButton_Order_History,
                self.account_ui.pushButton_Order_History
            ],
            'sales': [
                self.dashboard_ui.pushButton_Sales,
                self.orders_ui.pushButton_Sales,
                self.order_history_ui.pushButton_Sales,
                self.sales_ui.pushButton_Sales,
                self.account_ui.pushButton_Sales
            ],
            'account': [
                self.dashboard_ui.pushButton_Account,
                self.orders_ui.pushButton_Account,
                self.order_history_ui.pushButton_Account,
                self.sales_ui.pushButton_Account,
                self.account_ui.pushButton_Account
            ]
        }
        
        # Reset all buttons
        for button_list in all_nav_buttons.values():
            for button in button_list:
                button.setProperty('class', '')
                button.style().unpolish(button)
                button.style().polish(button)
        
        # Set active state for current button
        active_buttons = all_nav_buttons.get(button_name, [])
        for button in active_buttons:
            button.setProperty('class', 'activeButton')
            button.style().unpolish(button)
            button.style().polish(button)
    
    def show(self):
        """Show the cashier interface"""
        self.stack.setCurrentWidget(self.dashboard_widget)
        self.set_active_button('dashboard')
        self.stack.show()