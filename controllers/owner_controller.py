from models.database import Database
from PyQt5.QtWidgets import QStackedWidget, QWidget, QApplication
from gui_classes.UI_ODashboard import Ui_OWNER_DASHBOARD
from gui_classes.UI_OInventory import Ui_OWNER_INVENTORY
from gui_classes.UI_OOrders import Ui_OWNER_ORDERS
from gui_classes.UI_OSales import Ui_OWNER_SALES
from gui_classes.UI_OStockHistory import Ui_OWNER_STOCKHISTORY
from gui_classes.UI_OAccount import Ui_OWNER_ACCOUNT

from controllers.OInv_pageController import InventoryPageController
from controllers.OOrders_pageController import OrdersPageController
from controllers.OSales_pageController import SalesPageController
from controllers.OStk_Hstry_controller import StockHistoryPageController
from controllers.OAcc_pageController import AccountPageController
from controllers.date_time import DateTimeController

class OwnerController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.stack = QStackedWidget()
        self.stack.setFixedSize(1921, 1005)
        self.current_active_button = None
        
        # Initialize DateTimeController
        self.date_time_controller = DateTimeController()
        
        # Initialize all owner pages
        self._init_dashboard()
        self._init_inventory()
        self._init_orders()
        self._init_sales()
        self._init_stock_history()
        self._init_account()
        
        # Connect date/time labels
        self.date_time_controller.add_date_time_labels(
            self.dashboard_ui.dateLabel,
            self.dashboard_ui.timeLabel
        )
        self.date_time_controller.add_date_time_labels(
            self.account_ui.dateLabel,
            self.account_ui.timeLabel
        )
        
        # Connect navigation signals
        self._connect_navigation()
        
        # Force initial state
        self.stack.setCurrentIndex(0)
        QApplication.processEvents()
        self.set_active_button('dashboard')
        QApplication.processEvents()

    def show(self):
        self.stack.setCurrentWidget(self.dashboard_page)
        self.set_active_button('dashboard') 
        self.stack.show()  # Make the window visible
    
    def _init_dashboard(self):
        self.dashboard_page = QWidget()
        self.dashboard_ui = Ui_OWNER_DASHBOARD()
        self.dashboard_ui.setupUi(self.dashboard_page)
        self.stack.addWidget(self.dashboard_page)
    
    def _init_inventory(self):
        self.inventory_page = QWidget()
        self.inventory_ui = Ui_OWNER_INVENTORY()
        self.inventory_ui.setupUi(self.inventory_page)
        self.stack.addWidget(self.inventory_page)
        
        # Initialize inventory controller
        self.inventory_controller = InventoryPageController(self.inventory_ui)
    
    def _init_orders(self):
        self.orders_page = QWidget()
        self.orders_ui = Ui_OWNER_ORDERS()
        self.orders_ui.setupUi(self.orders_page)
        self.stack.addWidget(self.orders_page)
        
        # Initialize orders controller
        self.orders_controller = OrdersPageController(self.orders_ui, self)
    
    def _init_sales(self):
        self.sales_page = QWidget()
        self.sales_ui = Ui_OWNER_SALES()
        self.sales_ui.setupUi(self.sales_page)
        self.stack.addWidget(self.sales_page)
        
        # Initialize sales controller
        self.sales_controller = SalesPageController(self.sales_ui, self)
    
    def _init_stock_history(self):
        self.stock_history_page = QWidget()
        self.stock_history_ui = Ui_OWNER_STOCKHISTORY()
        self.stock_history_ui.setupUi(self.stock_history_page)
        self.stack.addWidget(self.stock_history_page)
    
        # Initialize stock history controller
        self.stkhistory_controller = StockHistoryPageController(self.stock_history_ui, self)
    
    def _init_account(self):
        self.account_page = QWidget()
        self.account_ui = Ui_OWNER_ACCOUNT()
        self.account_ui.setupUi(self.account_page)
        
        # Initialize account controller
        self.account_controller = AccountPageController(self.account_ui, self)
        
        self.stack.addWidget(self.account_page)
    
    def _connect_navigation(self):
        # Store all navigation buttons for easy access
        self.nav_buttons = {
            'dashboard': self.dashboard_ui.pushButton_Dashboard,
            'inventory': self.dashboard_ui.pushButton_Inventory,
            'orders': self.dashboard_ui.pushButton_Orders,
            'sales': self.dashboard_ui.pushButton_Sales,
            'stock_history': self.dashboard_ui.pushButton_Stock_History,
            'account': self.dashboard_ui.pushButton_Account
        }
        
        # Dashboard navigation
        self.dashboard_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.dashboard_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page), 
                    self.set_active_button('inventory')])
        self.dashboard_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_page), 
                    self.set_active_button('orders')])
        self.dashboard_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page), 
                    self.set_active_button('sales')])
        self.dashboard_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page), 
                    self.set_active_button('stock_history')])
        self.dashboard_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_page), 
                    self.set_active_button('account')])
        self.dashboard_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
        
        # Dashboard quick links
        self.dashboard_ui.btnViewSalesReport.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page),
                    self.set_active_button('sales')])
        
        self.dashboard_ui.btnViewMore_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page),
                    self.set_active_button('inventory')])
        
        # Inventory navigation
        self.inventory_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.inventory_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_page), 
                    self.set_active_button('orders')])
        self.inventory_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page), 
                    self.set_active_button('sales')])
        self.inventory_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page), 
                    self.set_active_button('stock_history')])
        self.inventory_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_page), 
                    self.set_active_button('account')])
        self.inventory_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
        
        # Inventory view history button
        self.inventory_ui.pushButton_ViewHistory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page),
                    self.set_active_button('stock_history')])
        
        # Orders navigation
        self.orders_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.orders_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page), 
                    self.set_active_button('inventory')])
        self.orders_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page), 
                    self.set_active_button('sales')])
        self.orders_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page), 
                    self.set_active_button('stock_history')])
        self.orders_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_page), 
                    self.set_active_button('account')])
        self.orders_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
        
        # Sales navigation
        self.sales_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.sales_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page), 
                    self.set_active_button('inventory')])
        self.sales_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_page), 
                    self.set_active_button('orders')])
        self.sales_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page), 
                    self.set_active_button('stock_history')])
        self.sales_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_page), 
                    self.set_active_button('account')])
        self.sales_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
        
        # Stock History navigation
        self.stock_history_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.stock_history_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page), 
                    self.set_active_button('inventory')])
        self.stock_history_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_page), 
                    self.set_active_button('orders')])
        self.stock_history_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page), 
                    self.set_active_button('sales')])
        self.stock_history_ui.pushButton_Account.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.account_page), 
                    self.set_active_button('account')])
        self.stock_history_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
        
        # Account navigation
        self.account_ui.pushButton_Dashboard.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.dashboard_page), 
                    self.set_active_button('dashboard')])
        self.account_ui.pushButton_Inventory.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.inventory_page), 
                    self.set_active_button('inventory')])
        self.account_ui.pushButton_Orders.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.orders_page), 
                    self.set_active_button('orders')])
        self.account_ui.pushButton_Sales.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.sales_page), 
                    self.set_active_button('sales')])
        self.account_ui.pushButton_Stock_History.clicked.connect(
            lambda: [self.stack.setCurrentWidget(self.stock_history_page), 
                    self.set_active_button('stock_history')])
        self.account_ui.pushButton_LogOut.clicked.connect(lambda: [
            self.stack.hide(),
            self.main_controller.logout()
        ])
    
    def set_active_button(self, button_name):
        """Set a single button as active using CSS classes"""
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
                if hasattr(button, 'setProperty'):  # Check if button exists
                    button.setProperty('class', '')  # Clear active class
                    button.style().unpolish(button)
                    button.style().polish(button)
                    button.update()
        
        # Set active class on all buttons corresponding to the active page
        active_buttons = all_nav_buttons.get(button_name, [])
        for button in active_buttons:
            if hasattr(button, 'setProperty'):  # Check if button exists
                button.setProperty('class', 'activeButton')
                button.style().unpolish(button)
                button.style().polish(button)
                button.update()
        
        # Store current active button name
        self.current_active_button = button_name
        
        # Force application to process all pending events
        QApplication.processEvents()

    