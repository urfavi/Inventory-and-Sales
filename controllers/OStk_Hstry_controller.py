from PyQt5 import QtWidgets, QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView
#from models.database import Database # Uncomment if your Database class is here
from models.OStk_Hstry_model import StockHistoryModel

class StockHistoryPageController:
    # Define column constants for clarity (optional, but good practice)
    COL_HISTORY_ID = 0 # Hidden column
    COL_USER_ID = 1
    COL_USERNAME = 2
    COL_ACTION = 3
    COL_PRODUCT_NAME = 4
    COL_OLD_QTY = 5
    COL_NEW_QTY = 6
    COL_UPDATED_AT = 7

    def __init__(self, history_ui, history_widget, current_user_shop_id, database_connection, parent=None):
        """
        Initialize the stock history controller.

        Args:
            history_ui: The UI elements for stock history (an instance of Ui_OWNER_STOCKHISTORY).
            history_widget: The QWidget that this controller manages (e.g., the main stock history tab/page).
            current_user_shop_id: The shop_id of the currently logged-in user.
                                  Defaults to 1 if None or invalid.
            database_connection: An active database connection object.
            parent: Optional parent widget reference.
        """
        if history_ui is None:
            QMessageBox.critical(None, "Initialization Error", "Stock History UI element (history_ui) was not provided.")
            raise ValueError("history_ui must be provided to StockHistoryPageController")
            
        self.ui = history_ui
        self.history_widget = history_widget
        self.parent = parent

        # Handle shop ID with validation
        try:
            # Ensure current_user_shop_id is an integer; default to 1 if conversion fails or is None
            self.current_user_shop_id = int(current_user_shop_id) if current_user_shop_id is not None else 1
        except (ValueError, TypeError):
            print("WARNING: Invalid shop_id provided. Defaulting to 1.")
            self.current_user_shop_id = 1

        # Initialize model with the database connection
        if database_connection is None:
            print("ERROR: Missing database connection for StockHistoryModel.")
            QMessageBox.critical(self.history_widget, "Initialization Error",
                                 "Database connection is required to manage stock history.")
            self.history_model = None # Model will not be functional
        else:
            self.database = database_connection
            self.history_model = StockHistoryModel(self.database)

        # Set up initial UI connections and load data
        self._setup_connections()
        self.initialize_stock_history_table()
        self.load_stock_history() # Load data upon initialization

        self.search_timer = QtCore.QTimer()
        self.search_timer.setSingleShot(True)  # Only trigger once per timeout
        self.search_timer.timeout.connect(self.filter_stock_history)
        
        # Connect the text changed signal
        self.ui.lineEdit_OWNER_QuickSearch_StockHistory.textChanged.connect(
            self._on_search_text_changed
        )

        # Manual search button
        self.ui.pushButton_SEARCH_StockHistory.clicked.connect(
            self.filter_stock_history  # Directly call without debounce
        )

    def _setup_connections(self):
        """Connect all UI signals to their respective slots, with robustness checks."""
        try:
            # Connect filter combo box
            self.ui.comboBox_filterStockHistory.currentTextChanged.connect(self.update_stock_history_label)
            self.ui.comboBox_filterStockHistory.currentTextChanged.connect(self.load_stock_history)

            # Connect search functionality
            self.ui.pushButton_SEARCH_StockHistory.clicked.connect(
                self.filter_stock_history  # Directly call the filter function
            )

            # Connect delete button
            self.ui.pushButton_OWNER_Delete_Stock.clicked.connect(self.delete_selected_history)
            self.ui.pushButton_OWNER_Delete_All.clicked.connect(self.delete_all_stock_history)
            
            # Initialize label text with the current filter text
            self.update_stock_history_label(self.ui.comboBox_filterStockHistory.currentText())

            # Optional: Trigger search on pressing 'Enter' in the search box
            self.ui.lineEdit_OWNER_QuickSearch_StockHistory.returnPressed.connect(
                self.filter_stock_history
            )

        except AttributeError as e:
            self._show_error_message(f"Critical UI element missing for Stock History: {e}\nPlease check your UI design file (Ui_OWNER_STOCKHISTORY.py).", title="UI Connection Error")
        except Exception as e:
            self._show_error_message(f"An unexpected error occurred during Stock History connection setup: {e}", title="Connection Setup Error")

    def initialize_stock_history_table(self):
        """Initialize the stock history table with columns, with robustness checks."""
        try:
            self.ui.tableWidget_StockHistory.setColumnCount(8) # Increased to 8 for the hidden ID
            self.ui.tableWidget_StockHistory.setHorizontalHeaderLabels([
                "History ID",    # Hidden
                "User ID",
                "Username",
                "Action",
                "Product Name",
                "Old Qty",
                "New Qty",
                "Updated At"
            ])
            self.ui.tableWidget_StockHistory.setColumnHidden(self.COL_HISTORY_ID, True) # Hide the ID column

            # Set table properties
            self.ui.tableWidget_StockHistory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.tableWidget_StockHistory.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.ui.tableWidget_StockHistory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            # self.ui.tableWidget_StockHistory.setStyleSheet(
            # "QTableView::item:selected { background-color: #3498db; color: white; }")

            self.ui.tableWidget_StockHistory.setSortingEnabled(True) # Enable sorting by columns
            
            # Auto-resize columns initially based on content
             # Set initial column widths
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_USER_ID, 160)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_USERNAME, 170)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_ACTION, 180)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_PRODUCT_NAME, 260)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_OLD_QTY, 180)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_NEW_QTY, 180)
            self.ui.tableWidget_StockHistory.setColumnWidth(self.COL_UPDATED_AT, 290)

            # Set resize modes
            header = self.ui.tableWidget_StockHistory.horizontalHeader()
            header.setSectionResizeMode(self.COL_USER_ID, QHeaderView.Fixed)
            header.setSectionResizeMode(self.COL_USERNAME, QHeaderView.Fixed)
            header.setSectionResizeMode(self.COL_ACTION, QHeaderView.Fixed)
            header.setSectionResizeMode(self.COL_PRODUCT_NAME, QHeaderView.Fixed)  # Only this column stretches
            header.setSectionResizeMode(self.COL_OLD_QTY, QHeaderView.Fixed)
            header.setSectionResizeMode(self.COL_NEW_QTY, QHeaderView.Fixed)
            header.setSectionResizeMode(self.COL_UPDATED_AT, QHeaderView.Fixed)

        except AttributeError as e:
            self._show_error_message(f"Critical table widget or UI element missing: {e}\nPlease check your UI design file (tableWidget_StockHistory).", title="Table Init Error")
        except Exception as e:
            self._show_error_message(f"An unexpected error occurred during Stock History table initialization: {e}", title="Table Init Error")

    def update_stock_history_label(self, filter_text: str):
        """Update the stock history label based on the selected filter."""
        try:
            # Using a dictionary for cleaner mapping
            label_map = {
                "roof": "Roof Stock History",
                "spandrel": "Spandrel Stock History",
                "gutter": "Gutter Stock History",
                "others": "Other Stock History"
            }
            # Remove leading/trailing spaces and convert to lowercase for robust comparison
            normalized_filter = filter_text.strip().lower()
            self.ui.stockHistoryText.setText(label_map.get(normalized_filter, "All Stock History"))
        except AttributeError as e:
            self._show_error_message(f"Missing 'stockHistoryText' label in UI: {e}. Check your Ui_OWNER_STOCKHISTORY.py.", title="UI Label Error")
        except Exception as e:
            self._show_error_message(f"An unexpected error occurred updating history label: {e}", title="Label Update Error")

    def load_stock_history(self):
        """Load stock history data based on current filter."""
        if self.history_model is None:
            self._show_error_message("Cannot load stock history: Database connection failed during initialization.", title="Database Error")
            self.ui.tableWidget_StockHistory.setRowCount(0)
            return
        
        try:
            # Store current column widths before reloading
            column_widths = {}
            for col in range(self.ui.tableWidget_StockHistory.columnCount()):
                column_widths[col] = self.ui.tableWidget_StockHistory.columnWidth(col)

            filter_text = self.ui.comboBox_filterStockHistory.currentText().strip()
            print(f"DEBUG: Selected filter text: '{filter_text}'")

            # Map UI filter text to database values
            type_mapping = {
                "Filter History": None, # Assuming "Filter History" means no specific type filter
                "Roof": "ROOF",
                "Spandrel": "SPANDREL",
                "Gutter": "GUTTER",
                "Others": "OTHER"
            }
            
            # Get the database product type (None means no filtering)
            db_product_type = type_mapping.get(filter_text, None)
            
            # Get history data
            history_data = self.history_model.get_stock_history(
                product_type=db_product_type,
                shop_id=self.current_user_shop_id
            )
            
            # Populate table
            self._populate_history_table(history_data) # Pass the list directly

            for col, width in column_widths.items():
                if col < self.ui.tableWidget_StockHistory.columnCount():  # Ensure column exists
                    self.ui.tableWidget_StockHistory.setColumnWidth(col, width)

        except AttributeError as e:
             self._show_error_message(f"UI element for filter combo box missing: {e}. Check your Ui_OWNER_STOCKHISTORY.py.", title="UI Element Error")
        except Exception as e:
            self._show_error_message(f"Failed to load stock history: {str(e)}", title="Load History Error")


    def _populate_history_table(self, history_data: list):
        """Populate the table with history data."""
        try:
            # Store current column widths
            column_widths = {}
            for col in range(self.ui.tableWidget_StockHistory.columnCount()):
                column_widths[col] = self.ui.tableWidget_StockHistory.columnWidth(col)

            self.ui.tableWidget_StockHistory.setRowCount(0) # Clear existing rows

            if not history_data:
                print("No stock history data to display.")
                # Optionally display a message in the table or a status bar
                return

            # Ensure column count is correct if headers were reset or changed
            if self.ui.tableWidget_StockHistory.columnCount() != 8:
                 self.initialize_stock_history_table() # Re-initialize if column count is off

            for row_idx, record in enumerate(history_data):
                self.ui.tableWidget_StockHistory.insertRow(row_idx)

                # Fetch data using .get() for safety against missing keys
                history_id = str(record.get('stk_hstry_id', 'N/A'))
                user_id = str(record.get('user_id', 'N/A'))
                username = record.get('user_acc_username', 'N/A')
                action_raw = record.get('action_type', 'N/A')
                product_name = record.get('product_name', 'N/A')
                old_qty = str(record.get('old_quantity', 'N/A'))
                new_qty = str(record.get('new_quantity', 'N/A'))

                updated_at = record.get('timestamp')
                formatted_updated_at = updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else "N/A"

                # Populate items and set alignment using COL_ constants
                items_to_set = [
                    (self.COL_HISTORY_ID, history_id, Qt.AlignVCenter | Qt.AlignLeft), # Hidden
                    (self.COL_USER_ID, user_id, Qt.AlignVCenter | Qt.AlignCenter),
                    (self.COL_USERNAME, username, Qt.AlignVCenter | Qt.AlignLeft),
                    (self.COL_ACTION, action_raw, Qt.AlignVCenter | Qt.AlignLeft),
                    (self.COL_PRODUCT_NAME, product_name, Qt.AlignVCenter | Qt.AlignCenter),
                    (self.COL_OLD_QTY, old_qty, Qt.AlignVCenter | Qt.AlignCenter),
                    (self.COL_NEW_QTY, new_qty, Qt.AlignVCenter | Qt.AlignCenter),
                    (self.COL_UPDATED_AT, formatted_updated_at, Qt.AlignVCenter | Qt.AlignCenter)
                ]

                for col, text, alignment in items_to_set:
                    item = QTableWidgetItem(text)
                    item.setTextAlignment(alignment)
                    self.ui.tableWidget_StockHistory.setItem(row_idx, col, item)
            
            # The column resizing is already handled well in initialize_stock_history_table()
            # It's usually best to do it once there, and let QHeaderView.Stretch handle the rest
            # unless you have a specific reason to re-apply after every populate.
            # However, if you add/remove rows frequently, resizeColumnsToContents might be useful
            # after populating, but setSectionResizeMode should be done only once.
            self.ui.tableWidget_StockHistory.resizeColumnsToContents()

            for col, width in column_widths.items():
                if col < self.ui.tableWidget_StockHistory.columnCount():  # Ensure column exists
                    self.ui.tableWidget_StockHistory.setColumnWidth(col, width)

        except Exception as e:
            self._show_error_message(f"An error occurred while populating the table: {e}", title="Table Population Error")

    def _on_search_text_changed(self):
        """Handler for text changes that starts the debounce timer"""
        self.search_timer.start(400)  # 300ms delay after typing stops

    def filter_stock_history(self):
        """Filter the table ONLY when button/Enter is pressed"""
        try:
            search_text = self.ui.lineEdit_OWNER_QuickSearch_StockHistory.text().lower()
            
            for row in range(self.ui.tableWidget_StockHistory.rowCount()):
                match = False
                # Search only in visible columns (skip hidden history_id column)
                for col in range(self.COL_USER_ID, self.ui.tableWidget_StockHistory.columnCount()):
                    item = self.ui.tableWidget_StockHistory.item(row, col)
                    if item and search_text in item.text().lower():
                        match = True
                        break
                
                self.ui.tableWidget_StockHistory.setRowHidden(row, not match)

        except Exception as e:
            self._show_error_message(f"Search error: {str(e)}", title="Search Error")
    
    def log_stock_action(self, product_spec_id: int, product_id: int, old_quantity: int, new_quantity: int, action_type: str, product_name: str, user_acc_id: int = 1) -> bool:
        """
        Logs a stock action into the history.

        Args:
            product_spec_id: The ID of the product specification.
            product_id: The ID of the product.
            old_quantity: The stock quantity before the action.
            new_quantity: The stock quantity after the action.
            action_type: The type of action (e.g., "ADD", "SALE", "ADJUSTMENT", "DELETE").
            product_name: The name of the product.
            user_acc_id: The ID of the user performing the action. Defaults to 1.

        Returns:
            True if the action was logged successfully, False otherwise.
        """
        if self.history_model is None:
            print("WARNING: Cannot log stock action - history model not initialized.")
            return False

        try:
            # Convert quantities to integers safely
            old_qty = int(old_quantity) if isinstance(old_quantity, (int, str)) and str(old_quantity).isdigit() else 0
            new_qty = int(new_quantity) if isinstance(new_quantity, (int, str)) and str(new_quantity).isdigit() else 0

            success = self.history_model.add_history_entry(
                shop_id=self.current_user_shop_id, # Use the controller's shop ID
                user_acc_id=user_acc_id, # Pass the user_acc_id received by the function
                product_spec_id=product_spec_id,
                product_id=product_id,
                product_name=product_name,
                stk_hstry_old_stock_qty=old_qty,
                stk_hstry_new_stock_qty=new_qty,
                stk_hstry_action=action_type.upper(), # Ensure action type is uppercase for consistency
            )
            
            if success:
                print(f"Successfully logged {action_type} action for product {product_id} ({product_name}).")
                # Reload history to show the new entry immediately
                self.load_stock_history() 
            return success
            
        except Exception as e:
            print(f"Error logging action: {str(e)}")
            self._show_error_message(f"Failed to log stock action: {e}", title="Log Action Error")
            return False
    
    def delete_selected_history(self):
        """Handle deletion of selected stock history record."""
        try:
            selected_items = self.ui.tableWidget_StockHistory.selectedItems()

            if not selected_items:
                QMessageBox.warning(
                    self.history_widget,
                    "No Selection",
                    "Please select a history record to delete first by clicking on a row."
                )
                return
            
            selected_row = self.ui.tableWidget_StockHistory.currentRow()
            
            # Get the history ID from the HIDDEN first column (COL_HISTORY_ID)
            history_id_item = self.ui.tableWidget_StockHistory.item(selected_row, self.COL_HISTORY_ID)

            if not history_id_item:
                self._show_error_message("Could not retrieve the ID of the selected history record. Table data might be inconsistent.", title="Deletion Error")
                return
                
            history_id = int(history_id_item.text())
            
            # Confirm deletion
            reply = QMessageBox.question(
                self.history_widget,
                "Confirm Deletion",
                "Are you sure you want to delete this history record? This action cannot be undone.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                if self.history_model.delete_history_entry(history_id):
                    QMessageBox.information(self.history_widget, "Success", "History record deleted successfully.")
                    self.load_stock_history()  # Refresh the table
                else:
                    self._show_error_message("Failed to delete history record due to a database error.", title="Deletion Error")
        except ValueError:
            self._show_error_message("Invalid history ID found for deletion. Please select a valid row.", title="Deletion Error")
        except Exception as e:
            self._show_error_message(f"An unexpected error occurred during deletion: {e}", title="Deletion Error")
    
    def delete_all_stock_history(self):
        """Simple version without processing dialog"""
        # Check if table is empty
        if self.ui.tableWidget_StockHistory.rowCount() == 0:
            QMessageBox.information(
                self.history_widget,
                "No Records",
                "The stock history table is already empty."
            )
            return
        
        # Confirm with user
        reply = QMessageBox.question(
            self.history_widget,
            "Confirm Delete All",
            "Are you sure you want to delete ALL stock history records?\nThis action cannot be undone!",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                # Perform deletion
                success = self.history_model.delete_all_history_entries(
                    shop_id=self.current_user_shop_id
                )
                
                if success:
                    QMessageBox.information(
                        self.history_widget,
                        "Success",
                        "All stock history records have been deleted successfully."
                    )
                    self.load_stock_history()  # Refresh table
                else:
                    self._show_error_message("Failed to delete all history records.")
                    
            except Exception as e:
                self._show_error_message(f"Error during deletion: {str(e)}")
                
        else:
            # User canceled - just refresh
            self.load_stock_history()
    
    def _show_error_message(self, message: str, title: str = "Error"):
        """Helper to show error messages using QMessageBox."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle(title)
        
        # Determine the parent for the QMessageBox to ensure it's displayed correctly
        if self.history_widget and self.history_widget.isVisible():
            msg.setParent(self.history_widget)
        elif self.parent:
            msg.setParent(self.parent)
        # If no suitable parent, it will be displayed as a top-level window by default
        
        msg.exec_()