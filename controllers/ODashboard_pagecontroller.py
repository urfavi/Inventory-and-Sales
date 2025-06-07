from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QLabel
from PyQt5.QtCore import Qt
from models.database import Database
from models.ODashboard_pageModel import DashboardModel
import logging

class DashboardPageController:
    def __init__(self, dashboard_ui, current_user_shop_id=None, current_user_id=None,
                 current_username=None, parent=None, database_connection=None):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.ui = dashboard_ui
        self.current_user_shop_id = current_user_shop_id
        self.current_user_id = current_user_id
        self.current_username = current_username
        self.parent = parent
        if database_connection:
            self.db = database_connection
            self.logger.debug("Using provided database connection")
        elif self.parent and hasattr(self.parent, 'db'):
            self.db = self.parent.db
            self.logger.debug("Using parent's database connection")
        else:
            self.db = Database()
            try:
                self.db.connect()
                self.logger.debug("Created new database connection")
            except Exception as e:
                self.logger.error(f"Failed to connect to database: {e}")
                QMessageBox.critical(None, "Database Error",
                                     "Failed to initialize database connection")
                raise
        self.dashboard_model = DashboardModel(self.db)
        self._verify_ui_elements()
        self._initialize_ui_state()
        self.load_dashboard_widgets()

    def _verify_ui_elements(self):
        self.lowstock_product_labels = [
            getattr(self.ui, f'lowstock_product_label_{i}', None)
            for i in range(1, 5)
        ]
        self.lowstock_qty_labels = [
            getattr(self.ui, f'lowstock_qty_label_{i}', None)
            for i in range(1, 5)
        ]
        self.logger.debug("Verifying UI elements:")
        for i, (prod_label, qty_label) in enumerate(zip(self.lowstock_product_labels,
                                                        self.lowstock_qty_labels), 1):
            self.logger.debug(f"Label pair {i}: Product={prod_label is not None}, Qty={qty_label is not None}")

    def _initialize_ui_state(self):
        if hasattr(self.ui, 'label_13'):
            self.ui.label_13.setText("All items are well stocked.")
            self.ui.label_13.setStyleSheet(
                "color: white; border-radius: 15px; padding: 3px; background-color: #5cb85c;"
            )
            self.ui.label_13.setAlignment(Qt.AlignCenter)
        self._clear_low_stock_labels()
        if hasattr(self.ui, 'dashb_lowinstock_value'):
            self.ui.dashb_lowinstock_value.setText("0 items")

    def _clear_low_stock_labels(self):
        self.logger.debug("Clearing low stock labels")
        for label in self.lowstock_product_labels + self.lowstock_qty_labels:
            if label:
                label.setText("")
                label.setStyleSheet("")

    def load_dashboard_widgets(self):
        self.logger.debug("Loading dashboard widgets")
        self.load_low_stock_warning()

    def load_low_stock_warning(self):
        try:
            if not self.current_user_shop_id:
                self.logger.error("No shop_id available")
                return
            self.logger.debug(f"Loading low stock for shop {self.current_user_shop_id}")
            total_low_stock = self.dashboard_model.get_low_stock_count(
                shop_id=self.current_user_shop_id
            )
            self.logger.debug(f"Total low stock items: {total_low_stock}")
            critical_items = self.dashboard_model.get_low_stock_products(
                shop_id=self.current_user_shop_id,
                limit=4
            )
            self.logger.debug(f"Displaying {len(critical_items)} critical items")
            if hasattr(self.ui, 'dashb_lowinstock_value'):
                self.ui.dashb_lowinstock_value.setText(f"{total_low_stock} items")
                self.logger.debug(f"Updated counter to show {total_low_stock} items")
            self._clear_low_stock_labels()
            if critical_items:
                self._display_low_stock_items(critical_items)
            else:
                self._display_no_low_stock()
        except Exception as e:
            self.logger.error(f"Error loading low stock warning: {e}")
            QMessageBox.warning(
                self.ui, "Low Stock Warning Error",
                f"Failed to load low stock data: {e}")

    def _display_low_stock_items(self, low_stock_products):
        self.logger.debug("Displaying low stock items")
        if hasattr(self.ui, 'label_13'):
            self.ui.label_13.setText("Warning! These items are low of stock.")
            self.ui.label_13.setStyleSheet(
                "color: white; border-radius: 15px; padding: 3px; background-color: #c25b55;"
            )
        for i in range(4):
            if i < len(self.lowstock_product_labels) and self.lowstock_product_labels[i]:
                self.lowstock_product_labels[i].setVisible(True)
            if i < len(self.lowstock_qty_labels) and self.lowstock_qty_labels[i]:
                self.lowstock_qty_labels[i].setVisible(True)
        for i, item_dict in enumerate(low_stock_products[:4]):
            if i >= 4:
                break
            product_name = item_dict.get('product_name', 'N/A')
            current_qty = item_dict.get('prod_spec_stock_qty', 0)
            if i < len(self.lowstock_product_labels) and self.lowstock_product_labels[i]:
                self.lowstock_product_labels[i].setText(str(product_name))
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(16)
                self.lowstock_product_labels[i].setFont(font)
                palette = self.lowstock_product_labels[i].palette()
                palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#000000"))
                self.lowstock_product_labels[i].setPalette(palette)
            if i < len(self.lowstock_qty_labels) and self.lowstock_qty_labels[i]:
                self.lowstock_qty_labels[i].setText(f"ONLY {current_qty} LEFT")
                self.lowstock_qty_labels[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(16)
                self.lowstock_qty_labels[i].setFont(font)
                palette = self.lowstock_qty_labels[i].palette()
                palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#b2423c"))
                self.lowstock_qty_labels[i].setPalette(palette)
        for i in range(len(low_stock_products), 4):
            if i < len(self.lowstock_product_labels) and self.lowstock_product_labels[i]:
                self.lowstock_product_labels[i].setText("")
                self.lowstock_product_labels[i].setVisible(False)
            if i < len(self.lowstock_qty_labels) and self.lowstock_qty_labels[i]:
                self.lowstock_qty_labels[i].setText("")
                self.lowstock_qty_labels[i].setVisible(False)

    def _display_no_low_stock(self):
        self.logger.debug("Displaying no low stock message")
        if hasattr(self.ui, 'label_13'):
            self.ui.label_13.setText("All items are well stocked.")
            self.ui.label_13.setStyleSheet(
                "color: white; border-radius: 15px; padding: 3px; background-color: #5cb85c;"
            )
        if self.lowstock_product_labels and self.lowstock_product_labels[0]:
            self.lowstock_product_labels[0].setText("No products are low in stock.")
            self.lowstock_product_labels[0].setStyleSheet("font-style: italic; color: grey;")
            self.lowstock_product_labels[0].setAlignment(Qt.AlignCenter)