# controllers/OSales_pageController.py

from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView, QMessageBox
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QCalendarWidget, QDialog, QVBoxLayout, QPushButton
from models.database import Database
from datetime import datetime


class SalesPageController:
    # MODIFIED __init__ to accept keyword arguments from OwnerController
    def __init__(self, sales_ui, parent_controller, current_user_id, current_shop_id, database_connection):
        self.ui = sales_ui # Map sales_ui to self.ui
        self.parent_controller = parent_controller # Store the parent controller
        self.current_user_id = current_user_id
        self.current_shop_id = current_shop_id
        self.database = database_connection # Map database_connection to self.database

        # Initialize default dates
        self.start_date_obj = QDate.currentDate().addDays(-30) # Default: 30 days ago
        self.end_date_obj = QDate.currentDate() # Default: Today

        # --- Initial UI Setup ---
        self._initial_ui_setup()
        self._connect_signals()

        # Initial data load
        self.load_sales_data() # Use this single method to handle initial load and view switching

    def _initial_ui_setup(self):
        # Set initial text for the date buttons
        self.ui.pushButton_StartDate.setText(self.start_date_obj.toString("yyyy-MM-dd"))
        self.ui.pushButton_EndDate.setText(self.end_date_obj.toString("yyyy-MM-dd"))

        # Setup Sales Summary Table
        summary_headers = ["Report ID", "Shop Branch", "Total Quantity Sold", "Total Revenue (₱)", "Date Generated"]
        self.ui.tableWidget_salesSummary.setColumnCount(len(summary_headers))
        self.ui.tableWidget_salesSummary.setHorizontalHeaderLabels(summary_headers)
        self.ui.tableWidget_salesSummary.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_salesSummary.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Setup Sales Detailed Table
        detail_headers = ["Detail ID", "Product Name", "Quantity Sold", "Total Sales Amount (₱)", "Date Recorded"]
        self.ui.tableWidget_orderDetails.setColumnCount(len(detail_headers))
        self.ui.tableWidget_orderDetails.setHorizontalHeaderLabels(detail_headers)
        self.ui.tableWidget_orderDetails.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_orderDetails.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Ensure SALES_label is visible and has default text
        self.ui.SALES_label.setText("Sales Report")
        
        # Set initial view to summary (default)
        self.ui.stackedWidget_Sales.setCurrentIndex(0) # 0 for summary page
        # Apply initial button styles
        self._apply_view_button_styles("summary")


    def _connect_signals(self):
        # Connect filter and generate report buttons
        self.ui.comboBox_filterSales.currentIndexChanged.connect(self.load_sales_data)
        self.ui.pushButton_GenerateSReport.clicked.connect(self.load_sales_data)
        
        # Connect the view switching buttons
        self.ui.pushButton_summaryView.clicked.connect(self._show_summary_view)
        self.ui.pushButton_salesDetail.clicked.connect(self._show_detailed_view)

        # Connect the date buttons to open the date pickers
        self.ui.pushButton_StartDate.clicked.connect(self._open_start_date_picker)
        self.ui.pushButton_EndDate.clicked.connect(self._open_end_date_picker)


    def _apply_view_button_styles(self, active_view):
        """Applies consistent styling to the view switching buttons."""
        active_style = "background-color: #8d2721; color: white;" # Your active color
        inactive_style = "background-color: #003366; color: white;" # Your inactive color

        if active_view == "summary":
            self.ui.pushButton_summaryView.setStyleSheet(active_style)
            self.ui.pushButton_salesDetail.setStyleSheet(inactive_style)
        elif active_view == "detail":
            self.ui.pushButton_summaryView.setStyleSheet(inactive_style)
            self.ui.pushButton_salesDetail.setStyleSheet(active_style)


    def load_sales_data(self):
        """
        Loads sales data into the currently active table widget based on the selected filter
        and date range. This is the main method for refreshing data.
        """
        print(f"DEBUG: Loading sales data for Shop ID: {self.current_shop_id}")
        self.ui.tableWidget_salesSummary.setRowCount(0)
        self.ui.tableWidget_orderDetails.setRowCount(0)

        current_view_index = self.ui.stackedWidget_Sales.currentIndex()

        if current_view_index == 0: # Summary View
            print("DEBUG: Refreshing Sales Summary...")
            self._load_sales_summary()
        elif current_view_index == 1: # Detailed View
            print("DEBUG: Refreshing Sales Details...")
            self._load_sales_details()

    def _show_summary_view(self):
        self.ui.stackedWidget_Sales.setCurrentIndex(0) # Index 0 is the summary page
        self._apply_view_button_styles("summary")
        self._load_sales_summary() # Reload data when view changes

    def _show_detailed_view(self):
        self.ui.stackedWidget_Sales.setCurrentIndex(1) # Index 1 is the detailed page
        self._apply_view_button_styles("detail")
        self._load_sales_details() # Reload data when view changes

    def _load_sales_summary(self):
        print("DEBUG: Loading Sales Summary...")
        self.ui.tableWidget_salesSummary.setRowCount(0)

        filter_text = self.ui.comboBox_filterSales.currentText().strip()
        
        start_date = self.start_date_obj.toString("yyyy-MM-dd")
        end_date = self.end_date_obj.toString("yyyy-MM-dd")

        group_by_clause = ""
        select_period_clause = ""

        if "Daily" in filter_text:
            select_period_clause = "TO_CHAR(oh.oh_created_at, 'YYYY-MM-DD') AS period_display"
            group_by_clause = "GROUP BY period_display"
        elif "Weekly" in filter_text:
            select_period_clause = "TO_CHAR(oh.oh_created_at, 'YYYY-IW') AS period_display"
            group_by_clause = "GROUP BY period_display"
        elif "Monthly" in filter_text:
            select_period_clause = "TO_CHAR(oh.oh_created_at, 'YYYY-MM') AS period_display"
            group_by_clause = "GROUP BY period_display"
        elif "Annually" in filter_text:
            select_period_clause = "EXTRACT(YEAR FROM oh.oh_created_at) AS period_display"
            group_by_clause = "GROUP BY period_display"
        else: # Default for "Filter Sales" or any other non-specific filter. Assume Daily.
            select_period_clause = "TO_CHAR(oh.oh_created_at, 'YYYY-MM-DD') AS period_display"
            group_by_clause = "GROUP BY period_display"

        full_query = f"""
            SELECT
                {select_period_clause},
                SUM(od.od_quantity) AS total_quantity_sold,
                SUM(od.od_total_amt) AS total_revenue
            FROM
                order_header oh
            JOIN
                order_detail od ON oh.oh_id = od.oh_id AND oh.shop_id = od.shop_id
            WHERE
                oh.shop_id = %s
                AND oh.oh_created_at BETWEEN %s AND (%s::timestamp + INTERVAL '1 day' - INTERVAL '1 second')
            {group_by_clause}
            ORDER BY
                period_display DESC;
            """
        params = [self.current_shop_id, start_date, end_date]

        try:
            sales_summary = self.database.fetch_all(full_query, params)
            print(f"DEBUG: Sales Summary Query: {full_query}")
            print(f"DEBUG: Sales Summary Params: {params}")

            if sales_summary:
                self.ui.tableWidget_salesSummary.setRowCount(len(sales_summary))
                for row_idx, summary in enumerate(sales_summary):
                    period_val = summary.get('period_display', 'N/A')
                    self.ui.tableWidget_salesSummary.setItem(row_idx, 0, QTableWidgetItem(str(period_val)))
                    
                    self.ui.tableWidget_salesSummary.setItem(row_idx, 1, QTableWidgetItem("All Branches"))
                    
                    self.ui.tableWidget_salesSummary.setItem(row_idx, 2, QTableWidgetItem(str(summary.get('total_quantity_sold', 0))))
                    self.ui.tableWidget_salesSummary.setItem(row_idx, 3, QTableWidgetItem(f"₱{summary.get('total_revenue', 0.00):.2f}"))
                    self.ui.tableWidget_salesSummary.setItem(row_idx, 4, QTableWidgetItem(QDate.currentDate().toString("yyyy-MM-dd")))
            else:
                print("No sales summary data found for the selected period and date range.")
        except Exception as e:
            print(f"Error executing sales summary query: {e}")
            # Ensure self.ui.sales_inview is the correct parent widget for QMessageBox
            # If not, use self.ui or None
            QMessageBox.critical(self.ui, "Database Error", f"Failed to load sales summary: {e}")


    def _load_sales_details(self):
        print("DEBUG: Loading Sales Details...")
        self.ui.tableWidget_orderDetails.setRowCount(0)

        start_date = self.start_date_obj.toString("yyyy-MM-dd")
        end_date = self.end_date_obj.toString("yyyy-MM-dd")

        query = """
            SELECT
                od.od_id AS detail_id,
                s.shop_branch_name AS shop_name, -- Corrected column name based on your DDL
                p.product_name,
                od.od_quantity AS quantity_sold,
                od.od_total_amt AS total_sales_amount,
                oh.oh_created_at AS date_recorded
            FROM
                order_detail od
            JOIN
                product p ON od.product_id = p.product_id AND od.shop_id = p.shop_id
            JOIN
                order_header oh ON od.oh_id = oh.oh_id AND od.shop_id = oh.shop_id
            JOIN
                shop s ON oh.shop_id = s.shop_id
            WHERE
                oh.shop_id = %s
                AND oh.oh_created_at BETWEEN %s AND (%s::timestamp + INTERVAL '1 day' - INTERVAL '1 second')
            ORDER BY
                oh.oh_created_at DESC;
            """
        params = [self.current_shop_id, start_date, end_date]

        try:
            sales_details = self.database.fetch_all(query, params)
            print(f"DEBUG: Sales Details Query: {query}")
            print(f"DEBUG: Sales Details Params: {params}")

            if sales_details:
                self.ui.tableWidget_orderDetails.setRowCount(len(sales_details))
                for row_idx, detail in enumerate(sales_details):
                    self.ui.tableWidget_orderDetails.setItem(row_idx, 0, QTableWidgetItem(str(detail.get('detail_id', ''))))
                    self.ui.tableWidget_orderDetails.setItem(row_idx, 1, QTableWidgetItem(detail.get('product_name', '')))
                    self.ui.tableWidget_orderDetails.setItem(row_idx, 2, QTableWidgetItem(str(detail.get('quantity_sold', 0))))
                    self.ui.tableWidget_orderDetails.setItem(row_idx, 3, QTableWidgetItem(f"₱{detail.get('total_sales_amount', 0.00):.2f}"))
                    
                    date_recorded = detail.get('date_recorded')
                    if isinstance(date_recorded, datetime):
                        formatted_date = date_recorded.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        formatted_date = str(date_recorded)
                    self.ui.tableWidget_orderDetails.setItem(row_idx, 4, QTableWidgetItem(formatted_date))
            else:
                print("No sales detail data found for the selected date range.")
        except Exception as e:
            print(f"Error executing sales detail query: {e}")
            # Ensure self.ui.sales_inview is the correct parent widget for QMessageBox
            # If not, use self.ui or None
            QMessageBox.critical(self.ui, "Database Error", f"Failed to load sales details: {e}")


    def _open_start_date_picker(self):
        self._open_date_picker(self._set_start_date, self.start_date_obj)

    def _open_end_date_picker(self):
        self._open_date_picker(self._set_end_date, self.end_date_obj)

    def _open_date_picker(self, set_date_callback, current_date):
        """
        Opens a QCalendarWidget in a dialog for date selection.
        :param set_date_callback: The function to call with the selected QDate object.
        :param current_date: The QDate object representing the currently selected date.
        """
        # Parent the dialog to self.ui (the main widget of the sales page)
        dialog = QDialog(self.ui)
        dialog.setWindowTitle("Select Date")
        dialog.setFixedSize(300, 300)

        layout = QVBoxLayout(dialog)
        calendar = QCalendarWidget()
        calendar.setSelectedDate(current_date)
        layout.addWidget(calendar)

        ok_button = QPushButton("OK")
        layout.addWidget(ok_button)

        def on_ok_clicked():
            selected_date = calendar.selectedDate()
            set_date_callback(selected_date)
            dialog.accept()

        ok_button.clicked.connect(on_ok_clicked)

        dialog.exec_()


    def _set_start_date(self, date_obj):
        self.start_date_obj = date_obj
        self.ui.pushButton_StartDate.setText(self.start_date_obj.toString("yyyy-MM-dd"))
        self.load_sales_data() # Call the main loading method

    def _set_end_date(self, date_obj):
        self.end_date_obj = date_obj
        self.ui.pushButton_EndDate.setText(self.end_date_obj.toString("yyyy-MM-dd"))
        self.load_sales_data() # Call the main loading method

    def generate_sales_report(self):
        print("DEBUG: Generate Sales Report button clicked.")
        pass