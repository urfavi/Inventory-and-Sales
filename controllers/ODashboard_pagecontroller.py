from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QLabel, QVBoxLayout, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
from models.database import Database
from models.ODashboard_pageModel import DashboardModel # Assuming ODashboard_pageModel is DashboardModel
import logging
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np # For potential use in chart data generation if needed


class DashboardPageController:
    def __init__(self, dashboard_ui, current_user_shop_id, current_user_id, current_username, parent, database_connection):
        self.dashboard_ui = dashboard_ui
        self.current_user_shop_id = current_user_shop_id
        self.current_user_id = current_user_id
        self.current_username = current_username
        self.parent = parent
        self.database = database_connection # This is your Database connection instance

        # Initialize logger for this controller FIRST, as other methods might use it
        self.logger = logging.getLogger(__name__)
        self.logger.debug("DashboardPageController initializing...")

        # Initialize the model, passing the database connection
        self.dashboard_model = DashboardModel(self.database)

        # Connect UI elements (e.g., if there are refresh buttons, etc.)
        # Example: self.dashboard_ui.refreshButton.clicked.connect(self.load_dashboard_data)

        # Set initial labels that don't depend on data
        if hasattr(self.dashboard_ui, 'label_ShopName'):
            self.dashboard_ui.label_ShopName.setText("Shop ID: " + str(self.current_user_shop_id))
        if hasattr(self.dashboard_ui, 'label_Username'):
            self.dashboard_ui.label_Username.setText("Owner: " + self.current_username)

        # Initialize low stock labels lists for dynamic updates
        self.lowstock_product_labels = [
            getattr(self.dashboard_ui, f'lowstock_product_label_{i}', None) for i in range(1, 5)
        ]
        self.lowstock_qty_labels = [
            getattr(self.dashboard_ui, f'lowstock_qty_label_{i}', None) for i in range(1, 5)
        ]

        # Load all dashboard data including the chart and low stock info
        self.load_dashboard_data()
        self.logger.debug("DashboardPageController initialized and data loaded.")

    def load_dashboard_data(self):
        """
        A central method to load/refresh all data displayed on the dashboard.
        This should be called from __init__ and whenever data needs to be refreshed.
        """
        self.logger.info("Loading dashboard data...")

        # Populate Today's Sales
        today_sales_value = self.dashboard_model.get_today_sales(self.current_user_shop_id)
        if hasattr(self.dashboard_ui, 'value_Tod_sales'):
            self.dashboard_ui.value_Tod_sales.setText(f"₱{today_sales_value:,.2f}")
            self.logger.debug(f"Today's Sales: ₱{today_sales_value:,.2f}")

        # Populate Today's Orders
        today_orders_count = self.dashboard_model.get_today_orders(self.current_user_shop_id)
        if hasattr(self.dashboard_ui, 'value_Tod_orders'):
            self.dashboard_ui.value_Tod_orders.setText(str(today_orders_count))
            self.logger.debug(f"Today's Orders: {today_orders_count}")

        # Populate Best Sellers Chart
        self.add_best_sellers_chart() # This method will now be called after logger init

        # 5. Get Low Stock Items (using existing methods, ensure model has get_low_stock_products)
        try:
            # Note: The model needs a get_low_stock_products method if you're calling it directly here.
            # Your DashboardModel only has get_low_stock_count. Let's assume you'll add get_low_stock_products
            # to the model, or adjust this to use get_low_stock_count if that's what's intended for the table.
            # For now, let's keep the call consistent with your original intent, assuming model supports it.
            low_stock_items = self.dashboard_model.get_low_stock_products(self.current_user_shop_id) # This method must exist in DashboardModel
            self._populate_low_stock_table(low_stock_items) # This method was not provided, creating a placeholder
            print(f"DEBUG: Low Stock Items: {low_stock_items}")
        except AttributeError:
             print(f"ERROR: DashboardModel does not have 'get_low_stock_products' method. Please add it to your DashboardModel.")
             self._populate_low_stock_table([]) # Clear table on error
        except Exception as e:
            print(f"ERROR: Failed to load low stock items: {e}")
            self._populate_low_stock_table([]) # Clear table on error

        # 6. Load Low Stock Warning (using existing method which seems to handle the count and the 4 critical items)
        self.load_low_stock_warning()


    def add_best_sellers_chart(self):
        """Add best sellers chart to the dashboard"""
        self.logger.debug("Attempting to add best sellers chart.")

        # Clear existing widgets from the frame's layout
        layout = self.dashboard_ui.frameBestSellersChart.layout()
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        else:
            layout = QtWidgets.QVBoxLayout(self.dashboard_ui.frameBestSellersChart)
            self.dashboard_ui.frameBestSellersChart.setLayout(layout)

        # Adjust frame size (you had this, keep it here or set in Qt Designer)
        # self.dashboard_ui.frameBestSellersChart.setGeometry(QtCore.QRect(20, 80, 891, 555))
        # It's better to let Qt Designer handle the geometry if possible,
        # or ensure this size fits your design.

        # Create matplotlib figure
        fig = Figure(figsize=(6.5, 4.3), dpi=100, facecolor='none')
        ax = fig.add_subplot(111)

        # Make the plot area (axes) transparent
        ax.set_facecolor('none')

        # Get best sellers data
        # Ensure model.get_best_sellers expects shop_id
        best_sellers = self.dashboard_model.get_best_sellers(self.current_user_shop_id)
        self.logger.debug(f"DEBUG Chart Data: {best_sellers}")

        if best_sellers:
            # Ensure the keys match your model's return format
            items = [row['product_name'] for row in best_sellers]
            sales = [row['total_quantity'] for row in best_sellers]

            # Create bar chart
            bars = ax.bar(items, sales, color='#003366', width=0.6)

            # Customize chart
            ax.set_ylabel('Quantity Sold', fontsize=10)
            ax.tick_params(axis='x', labelsize=8, rotation=45)

            # Add value labels on bars
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                                f'{int(height)}',
                                ha='center', va='bottom', fontsize=8)
        else:
            ax.text(0.5, 0.5, "No best sellers data available.",
                            horizontalalignment='center', verticalalignment='center',
                            transform=ax.transAxes, fontsize=12, color='gray')

        fig.tight_layout()

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

        canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Expanding
        )
        self.logger.debug("Best sellers chart added successfully.")

    def _populate_low_stock_table(self, data):
        # This function was not provided in your original snippet, but implied by your call.
        # If you have a separate QTableWidget for low stock items, this is where you'd populate it.
        # If the low stock is only handled by the labels in load_low_stock_warning, then this can be a placeholder.
        print(f"DEBUG: _populate_low_stock_table called with {len(data)} items.")
        if not hasattr(self.dashboard_ui, 'tableWidget_LowStock'): # Assuming a table for low stock
            print("WARNING: tableWidget_LowStock not found in UI. Low stock table not populated.")
            return

        self.dashboard_ui.tableWidget_LowStock.setRowCount(0)
        if not data:
            print("INFO: No low stock table data to display.")
            return

        self.dashboard_ui.tableWidget_LowStock.setRowCount(len(data))
        for row_idx, item in enumerate(data):
            # Assuming 'item' is like {'product_name': '...', 'prod_spec_stock_qty': N}
            if isinstance(item, dict):
                product_name = item.get('product_name', 'N/A')
                quantity = item.get('prod_spec_stock_qty', 0)
            elif isinstance(item, (list, tuple)) and len(item) >= 2: # Assuming at least name and quantity
                product_name = item[0]
                quantity = item[1]
            else:
                product_name = 'N/A'
                quantity = 0
                print(f"WARNING: Unexpected data format for low stock item: {item}")

            self.dashboard_ui.tableWidget_LowStock.setItem(row_idx, 0, QTableWidgetItem(product_name))
            self.dashboard_ui.tableWidget_LowStock.setItem(row_idx, 1, QTableWidgetItem(str(quantity)))
        self.dashboard_ui.tableWidget_LowStock.resizeColumnsToContents()


    # Existing low stock warning methods (no change needed here, just kept for completeness)
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
            # Ensure DashboardModel has get_low_stock_products
            critical_items = self.dashboard_model.get_low_stock_products( # This method must exist in DashboardModel
                shop_id=self.current_user_shop_id,
                limit=4
            )
            self.logger.debug(f"Displaying {len(critical_items)} critical items")
            # CORRECTED: Use self.dashboard_ui instead of self.ui for the UI object
            if hasattr(self.dashboard_ui, 'dashb_lowinstock_value'):
                self.dashboard_ui.dashb_lowinstock_value.setText(f"{total_low_stock} items")
                self.logger.debug(f"Updated counter to show {total_low_stock} items")

            # CORRECTED: Use self.dashboard_ui for label_13 and ensure lowstock_product_labels/qty_labels are handled correctly
            self._clear_low_stock_labels() # Make sure this method clears the *actual* labels on the UI
            if critical_items:
                self._display_low_stock_items(critical_items)
            else:
                self._display_no_low_stock()
        except AttributeError:
            self.logger.error(f"DashboardModel does not have 'get_low_stock_products' method. Please add it to your DashboardModel.")
            # Fallback for UI if method is missing
            if hasattr(self.dashboard_ui, 'dashb_lowinstock_value'):
                self.dashboard_ui.dashb_lowinstock_value.setText("Error")
            if hasattr(self.dashboard_ui, 'label_13'):
                self.dashboard_ui.label_13.setText("Error loading low stock. Check model.")
                self.dashboard_ui.label_13.setStyleSheet("color: red;")
            self._clear_low_stock_labels()
        except Exception as e:
            self.logger.error(f"Error loading low stock warning: {e}", exc_info=True)
            # CORRECTED: Use self.dashboard_ui for QMessageBox parent
            QMessageBox.warning(
                self.dashboard_ui, "Low Stock Warning Error",
                f"Failed to load low stock data: {e}")

    # Helper method to clear low stock labels
    def _clear_low_stock_labels(self):
        # Ensure these loops correctly iterate over your actual QLabel objects
        for label in self.lowstock_product_labels:
            if label:
                label.setText("")
                label.setVisible(False)
        for label in self.lowstock_qty_labels:
            if label:
                label.setText("")
                label.setVisible(False)

    def _display_low_stock_items(self, low_stock_products):
        self.logger.debug("Displaying low stock items")
        # CORRECTED: Use self.dashboard_ui for label_13
        if hasattr(self.dashboard_ui, 'label_13'):
            self.dashboard_ui.label_13.setText("Warning! These items are low of stock.")
            self.dashboard_ui.label_13.setStyleSheet(
                "color: white; border-radius: 15px; padding: 3px; background-color: #c25b55;"
            )
        # Ensure these are your actual QLabel objects defined in your UI
        for i in range(len(self.lowstock_product_labels)):
            if i < len(low_stock_products):
                item_dict = low_stock_products[i]
                product_name = item_dict.get('product_name', 'N/A')
                current_qty = item_dict.get('prod_spec_stock_qty', 0)

                if self.lowstock_product_labels[i]:
                    self.lowstock_product_labels[i].setText(str(product_name))
                    font = QtGui.QFont()
                    font.setFamily("Poppins")
                    # CORRECTED: Ensure font size is positive, e.g., 16
                    font.setPointSize(16) # Set a default positive size
                    self.lowstock_product_labels[i].setFont(font)
                    palette = self.lowstock_product_labels[i].palette()
                    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#000000"))
                    self.lowstock_product_labels[i].setPalette(palette)
                    self.lowstock_product_labels[i].setVisible(True)

                if self.lowstock_qty_labels[i]:
                    self.lowstock_qty_labels[i].setText(f"ONLY {current_qty} LEFT")
                    self.lowstock_qty_labels[i].setAlignment(Qt.AlignRight | Qt.AlignVCenter)
                    font = QtGui.QFont()
                    font.setFamily("Poppins")
                    # CORRECTED: Ensure font size is positive, e.g., 16
                    font.setPointSize(16) # Set a default positive size
                    self.lowstock_qty_labels[i].setFont(font)
                    palette = self.lowstock_qty_labels[i].palette()
                    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#b2423c"))
                    self.lowstock_qty_labels[i].setPalette(palette)
                    self.lowstock_qty_labels[i].setVisible(True)
            else:
                # Hide unused labels
                if self.lowstock_product_labels[i]:
                    self.lowstock_product_labels[i].setText("")
                    self.lowstock_product_labels[i].setVisible(False)
                if self.lowstock_qty_labels[i]:
                    self.lowstock_qty_labels[i].setText("")
                    self.lowstock_qty_labels[i].setVisible(False)


    def _display_no_low_stock(self):
        self.logger.debug("Displaying no low stock message")
        # CORRECTED: Use self.dashboard_ui for label_13
        if hasattr(self.dashboard_ui, 'label_13'):
            self.dashboard_ui.label_13.setText("All items are well stocked.")
            self.dashboard_ui.label_13.setStyleSheet(
                "color: white; border-radius: 15px; padding: 3px; background-color: #5cb85c;"
            )
        # Only set the first label if there's no low stock
        if self.lowstock_product_labels and self.lowstock_product_labels[0]:
            self.lowstock_product_labels[0].setText("No products are low in stock.")
            self.lowstock_product_labels[0].setStyleSheet("font-style: italic; color: grey; text-align: center;") # Added text-align
            self.lowstock_product_labels[0].setAlignment(Qt.AlignCenter)
            self.lowstock_product_labels[0].setVisible(True) # Ensure it's visible

        # Hide other labels if no low stock
        for i in range(1, len(self.lowstock_product_labels)): # Iterate over remaining labels
            if self.lowstock_product_labels[i]:
                self.lowstock_product_labels[i].setText("")
                self.lowstock_product_labels[i].setVisible(False)
            if self.lowstock_qty_labels[i]:
                self.lowstock_qty_labels[i].setText("")
                self.lowstock_qty_labels[i].setVisible(False)


    # --- Button Click Handlers ---
    def on_view_sales_report_clicked(self):
        self.logger.info("View Sales Report button clicked!")
        # CORRECTED: Use self.dashboard_ui for QMessageBox parent
        QMessageBox.information(self.dashboard_ui, "Action", "Navigating to Sales Report (Not yet implemented)")

    def on_view_more_inventory_clicked(self):
        self.logger.info("View More in Inventory button clicked!")
        # CORRECTED: Use self.dashboard_ui for QMessageBox parent
        QMessageBox.information(self.dashboard_ui, "Action", "Navigating to Inventory (Not yet implemented)")

    # --- Navigation Button Handlers ---
    def on_dashboard_clicked(self):
        self.logger.info("Dashboard button clicked!")
        # Implement logic to navigate to the Dashboard (might already be on this page)
        # if self.parent and hasattr(self.parent, 'show_dashboard_page'):
        #     self.parent.show_dashboard_page()

    def on_inventory_clicked(self):
        self.logger.info("Inventory button clicked!")
        if self.parent and hasattr(self.parent, 'show_inventory_page'):
            self.parent.show_inventory_page()

    def on_orders_clicked(self):
        self.logger.info("Orders button clicked!")
        if self.parent and hasattr(self.parent, 'show_orders_page'):
            self.parent.show_orders_page()

    def on_sales_clicked(self):
        self.logger.info("Sales button clicked!")
        if self.parent and hasattr(self.parent, 'show_sales_page'):
            self.parent.show_sales_page()

    def on_account_clicked(self):
        self.logger.info("Account button clicked!")
        if self.parent and hasattr(self.parent, 'show_account_page'):
            self.parent.show_account_page()

    def on_stock_history_clicked(self):
        self.logger.info("Stock History button clicked!")
        if self.parent and hasattr(self.parent, 'show_stock_history_page'):
            self.parent.show_stock_history_page()

    def on_logout_clicked(self):
        self.logger.info("Logout button clicked!")
        # CORRECTED: Use self.dashboard_ui for QMessageBox parent
        reply = QMessageBox.question(self.dashboard_ui, 'Logout', 'Are you sure you want to log out?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.parent and hasattr(self.parent, 'logout_user'):
                self.parent.logout_user()
            else:
                # CORRECTED: Use self.dashboard_ui for QMessageBox parent
                QMessageBox.information(self.dashboard_ui, "Logout", "Logout logic not fully implemented yet.")