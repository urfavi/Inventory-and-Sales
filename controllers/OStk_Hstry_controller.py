from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
#from models.database import Database
from models.OStk_Hstry_model import StockHistoryModel
from PyQt5.QtWidgets import QHeaderView # Make sure to import QHeaderVie

class StockHistoryPageController:
    # Define column constants for clarity (optional, but good practice)
    COL_USER_ID = 0
    COL_USERNAME = 1
    COL_ACTION = 2
    COL_PRODUCT_NAME = 3
    COL_OLD_QTY = 4
    COL_NEW_QTY = 5
    COL_UPDATED_AT = 6

    def __init__(self, history_ui, history_widget, current_user_shop_id, database_connection, parent=None):
        """
        Initialize the stock history controller

        Args:
            stkhistory_ui: The UI elements for stock history (an instance of Ui_OWNER_STOCKHISTORY).
            current_user_shop_id: The shop_id of the currently logged-in user.
                                    FOR NOW, THIS WILL BE TEMPORARILY HARDCODED TO 1 IF NONE IS PROVIDED.
            parent: Optional parent widget reference.
        """
        if history_ui is None:
            QMessageBox.critical(None, "Initialization Error", "Stock History UI element (stkhistory_ui) was not provided.")
            raise ValueError("stkhistory_ui must be provided to StockHistoryPageController")
            
        self.ui = history_ui
        self.history_widget = history_widget 
        self.parent = parent

        # Handle shop ID with validation
        try:
            self.current_user_shop_id = int(current_user_shop_id) if current_user_shop_id is not None else 1
        except (ValueError, TypeError):
            print("WARNING: Invalid shop_id. Defaulting to 1")
            self.current_user_shop_id = 1

        # Initialize model
        if database_connection is None:
            print("ERROR: Missing database connection")
            QMessageBox.critical(None, "Initialization Error", 
                            "Database connection is required")
            self.history_model = None
        else:
            self.database = database_connection
            self.history_model = StockHistoryModel(self.database)

        # Set up initial UI connections and load data
        self._setup_connections()
        self.initialize_stock_history_table()
        self.load_stock_history() # Load data upon initialization

    def _setup_connections(self):
        """Connect all UI signals to their respective slots, with robustness checks."""
        try:
            # Connect filter combo box
            self.ui.comboBox_filterStockHistory.currentTextChanged.connect(self.update_stock_history_label)
            self.ui.comboBox_filterStockHistory.currentTextChanged.connect(self.load_stock_history)

            # Connect search functionality
            self.ui.lineEdit_OWNER_QuickSearch_StockHistory.textChanged.connect(self.filter_stock_history)

            # Initialize label text with the current filter text
            self.update_stock_history_label(self.ui.comboBox_filterStockHistory.currentText())

        except AttributeError as e:
            print(f"ERROR: Missing UI element in _setup_connections: {e}. Check your Ui_OWNER_STOCKHISTORY.py.")
            self._show_error_message(f"Critical UI element missing for Stock History: {e}\nPlease check your UI design file.")
        except Exception as e:
            print(f"An unexpected error occurred during Stock History connection setup: {e}")
            self._show_error_message(f"An unexpected error occurred during Stock History setup: {e}")


    def initialize_stock_history_table(self):
        """Initialize the stock history table with columns, with robustness checks."""
        try:
            self.ui.tableWidget_StockHistory.setColumnCount(7)
            self.ui.tableWidget_StockHistory.setHorizontalHeaderLabels([
                "User ID",
                "Username",
                "Action",
                "Product Name",
                "Old Qty",
                "New Qty",
                "Updated At"
            ])

            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # Set table properties
            self.ui.tableWidget_StockHistory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.ui.tableWidget_StockHistory.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.ui.tableWidget_StockHistory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            self.ui.tableWidget_StockHistory.setSortingEnabled(True) # Enable sorting by columns
            self.ui.tableWidget_StockHistory.resizeColumnsToContents() # Adjust column widths

        except AttributeError as e:
            print(f"ERROR: Missing table widget or UI element in initialize_stock_history_table: {e}. Check your Ui_OWNER_STOCKHISTORY.py (tableWidget_StockHistory).")
            self._show_error_message(f"Critical UI table element missing: {e}\nPlease check your UI design file.")
        except Exception as e:
            print(f"An unexpected error occurred during Stock History table initialization: {e}")
            self._show_error_message(f"An unexpected error occurred during table setup: {e}")


    def update_stock_history_label(self, filter_text):
        """Update the stock history label based on the selected filter."""
        try:
            if filter_text.strip().lower() == "roof":
                self.ui.stockHistoryText.setText("Roof Stock History")
            elif filter_text.strip().lower() == "spandrel":
                self.ui.stockHistoryText.setText("Spandrel Stock History")
            elif filter_text.strip().lower() == "gutter":
                self.ui.stockHistoryText.setText("Gutter Stock History")
            elif filter_text.strip().lower() == "others":
                self.ui.stockHistoryText.setText("Other Stock History")
            else:
                self.ui.stockHistoryText.setText("All Stock History")
        except AttributeError as e:
            print(f"ERROR: Missing 'stockHistoryText' label in UI: {e}. Check your Ui_OWNER_STOCKHISTORY.py.")
            self._show_error_message(f"UI label 'stockHistoryText' missing: {e}")
        except Exception as e:
            print(f"An unexpected error occurred updating history label: {e}")


    def load_stock_history(self):
        """Load stock history data based on current filter."""
        if self.history_model is None:
            print("Stock history model is not initialized. Cannot load data.")
            self._show_error_message("Cannot load stock history: Database connection failed during initialization.")
            self.ui.tableWidget_StockHistory.setRowCount(0)
            return

        try:
            # Get the raw text from combobox
            filter_text = self.ui.comboBox_filterStockHistory.currentText().strip()
            print(f"DEBUG: Selected filter text: '{filter_text}'")

            # Map UI filter text to database values
            type_mapping = {
                "    Filter History": None,
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
            self._populate_history_table(history_data or [])

        except Exception as e:
            print(f"Error loading stock history: {e}")
            self._show_error_message(f"Failed to load stock history: {str(e)}")


    def _populate_history_table(self, history_data):
        """Populate the table with history data including product type."""
        try:
            self.ui.tableWidget_StockHistory.setRowCount(0)

            if not history_data:
                print("No stock history data to display.")
                return

            # Update column count and headers to include product type
            self.ui.tableWidget_StockHistory.setColumnCount(7)  # Added one more column
            self.ui.tableWidget_StockHistory.setHorizontalHeaderLabels([
                "User ID",
                "Username",
                "Action",
                "Product Name",
                "Old Qty",
                "New Qty",
                "Updated At"
            ])

            for row_idx, record in enumerate(history_data):
                self.ui.tableWidget_StockHistory.insertRow(row_idx)

                # Get data from record
                user_id = str(record.get('user_id', 'N/A'))
                username = record.get('user_acc_username', 'N/A')
                action_raw = record.get('action_type', 'N/A')
                product_name = record.get('product_name', 'N/A')
                old_qty = str(record.get('old_quantity', 'N/A'))
                new_qty = str(record.get('new_quantity', 'N/A'))
                
                updated_at = record.get('timestamp')
                formatted_updated_at = updated_at.strftime('%Y-%m-%d %H:%M:%S') if updated_at else "N/A"

                # Set items in table
                self.ui.tableWidget_StockHistory.setItem(row_idx, 0, QTableWidgetItem(user_id))
                self.ui.tableWidget_StockHistory.setItem(row_idx, 1, QTableWidgetItem(username))
                self.ui.tableWidget_StockHistory.setItem(row_idx, 2, QTableWidgetItem(action_raw))
                self.ui.tableWidget_StockHistory.setItem(row_idx, 3, QTableWidgetItem(product_name))
                self.ui.tableWidget_StockHistory.setItem(row_idx, 4, QTableWidgetItem(old_qty)) # This is the 5th column, index 4
                self.ui.tableWidget_StockHistory.setItem(row_idx, 5, QTableWidgetItem(new_qty)) # This is the 6th column, index 5
                self.ui.tableWidget_StockHistory.setItem(row_idx, 6, QTableWidgetItem(formatted_updated_at)) # This is the 7th column, index 6

            self.ui.tableWidget_StockHistory.resizeColumnsToContents()

            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) # User ID
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(1, QHeaderView.Interactive) # Username (allows user to resize)
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents) # Action
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(3, QHeaderView.Stretch)       # Product Name (stretches to fill space)
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents) # Old Qty
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents) # New Qty
            self.ui.tableWidget_StockHistory.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents) # Updated At

        except Exception as e:
            print(f"Error populating stock history table: {e}")
            self._show_error_message(f"An error occurred while populating the table: {e}")

    def filter_stock_history(self):
        """Filter the displayed history based on search text entered in the quick search line edit."""
        try:
            search_text = self.ui.lineEdit_OWNER_QuickSearch_StockHistory.text().lower()

            for row in range(self.ui.tableWidget_StockHistory.rowCount()):
                match = False
                for col in range(self.ui.tableWidget_StockHistory.columnCount()):
                    item = self.ui.tableWidget_StockHistory.item(row, col)
                    if item and search_text in item.text().lower():
                        match = True
                        break # Found a match in this row, move to next row

                self.ui.tableWidget_StockHistory.setRowHidden(row, not match)
        except AttributeError as e:
            print(f"ERROR: Missing UI element for search filter: {e}. Check your Ui_OWNER_STOCKHISTORY.py (lineEdit_OWNER_QuickSearch_StockHistory or tableWidget_StockHistory).")
            self._show_error_message(f"Search UI element missing: {e}")
        except Exception as e:
            print(f"An unexpected error occurred during quick search filtering: {e}")
            self._show_error_message(f"An unexpected error occurred during search: {e}")
    
    def log_stock_action(self, product_spec_id, product_id, old_quantity, new_quantity, action_type, product_name, user_acc_id=1):
        """
        Improved version that:
        1. Keeps your working code for add/edit
        2. Handles deletes properly
        3. Matches your database columns
        """
        if self.history_model is None:
            print("WARNING: Cannot log - history model not initialized")
            return False

        try:
            # Convert to integers safely
            old_qty = int(old_quantity) if str(old_quantity).isdigit() else 0
            new_qty = int(new_quantity) if str(new_quantity).isdigit() else 0

            # Use your EXACT column names
            success = self.history_model.add_history_entry(
                shop_id=getattr(self, 'current_user_shop_id', 1),
                user_acc_id=1,
                product_spec_id=product_spec_id,
                product_id=product_id,
                product_name=product_name, # <--- ADD THIS LINE!
                stk_hstry_old_stock_qty=old_qty,
                stk_hstry_new_stock_qty=new_qty,
                stk_hstry_action=action_type.upper(),
                # REMOVE stk_hstry_updated_at="NOW()" entirely, or pass a real datetime object
                # If your database column has a DEFAULT value like CURRENT_TIMESTAMP, just omit it.
                # Otherwise, you would generate a datetime object here:
                # stk_hstry_updated_at=datetime.datetime.now() # Requires `import datetime`
            )
            
            if success:
                print(f"Successfully logged {action_type} action for product {product_id}")
            return success
            
        except Exception as e:
            print(f"Error logging action: {str(e)}")
            return False
    
    def _show_error_message(self, message):
        """Helper to show error messages using QMessageBox"""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.setWindowTitle("Application Error")
        # Ensure a parent widget is passed for QMessageBox. This is a common point of error.
        # If self.ui.tableWidget_StockHistory.parent() is not the main window,
        # you might need to pass the actual main window widget from OwnerController.
        if hasattr(self.ui, 'tableWidget_StockHistory') and self.ui.tableWidget_StockHistory.parent():
             msg.setParent(self.ui.tableWidget_StockHistory.parent())
        elif self.parent: # Fallback to parent if available
             msg.setParent(self.parent)
        else: # Last resort, no parent
             pass 
        msg.exec_()