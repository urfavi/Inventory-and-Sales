from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from models.database import Database
from models.OInventory_pageModel import InventoryModel

class InventoryController:
    def __init__(self, ui):
        self.ui = ui
        self.db = Database()
        self.model = InventoryModel(self.db)
        
        self.current_product = None
        self.setup_ui()
        
    def setup_ui(self):
        """Initialize all UI components"""
        self.setup_validators()
        self.setup_tables()
        self.setup_connections()
        self.load_initial_data()
        
    def setup_validators(self):
        """Set up input validators for all fields"""
        # Price validators (decimal)
        price_validator = QtGui.QDoubleValidator(0.01, 999999, 2)
        for widget in self.ui.findChildren(QtWidgets.QLineEdit, QtCore.QRegExp(".*Price")):
            widget.setValidator(price_validator)
            widget.editingFinished.connect(lambda w=widget: self.format_price(w))
        
        # Quantity validators (integer >=11)
        qty_validator = QtGui.QIntValidator(11, 999999)
        for widget in self.ui.findChildren(QtWidgets.QLineEdit, QtCore.QRegExp(".*Qty")):
            widget.setValidator(qty_validator)
        
        # Color validators (letters only)
        color_validator = QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("^[A-Za-z ]+$"))
        for widget in self.ui.findChildren(QtWidgets.QLineEdit, QtCore.QRegExp(".*Color")):
            widget.setValidator(color_validator)
        
        # Auto-capitalize text fields
        for widget in self.ui.findChildren((QtWidgets.QLineEdit, QtWidgets.QTextEdit)):
            if widget.objectName() not in ["lineEdit_Search"]:  # Exclude search
                widget.editingFinished.connect(lambda w=widget: self.auto_capitalize(w))
    
    def setup_tables(self):
        """Configure all tables with common settings"""
        tables = [
            self.ui.tableWidget_ALL_ITEMS,
            self.ui.tableWidget_ROOF,
            self.ui.tableWidget_SPANDREL,
            self.ui.tableWidget_GUTTER,
            self.ui.tableWidget_OTHER
        ]
        
        for table in tables:
            table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
            table.itemSelectionChanged.connect(self.handle_selection)
    
    def setup_connections(self):
        """Connect all signals to slots"""
        # View buttons
        self.ui.pushButton_Inventory_ALL_ITEMS_table.clicked.connect(self.show_all_items)
        self.ui.pushButton_Inventory_ROOF_table.clicked.connect(self.show_roof_items)
        self.ui.pushButton_Inventory_SPANDREL_table.clicked.connect(self.show_spandrel_items)
        self.ui.pushButton_Inventory_GUTTER_table.clicked.connect(self.show_gutter_items)
        self.ui.pushButton_Inventory_OTHER_table.clicked.connect(self.show_other_items)
        
        # Action buttons
        self.ui.pushButton_OWNER_Add_Inventory.clicked.connect(self.show_add_form)
        self.ui.pushButton_OWNER_Edit_Inventory.clicked.connect(self.show_edit_form)
        self.ui.pushButton_OWNER_Delete_Inventory.clicked.connect(self.show_delete_form)
        
        # Add form
        self.ui.comboBox_Select_Prod_Type_toAdd.currentIndexChanged.connect(self.switch_add_form)
        self.ui.pushButton_Confirm_ROOFadd.clicked.connect(lambda: self.add_product("ROOF"))
        # ... connect other confirm buttons similarly
        
        # Edit form
        self.ui.comboBox_Select_Prod_Type_toEdit.currentIndexChanged.connect(self.switch_edit_form)
        self.ui.pushButton_Save_ROOFedit.clicked.connect(lambda: self.update_product("ROOF"))
        # ... connect other save buttons similarly
        
        # Delete form
        self.ui.comboBox_Select_Prod_Type_toDelete.currentIndexChanged.connect(self.switch_delete_form)
        self.ui.pushButton_Confirm_ROOFdelete.clicked.connect(lambda: self.delete_product("ROOF"))
        # ... connect other delete buttons similarly
    
    # -------------------- Core Methods --------------------
    
    def load_initial_data(self):
        """Load initial data when controller starts"""
        self.show_all_items()
        self.update_source_labels()
    
    def update_source_labels(self):
        """Update source labels for all product types"""
        for prod_type in ["ROOF", "SPANDREL", "GUTTER", "OTHER"]:
            label = getattr(self.ui, f"sourceLabel{prod_type.capitalize()}", None)
            if label:
                label.setText(self.model.get_product_source(prod_type) or "N/A")
    
    def get_current_form_data(self, form_type, product_type):
        """Extract data from the specified form"""
        prefix = f"{form_type}_{product_type}"
        fields = {
            "name": f"lineEdit_{prefix}_Name",
            "price": f"lineEdit_{prefix}_Price",
            "qty": f"lineEdit_{prefix}_Qty",
            "color": f"lineEdit_{prefix}_Color",
            "length": f"lineEdit_{prefix}_Length",
            "thickness": f"lineEdit_{prefix}_Thickness",
            "width": f"lineEdit_{prefix}_Width",
            "other": f"lineEdit_{prefix}_OtherSpecifications"
        }
        
        data = {}
        for field, widget_name in fields.items():
            widget = getattr(self.ui, widget_name, None)
            if widget:
                value = widget.text().strip() if isinstance(widget, QtWidgets.QLineEdit) else widget.toPlainText().strip()
                data[field] = value if value else None
        
        # Convert price and quantities to numbers
        try:
            data["price"] = float(data["price"].replace("₱", "").replace(",", "")) if data.get("price") else 0
            data["qty"] = int(data["qty"]) if data.get("qty") else 0
        except ValueError:
            pass
            
        return data
    
    def validate_product_data(self, data):
        """Validate product data before saving"""
        errors = []
        if not data.get("name"):
            errors.append("Product name is required")
        if not data.get("price") or data["price"] <= 0:
            errors.append("Price must be greater than 0")
        if not data.get("qty") or data["qty"] < 11:
            errors.append("Quantity must be at least 11")
        
        return errors
    
    # -------------------- Product CRUD Operations --------------------
    
    def add_product(self, product_type):
        """Add new product to inventory"""
        data = self.get_current_form_data("Add", product_type)
        errors = self.validate_product_data(data)
        
        if errors:
            self.show_error("\n".join(errors))
            return
        
        try:
            product_id = self.model.add_product(
                product_type=product_type,
                name=data["name"],
                price=data["price"],
                qty=data["qty"],
                color=data["color"],
                length=data["length"],
                thickness=data["thickness"],
                width=data["width"],
                other=data["other"],
                source="J&J FACTORY-MOALBOAL"
            )
            
            if product_id:
                self.show_success(f"{product_type} product added successfully!")
                self.clear_add_form()
                self.show_all_items()
            else:
                self.show_error("Failed to add product to database")
                
        except Exception as e:
            self.show_error(f"Error adding product: {str(e)}")
    
    def update_product(self, product_type):
        """Update existing product"""
        if not self.current_product:
            self.show_error("No product selected for editing")
            return
            
        data = self.get_current_form_data("Edit", product_type)
        errors = self.validate_product_data(data)
        
        if errors:
            self.show_error("\n".join(errors))
            return
        
        try:
            success = self.model.update_product(
                product_id=self.current_product["id"],
                name=data["name"],
                price=data["price"],
                qty=data["qty"],
                color=data["color"],
                length=data["length"],
                thickness=data["thickness"],
                width=data["width"],
                other=data["other"]
            )
            
            if success:
                self.show_success(f"{product_type} product updated successfully!")
                self.clear_edit_form()
                self.show_all_items()
            else:
                self.show_error("Failed to update product in database")
                
        except Exception as e:
            self.show_error(f"Error updating product: {str(e)}")
    
    def delete_product(self, product_type):
        """Delete product from inventory"""
        if not self.current_product:
            self.show_error("No product selected for deletion")
            return
            
        reply = QMessageBox.question(
            None, "Confirm Delete",
            f"Are you sure you want to delete {self.current_product['name']}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                success = self.model.delete_product(self.current_product["id"])
                if success:
                    self.show_success(f"{product_type} product deleted successfully!")
                    self.clear_delete_form()
                    self.show_all_items()
                else:
                    self.show_error("Failed to delete product from database")
                    
            except Exception as e:
                self.show_error(f"Error deleting product: {str(e)}")
    
    # -------------------- Form Management --------------------
    
    def clear_add_form(self):
        """Clear all add form fields"""
        for widget in self.ui.findChildren(QtWidgets.QLineEdit, QtCore.QRegExp("Add_.*")):
            widget.clear()
        self.ui.comboBox_Select_Prod_Type_toAdd.setCurrentIndex(0)
    
    def clear_edit_form(self):
        """Clear all edit form fields"""
        for widget in self.ui.findChildren(QtWidgets.QLineEdit, QtCore.QRegExp("Edit_.*")):
            widget.clear()
        self.ui.comboBox_Select_Prod_Type_toEdit.setCurrentIndex(0)
        self.current_product = None
    
    def clear_delete_form(self):
        """Clear delete form"""
        self.ui.comboBox_Select_Prod_Type_toDelete.setCurrentIndex(0)
        self.current_product = None
    
    # -------------------- View Management --------------------
    
    def show_all_items(self):
        """Show all products in inventory"""
        self.load_table(self.ui.tableWidget_ALL_ITEMS, self.model.get_all_products())
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(0)
        self.set_active_button(self.ui.pushButton_Inventory_ALL_ITEMS_table)
    
    def show_roof_items(self):
        """Show only roof products"""
        self.load_table(self.ui.tableWidget_ROOF, self.model.get_products_by_type("ROOF"))
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(1)
        self.set_active_button(self.ui.pushButton_Inventory_ROOF_table)
    
    # ... similar methods for other product types
    
    def load_table(self, table, data):
        """Load data into specified table"""
        table.setRowCount(0)
        for row_idx, row_data in enumerate(data):
            table.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                
                # Format price column
                if col_idx == 3 and isinstance(value, (int, float)):
                    item.setText(f"₱{value:,.2f}")
                    item.setData(QtCore.Qt.UserRole, value)  # For sorting
                
                table.setItem(row_idx, col_idx, item)
    
    # -------------------- Helper Methods --------------------
    
    def handle_selection(self):
        """Handle product selection from any table"""
        sender = self.sender()
        if sender and sender.selectedItems():
            product_id = sender.selectedItems()[0].text()
            self.current_product = self.model.get_product(product_id)
    
    def format_price(self, widget):
        """Format price with peso symbol"""
        text = widget.text()
        if text and not text.startswith('₱'):
            widget.setText(f'₱{text}')
    
    def auto_capitalize(self, widget):
        """Auto-capitalize the first letter of text fields"""
        if isinstance(widget, QtWidgets.QLineEdit):
            text = widget.text()
            if text:
                widget.setText(text[0].upper() + text[1:])
        elif isinstance(widget, QtWidgets.QTextEdit):
            text = widget.toPlainText()
            if text:
                widget.setPlainText(text[0].upper() + text[1:])
    
    def set_active_button(self, button):
        """Set active button style"""
        for btn in self.table_view_buttons + self.action_buttons:
            btn.setProperty('class', '')
            btn.style().unpolish(btn)
            btn.style().polish(btn)
        
        button.setProperty('class', 'activeButton')
        button.style().unpolish(button)
        button.style().polish(button)
    
    def show_error(self, message):
        """Show error message"""
        QMessageBox.critical(None, "Error", message)
    
    def show_success(self, message):
        """Show success message"""
        QMessageBox.information(None, "Success", message)