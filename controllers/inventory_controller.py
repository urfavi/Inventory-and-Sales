from models.inventory_model import InventoryModel
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

class InventoryController:
    """Controller for inventory operations"""
    
    def __init__(self):
        """Initialize the inventory controller"""
        self.shop_id = 1  # Default shop ID
    
    def get_inventory_by_category(self, category="ALL"):
        """
        Retrieve inventory items by category
        
        Args:
            category (str): Product category (ALL, ROOF, SPANDREL, GUTTER, OTHER)
            
        Returns:
            list: List of inventory items
        """
        try:
            # Get data from database
            if category == "ALL":
                products = InventoryModel.get_all_products()
            else:
                products = InventoryModel.get_products_by_type(category)
                
            # Convert DB result to format expected by UI
            result = []
            for product in products:
                item = {
                    "prod_code": str(product['product_id']),
                    "name": product['product_name'],
                    "description": product['prod_spec_other'] or "",
                    "price": float(product['product_price']),
                    "stock_qty": int(product['prod_spec_stock_qty']),
                    "type": product['prod_type_name'],
                    "length": product['prod_dimension_length_mm'],
                    "width": product['prod_dimension_width_mm'],
                    "color": product['prod_spec_color'],
                    "thickness": product['prod_dimension_thickness_mm'],
                }
                result.append(item)
                
            return result
        except Exception as e:
            print(f"Error retrieving inventory: {str(e)}")
            return []
    
    def search_inventory(self, search_text, category="ALL"):
        """
        Search inventory items by text
        
        Args:
            search_text (str): Text to search for
            category (str): Product category to search in
            
        Returns:
            list: Filtered list of inventory items
        """
        if not search_text:
            return self.get_inventory_by_category(category)
            
        try:
            # Get search results from database
            products = InventoryModel.search_products(search_text)
            
            # Filter by category if needed
            if category != "ALL":
                products = [p for p in products if p['prod_type_name'] == category]
                
            # Convert to expected format
            result = []
            for product in products:
                item = {
                    "prod_code": str(product['product_id']),
                    "name": product['product_name'],
                    "description": product['prod_spec_other'] or "",
                    "price": float(product['product_price']),
                    "stock_qty": int(product['prod_spec_stock_qty']),
                    "type": product['prod_type_name'],
                    "length": product['prod_dimension_length_mm'],
                    "width": product['prod_dimension_width_mm'],
                    "color": product['prod_spec_color'],
                    "thickness": product['prod_dimension_thickness_mm'],
                }
                result.append(item)
                
            return result
        except Exception as e:
            print(f"Error searching inventory: {str(e)}")
            return []
    
    def populate_inventory_table(self, table_widget, items):
        """
        Populate a QTableWidget with inventory items
        
        Args:
            table_widget (QTableWidget): Table to populate
            items (list): Inventory items
            
        Returns:
            None
        """
        try:
            # Clear the table
            table_widget.setRowCount(0)
            
            # Set column headers if needed
            if table_widget.columnCount() == 0:
                table_widget.setColumnCount(6)
                headers = ["ID", "Name", "Type", "Price", "Stock", "Color"]
                table_widget.setHorizontalHeaderLabels(headers)
            
            # Add items to table
            for row, item in enumerate(items):
                table_widget.insertRow(row)
                
                # Set table cells
                table_widget.setItem(row, 0, QTableWidgetItem(str(item['prod_code'])))
                table_widget.setItem(row, 1, QTableWidgetItem(item['name']))
                table_widget.setItem(row, 2, QTableWidgetItem(item['type']))
                table_widget.setItem(row, 3, QTableWidgetItem(str(item['price'])))
                table_widget.setItem(row, 4, QTableWidgetItem(str(item['stock_qty'])))
                table_widget.setItem(row, 5, QTableWidgetItem(item['color']))
        except Exception as e:
            print(f"Error populating inventory table: {str(e)}")
    
    def add_stock(self, category, item_data):
        """
        Add new inventory item
        
        Args:
            category (str): Product category (ROOF, SPANDREL, GUTTER, OTHER)
            item_data (dict): Item data to add
            
        Returns:
            bool: Success status
        """
        try:
            # Extract common data from the dictionary
            name = item_data.get("name", "")
            price = float(item_data.get("price", 0.0))
            stock_qty = int(item_data.get("stock_qty", 0))
            color = item_data.get("color", "")
            description = item_data.get("description", "")
            
            # Ensure numeric values are properly converted
            length = int(item_data.get("length", 0) or 0)
            width = int(item_data.get("width", 0) or 0)
            thickness = int(item_data.get("thickness", 0) or 0)
            
            # Validate data
            if not name:
                raise ValueError("Product name is required")
                
            if price <= 0:
                raise ValueError("Price must be greater than zero")
                
            if stock_qty < 0:
                raise ValueError("Stock quantity cannot be negative")
            
            # Add to database
            product_id = InventoryModel.add_product(
                self.shop_id, category, name, price, stock_qty, 
                color, length, width, thickness, description
            )
            
            if product_id is None:
                raise Exception("Failed to add product")
                
            return True
        except ValueError as e:
            # Value errors are user input errors
            QMessageBox.warning(None, "Input Error", str(e))
            return False
        except Exception as e:
            # Other errors are system errors
            QMessageBox.critical(None, "System Error", f"Error adding inventory item: {str(e)}")
            return False
    
    def update_stock(self, category, product_id, item_data):
        """
        Update inventory item
        
        Args:
            category (str): Product category (ROOF, SPANDREL, GUTTER, OTHER)
            product_id (str): Product ID
            item_data (dict): Updated item data
            
        Returns:
            bool: Success status
        """
        try:
            # Extract data from the dictionary
            name = item_data.get("name")
            price = float(item_data.get("price")) if item_data.get("price") is not None else None
            stock_qty = int(item_data.get("stock_qty")) if item_data.get("stock_qty") is not None else None
            color = item_data.get("color")
            description = item_data.get("description")
            
            # Convert string dimensions to integers if present
            length = int(item_data.get("length")) if item_data.get("length") is not None else None
            width = int(item_data.get("width")) if item_data.get("width") is not None else None
            thickness = int(item_data.get("thickness")) if item_data.get("thickness") is not None else None
            
            # Validate data
            if price is not None and price <= 0:
                raise ValueError("Price must be greater than zero")
                
            if stock_qty is not None and stock_qty < 0:
                raise ValueError("Stock quantity cannot be negative")
            
            # Update in database
            success = InventoryModel.update_product(
                int(product_id), name, price, stock_qty, color,
                length, width, thickness, description
            )
            
            if not success:
                raise Exception(f"Failed to update product {product_id}")
                
            return True
        except ValueError as e:
            # Value errors are user input errors
            QMessageBox.warning(None, "Input Error", str(e))
            return False
        except Exception as e:
            # Other errors are system errors
            QMessageBox.critical(None, "System Error", f"Error updating inventory item: {str(e)}")
            return False
    
    def delete_stock(self, product_id):
        """
        Delete inventory item
        
        Args:
            product_id (str): Product ID to delete
            
        Returns:
            bool: Success status
        """
        try:
            # Convert product_id to integer
            int_product_id = int(product_id)
            
            # Delete from database
            success = InventoryModel.delete_product(int_product_id)
            
            if not success:
                raise Exception(f"Failed to delete product {product_id}")
                
            return True
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error deleting inventory item: {str(e)}")
            return False
    
    def get_low_stock_products(self, threshold=10):
        """
        Get products with low stock
        
        Args:
            threshold (int): Low stock threshold
            
        Returns:
            list: Low stock products
        """
        try:
            return InventoryModel.get_low_stock_products(threshold)
        except Exception as e:
            print(f"Error getting low stock products: {str(e)}")
            return []