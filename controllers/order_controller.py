from models.order_model import OrderModel
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

class OrderController:
    """Controller for order operations"""
    
    def __init__(self):
        """Initialize the order controller"""
        pass
    
    def get_all_orders(self):
        """
        Get all orders
        
        Returns:
            list: Orders list
        """
        try:
            return OrderModel.get_all_orders()
        except Exception as e:
            print(f"Error retrieving orders: {str(e)}")
            return []
    
    def get_order_details(self, order_id):
        """
        Get detailed order information
        
        Args:
            order_id (int): Order ID
            
        Returns:
            dict: Order details
        """
        try:
            return OrderModel.get_order_details(order_id)
        except Exception as e:
            print(f"Error retrieving order details: {str(e)}")
            return None
    
    def create_new_order(self, user_id, items):
        """
        Create a new order
        
        Args:
            user_id (int): User ID
            items (list): List of dictionaries with product_id, qty, price
            
        Returns:
            int or None: New order ID if successful
        """
        try:
            # Validate input
            if not items:
                raise ValueError("No items in order")
                
            # Create order in database
            order_id = OrderModel.create_order(user_id, items)
            
            if not order_id:
                raise Exception("Failed to create order")
                
            return order_id
        except ValueError as e:
            # User input errors
            QMessageBox.warning(None, "Input Error", str(e))
            return None
        except Exception as e:
            # System errors
            QMessageBox.critical(None, "System Error", f"Error creating order: {str(e)}")
            return None
    
    def update_order_status(self, order_id, status):
        """
        Update order status
        
        Args:
            order_id (int): Order ID
            status (str): New status (PENDING, COMPLETED, CANCELLED)
            
        Returns:
            bool: Success status
        """
        try:
            return OrderModel.update_order_status(order_id, status)
        except Exception as e:
            print(f"Error updating order status: {str(e)}")
            return False
    
    def get_recent_orders(self, limit=10):
        """
        Get recent orders for dashboard
        
        Args:
            limit (int): Maximum number of orders to return
            
        Returns:
            list: Recent orders
        """
        try:
            return OrderModel.get_recent_orders(limit)
        except Exception as e:
            print(f"Error retrieving recent orders: {str(e)}")
            return []
            
    def populate_orders_table(self, table_widget, orders):
        """
        Populate a QTableWidget with orders
        
        Args:
            table_widget (QTableWidget): Table to populate
            orders (list): Order list
            
        Returns:
            None
        """
        try:
            # Clear the table
            table_widget.setRowCount(0)
            
            # Set column headers if needed
            if table_widget.columnCount() == 0:
                table_widget.setColumnCount(5)
                headers = ["Order ID", "Date", "Cashier", "Total", "Status"]
                table_widget.setHorizontalHeaderLabels(headers)
            
            # Add items to table
            for row, order in enumerate(orders):
                table_widget.insertRow(row)
                
                # Set table cells
                table_widget.setItem(row, 0, QTableWidgetItem(str(order['order_id'])))
                
                # Format date nicely
                date_str = order['order_date'].strftime("%Y-%m-%d %H:%M")
                table_widget.setItem(row, 1, QTableWidgetItem(date_str))
                
                table_widget.setItem(row, 2, QTableWidgetItem(order['user_acc_name']))
                table_widget.setItem(row, 3, QTableWidgetItem(f"₱{order['order_total']:.2f}"))
                table_widget.setItem(row, 4, QTableWidgetItem(order['order_status']))
                
        except Exception as e:
            print(f"Error populating orders table: {str(e)}")