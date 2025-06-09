# controllers/OOrders_pageController.py

from PyQt5.QtWidgets import QTableWidgetItem,  QAbstractItemView
from PyQt5.QtCore import Qt, QTimer
from models.database import Database
from datetime import datetime

class OrdersPageController:
    def __init__(self, orders_ui, parent_controller=None, current_user_id=None,
                 current_shop_id=None, database_connection=None):
        self.ui = orders_ui
        self.parent_controller = parent_controller
        self.current_user_id = current_user_id
        self.current_shop_id = current_shop_id
        self.database = database_connection if database_connection else Database() # Use provided connection or create new
        print(f"DEBUG: OOrders_pageController initialized for Shop ID: {self.current_shop_id}, User ID: {self.current_user_id}")

        self._connect_signals()
        self._setup_ui()
        self.load_order_history() # Load initial data when the page is initialized

    def _connect_signals(self):
        # Connect the filter combobox to the refresh method
        # Renamed from comboBox_OrderType to comboBox_filterOrders as per UI
        self.ui.comboBox_filterOrders.currentIndexChanged.connect(self.load_order_history)
        
        # Connect the search button and line edit
        # Renamed from lineEdit_OrderSearch to lineEdit__QuickSearch_Orders as per UI
        self.ui.lineEdit__QuickSearch_Orders.returnPressed.connect(self.load_order_history)
        self.ui.pushButton_searchOrders.clicked.connect(self.load_order_history)

    def _setup_ui(self):
        # Set up table headers for the orders table
        # Renamed from tableWidget_Orders to tableWidget_order as per UI
        headers = [
            "Order ID", "Customer Name", "Products", "Price",
            "Quantity", "Subtotal", "Total Amount (₱)", "Created at"
        ]
        self.ui.tableWidget_order.setColumnCount(len(headers))
        self.ui.tableWidget_order.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget_order.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget_order.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Ensure orderReportText is visible and has default text
        self.ui.orderReportText.setText("Order History")


    # In OOrders_pageController.py

    def load_order_history(self):
        print("DEBUG: Loading order history...")
        self.ui.tableWidget_order.setRowCount(0)

        filter_text = self.ui.comboBox_filterOrders.currentText().strip()
        search_query = self.ui.lineEdit__QuickSearch_Orders.text().strip()

        query = """
            SELECT
                oh.oh_id AS order_id,                 -- Use oh_id from order_header
                oh.oh_by_customer_name AS customer_name, -- Use oh_by_customer_name
                p.product_name,
                od.od_product_price AS prod_spec_price, -- Use od_product_price from order_detail
                od.od_quantity AS order_item_quantity, -- Use od_quantity from order_detail
                od.od_total_amt AS subtotal,          -- Use od_total_amt from order_detail for item subtotal
                -- You'll need to SUM od.od_total_amt from order_detail for the overall order total,
                -- or add a column in order_header for total order amount if it exists.
                -- Assuming oh_total_amount or similar exists in order_header for the overall total.
                -- If not, you might need a subquery or aggregation.
                -- For now, let's assume 'order_total_amount' is desired from order_header
                -- If order_header itself has a total, use that. Otherwise, calculate.
                -- Let's use oh.oh_total_amount if it were there. Since it's not directly,
                -- we'll sum order_detail totals later, or you may need to add a total_amount
                -- column to order_header.
                -- For simplicity, let's just use the od_total_amt as a per-item subtotal for now.
                -- The original had o.order_total_amount, which isn't directly in oh.
                -- Let's use a subquery for the total amount for each order.
                -- Let's use the sum of od_total_amt for the specific order.
                SUM(od.od_total_amt) OVER (PARTITION BY oh.oh_id) AS order_total_amount, -- Calculate total amount for each order
                oh.oh_created_at AS order_created_at          -- Use oh_created_at
            FROM
                order_detail od         -- Corrected table name
            JOIN
                product p ON od.product_id = p.product_id AND od.shop_id = p.shop_id
            JOIN
                order_header oh ON od.oh_id = oh.oh_id AND od.shop_id = oh.shop_id -- Corrected table name and join condition
            WHERE
                oh.shop_id = %s
        """
        params = [self.current_shop_id]

        if filter_text != "Filter Orders" and filter_text != "":
            # Assuming product_type_id is in product table
            query += " AND p.product_type_id = (SELECT prod_type_id FROM product_type WHERE prod_type_name = %s)"
            params.append(filter_text)

        if search_query:
            query += " AND (oh.oh_by_customer_name ILIKE %s OR p.product_name ILIKE %s OR CAST(oh.oh_id AS TEXT) ILIKE %s)"
            params.extend([f"%{search_query}%", f"%{search_query}%", f"%{search_query}%"])

        query += " GROUP BY oh.oh_id, oh.oh_by_customer_name, p.product_name, od.od_product_price, od.od_quantity, od.od_total_amt, oh.oh_created_at" # Needed for SUM OVER window function
        query += " ORDER BY oh.oh_created_at DESC;"

        try:
            orders = self.database.fetch_all(query, params)

            if orders:
                self.ui.tableWidget_order.setRowCount(len(orders))
                for row_idx, order in enumerate(orders):
                    self.ui.tableWidget_order.setItem(row_idx, 0, QTableWidgetItem(str(order['order_id'])))
                    self.ui.tableWidget_order.setItem(row_idx, 1, QTableWidgetItem(order['customer_name']))
                    self.ui.tableWidget_order.setItem(row_idx, 2, QTableWidgetItem(order['product_name']))
                    self.ui.tableWidget_order.setItem(row_idx, 3, QTableWidgetItem(f"₱{order['prod_spec_price']:.2f}"))
                    self.ui.tableWidget_order.setItem(row_idx, 4, QTableWidgetItem(str(order['order_item_quantity'])))
                    self.ui.tableWidget_order.setItem(row_idx, 5, QTableWidgetItem(f"₱{order['subtotal']:.2f}"))
                    self.ui.tableWidget_order.setItem(row_idx, 6, QTableWidgetItem(f"₱{order['order_total_amount']:.2f}")) # This will be the overall order total now
                    
                    created_at = order['order_created_at']
                    if isinstance(created_at, datetime):
                        formatted_time = created_at.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        formatted_time = str(created_at)
                    self.ui.tableWidget_order.setItem(row_idx, 7, QTableWidgetItem(formatted_time))
            else:
                print("No order history data to display.")
        except Exception as e:
            print(f"Error loading order history: {e}")