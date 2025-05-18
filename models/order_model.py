from models.database import Database
import psycopg2.extras
from datetime import datetime, timedelta

class OrderModel:
    """Model for order-related database operations"""
    
    @staticmethod
    def get_all_orders():
        """
        Get all orders
        
        Returns:
            list: Orders list
        """
        try:
            query = """
            SELECT o.order_id, o.order_date, o.order_total, o.order_status,
                   u.user_acc_username, u.user_acc_name
            FROM orders o
            JOIN user_account u ON o.user_acc_id = u.user_acc_id
            ORDER BY o.order_date DESC
            """
            
            result = Database.execute_query(query)
            return result
        except Exception as e:
            print(f"Get orders error: {str(e)}")
            return []
    
    @staticmethod
    def get_order_details(order_id):
        """
        Get order details including items
        
        Args:
            order_id (int): Order ID
            
        Returns:
            dict: Order information with items
        """
        conn = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            # Get order header information
            cursor.execute("""
                SELECT o.order_id, o.order_date, o.order_total, o.order_status,
                       u.user_acc_username, u.user_acc_name
                FROM orders o
                JOIN user_account u ON o.user_acc_id = u.user_acc_id
                WHERE o.order_id = %s
            """, (order_id,))
            
            order_info = cursor.fetchone()
            if not order_info:
                return None
                
            # Get order items
            cursor.execute("""
                SELECT oi.order_item_id, oi.order_item_qty, oi.order_item_price,
                       p.product_id, p.product_name, 
                       pt.prod_type_name, ps.prod_spec_color
                FROM order_item oi
                JOIN product p ON oi.product_id = p.product_id
                JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
                JOIN product_specification ps ON p.product_id = ps.product_id
                WHERE oi.order_id = %s
            """, (order_id,))
            
            items = cursor.fetchall()
            
            # Convert to dictionary with items
            order_dict = dict(order_info)
            order_dict['items'] = [dict(item) for item in items]
            
            return order_dict
            
        except Exception as e:
            print(f"Get order details error: {str(e)}")
            return None
        finally:
            if conn:
                Database.release_connection(conn)
    
    @staticmethod
    def create_order(user_id, items):
        """
        Create a new order
        
        Args:
            user_id (int): User ID
            items (list): List of dicts with product_id, qty, price
            
        Returns:
            int or None: New order ID if successful, None otherwise
        """
        conn = None
        try:
            conn = Database.get_connection()
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            
            # Start transaction
            conn.autocommit = False
            
            # Calculate total
            total = sum(item['qty'] * item['price'] for item in items)
            
            # Insert order header
            cursor.execute("""
                INSERT INTO orders (user_acc_id, order_date, order_total, order_status)
                VALUES (%s, NOW(), %s, 'PENDING')
                RETURNING order_id
            """, (user_id, total))
            
            order_id = cursor.fetchone()['order_id']
            
            # Insert order items
            for item in items:
                cursor.execute("""
                    INSERT INTO order_item (order_id, product_id, order_item_qty, order_item_price)
                    VALUES (%s, %s, %s, %s)
                """, (order_id, item['product_id'], item['qty'], item['price']))
                
                # Update inventory quantities
                cursor.execute("""
                    UPDATE product_specification
                    SET prod_spec_stock_qty = prod_spec_stock_qty - %s,
                        prod_spec_updated_at = NOW()
                    WHERE product_id = %s
                """, (item['qty'], item['product_id']))
            
            # Commit transaction
            conn.commit()
            return order_id
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Create order error: {str(e)}")
            return None
        finally:
            if conn:
                conn.autocommit = True
                Database.release_connection(conn)
    
    @staticmethod
    def update_order_status(order_id, status):
        """
        Update order status
        
        Args:
            order_id (int): Order ID
            status (str): New status (PENDING, COMPLETED, CANCELLED)
            
        Returns:
            bool: Success status
        """
        try:
            query = """
            UPDATE orders
            SET order_status = %s
            WHERE order_id = %s
            """
            
            result = Database.execute_query(query, (status, order_id))
            return result > 0
        except Exception as e:
            print(f"Update order status error: {str(e)}")
            return False
    
    @staticmethod
    def get_recent_orders(limit=10):
        """
        Get recent orders
        
        Args:
            limit (int): Maximum number of orders to return
            
        Returns:
            list: Recent orders
        """
        try:
            query = """
            SELECT o.order_id, o.order_date, o.order_total, o.order_status,
                   u.user_acc_username, u.user_acc_name
            FROM orders o
            JOIN user_account u ON o.user_acc_id = u.user_acc_id
            ORDER BY o.order_date DESC
            LIMIT %s
            """
            
            result = Database.execute_query(query, (limit,))
            return result
        except Exception as e:
            print(f"Get recent orders error: {str(e)}")
            return []
    
    @staticmethod
    def get_sales_by_period(period='daily'):
        """
        Get sales totals by period
        
        Args:
            period (str): Period type (daily, weekly, monthly)
            
        Returns:
            list: Sales totals
        """
        try:
            # Define date range based on period
            if period == 'daily':
                # Last 7 days, grouped by day
                query = """
                SELECT DATE(order_date) as sale_date,
                       SUM(order_total) as total_sales,
                       COUNT(*) as order_count
                FROM orders
                WHERE order_status = 'COMPLETED'
                  AND order_date >= NOW() - INTERVAL '7 days'
                GROUP BY DATE(order_date)
                ORDER BY sale_date DESC
                """
                
            elif period == 'weekly':
                # Last 4 weeks, grouped by week
                query = """
                SELECT DATE_TRUNC('week', order_date) as sale_week,
                       SUM(order_total) as total_sales,
                       COUNT(*) as order_count
                FROM orders
                WHERE order_status = 'COMPLETED'
                  AND order_date >= NOW() - INTERVAL '4 weeks'
                GROUP BY DATE_TRUNC('week', order_date)
                ORDER BY sale_week DESC
                """
                
            elif period == 'monthly':
                # Last 6 months, grouped by month
                query = """
                SELECT DATE_TRUNC('month', order_date) as sale_month,
                       SUM(order_total) as total_sales,
                       COUNT(*) as order_count
                FROM orders
                WHERE order_status = 'COMPLETED'
                  AND order_date >= NOW() - INTERVAL '6 months'
                GROUP BY DATE_TRUNC('month', order_date)
                ORDER BY sale_month DESC
                """
                
            else:
                # Default to all time
                query = """
                SELECT SUM(order_total) as total_sales,
                       COUNT(*) as order_count
                FROM orders
                WHERE order_status = 'COMPLETED'
                """
            
            result = Database.execute_query(query)
            return result
        except Exception as e:
            print(f"Get sales by period error: {str(e)}")
            return []
    
    @staticmethod
    def get_sales_by_product_type(product_type=None, period='all'):
        """
        Get sales by product type
        
        Args:
            product_type (str, optional): Product type name. If None, returns all types.
            period (str): Period type (all, daily, weekly, monthly)
            
        Returns:
            list: Sales by product type
        """
        try:
            date_filter = ""
            if period == 'daily':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '1 day'"
            elif period == 'weekly':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '7 days'"
            elif period == 'monthly':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '30 days'"
            
            type_filter = ""
            if product_type:
                type_filter = " AND pt.prod_type_name = %s"
            
            query = f"""
            SELECT pt.prod_type_name,
                   SUM(oi.order_item_price * oi.order_item_qty) as total_sales,
                   SUM(oi.order_item_qty) as total_qty
            FROM order_item oi
            JOIN orders o ON oi.order_id = o.order_id
            JOIN product p ON oi.product_id = p.product_id
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            WHERE o.order_status = 'COMPLETED'
            {date_filter}
            {type_filter}
            GROUP BY pt.prod_type_name
            ORDER BY total_sales DESC
            """
            
            result = Database.execute_query(query, (product_type,) if product_type else None)
            return result
        except Exception as e:
            print(f"Get sales by product type error: {str(e)}")
            return []
    
    @staticmethod
    def get_best_selling_products(limit=10, period='all'):
        """
        Get best selling products
        
        Args:
            limit (int): Maximum number of products to return
            period (str): Period type (all, daily, weekly, monthly)
            
        Returns:
            list: Best selling products
        """
        try:
            date_filter = ""
            if period == 'daily':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '1 day'"
            elif period == 'weekly':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '7 days'"
            elif period == 'monthly':
                date_filter = " AND o.order_date >= NOW() - INTERVAL '30 days'"
            
            query = f"""
            SELECT p.product_id, p.product_name, pt.prod_type_name,
                   SUM(oi.order_item_qty) as total_qty,
                   SUM(oi.order_item_price * oi.order_item_qty) as total_sales
            FROM order_item oi
            JOIN orders o ON oi.order_id = o.order_id
            JOIN product p ON oi.product_id = p.product_id
            JOIN product_type pt ON p.prod_type_id = pt.prod_type_id
            WHERE o.order_status = 'COMPLETED'
            {date_filter}
            GROUP BY p.product_id, p.product_name, pt.prod_type_name
            ORDER BY total_qty DESC
            LIMIT %s
            """
            
            result = Database.execute_query(query, (limit,))
            return result
        except Exception as e:
            print(f"Get best selling products error: {str(e)}")
            return []