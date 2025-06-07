# models/ODashboard_pageModel.py

from models.database import Database
import logging
from datetime import datetime, timedelta 

class DashboardModel:
    LOW_STOCK_THRESHOLD = 20
    
    def __init__(self, database: Database):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        self.database = database
        self.db = database # Alias for convenience
        
        if not self.db.connection:
            self.logger.debug("No active database connection, attempting to connect")
            try:
                self.db.connect()
                self.logger.debug("Created new database connection")
            except Exception as e:
                self.logger.error(f"Failed to connect to database: {e}")
                raise

    def get_total_sales_for_shop(self, shop_id: int, start_date: str = None, end_date: str = None) -> float:
        """
        Fetch total sales for a given shop, optionally within a date range.
        Uses 'order_header' table and 'oh_total_amount'.
        """
        query = """
        SELECT COALESCE(SUM(oh_total_amount), 0.00)
        FROM order_header
        WHERE shop_id = %s
        """
        params = [shop_id]

        if start_date and end_date:
            query += " AND oh_created_at BETWEEN %s AND %s"
            params.extend([start_date, end_date])
        elif start_date:
            query += " AND oh_created_at >= %s"
            params.append(start_date)
        elif end_date:
            query += " AND oh_created_at <= %s"
            params.append(end_date)

        return self._execute_single_value_query(query, "total sales", tuple(params))

    def get_total_orders_for_shop(self, shop_id: int, start_date: str = None, end_date: str = None) -> int:
        """
        Fetch total number of orders for a given shop, optionally within a date range.
        Uses 'order_header' table.
        """
        query = """
        SELECT COALESCE(COUNT(oh_id), 0)
        FROM order_header
        WHERE shop_id = %s
        """
        params = [shop_id]

        if start_date and end_date:
            query += " AND oh_created_at BETWEEN %s AND %s"
            params.extend([start_date, end_date])
        elif start_date:
            query += " AND oh_created_at >= %s"
            params.append(start_date)
        elif end_date:
            query += " AND oh_created_at <= %s"
            params.append(end_date)
        

        return self._execute_single_value_query(query, "total orders", tuple(params))

    def get_best_sellers_data(self, shop_id: int, limit: int = 5, start_date: str = None, end_date: str = None) -> list:
        """
        Fetch best-selling products based on quantity sold for a given shop,
        optionally within a date range.
        Returns a list of dictionaries: [{'product_name': 'X', 'total_quantity_sold': 100}, ...]
        """
        if not isinstance(shop_id, int) or shop_id <= 0:
            self.logger.error(f"Invalid shop_id: {shop_id}")
            return []
        if not isinstance(limit, int) or limit <= 0:
            self.logger.error(f"Invalid limit: {limit}")
            return []

        query = """
        SELECT
            p.product_name,
            COALESCE(SUM(od.od_quantity), 0) as total_quantity_sold
        FROM
            product p
        JOIN
            order_detail od ON p.product_id = od.product_id
        JOIN
            order_header oh ON od.oh_id = oh.oh_id
        WHERE
            p.shop_id = %s
            -- Removed: AND oh.oh_status = 'COMPLETED' as per your request
        """
        params = [shop_id]

        if start_date and end_date:
            query += " AND oh.oh_created_at BETWEEN %s AND %s"
            params.extend([start_date, end_date])
        elif start_date:
            query += " AND oh.oh_created_at >= %s"
            params.append(start_date)
        elif end_date:
            query += " AND oh.oh_created_at <= %s"
            params.append(end_date)

        query += """
        GROUP BY
            p.product_name
        ORDER BY
            total_quantity_sold DESC
        LIMIT %s;
        """
        params.append(limit)
        
        return self._execute_query(query, tuple(params), "best sellers")

    def get_low_stock_products(self, shop_id: int, limit: int = 4) -> list:
        """Fetch products that are low in stock for a specific shop."""
        if not isinstance(shop_id, int) or shop_id <= 0:
            self.logger.error(f"Invalid shop_id: {shop_id}")
            return []
        if not isinstance(limit, int) or limit <= 0:
            self.logger.error(f"Invalid limit: {limit}")
            return []

        query = """
        SELECT
            p.product_name,
            ps.prod_spec_stock_qty
        FROM
            product_specification ps
        JOIN
            product p ON ps.product_id = p.product_id AND ps.shop_id = p.shop_id
        WHERE
            ps.shop_id = %s AND ps.prod_spec_stock_qty < %s
        ORDER BY
            ps.prod_spec_stock_qty ASC
        LIMIT %s;
        """
        return self._execute_query(query, 
                                 (shop_id, self.LOW_STOCK_THRESHOLD, limit), 
                                 "low stock products")
    
    def get_low_stock_count(self, shop_id: int) -> int:
        """Get the TOTAL count of all low-stock items (not limited)"""
        if not isinstance(shop_id, int) or shop_id <= 0:
            self.logger.error(f"Invalid shop_id: {shop_id}")
            return 0

        query = """
        SELECT COUNT(*)
        FROM product_specification ps
        JOIN product p ON ps.product_id = p.product_id AND ps.shop_id = p.shop_id
        WHERE ps.shop_id = %s AND ps.prod_spec_stock_qty < %s;
        """
        return self._execute_single_value_query(
            query, 
            "total low stock count", 
            (shop_id, self.LOW_STOCK_THRESHOLD)
        )

    def _execute_single_value_query(self, query: str, description: str, params: tuple = None):
        """
        Execute a query that returns a single value (e.g., SUM, COUNT).
        Handles various return types (int, float) and defaults to 0 on error/None.
        """
        self.logger.debug(f"Fetching {description} with params: {params}")
        try:
            raw_result = self.db.fetch_one(query, params) if params else self.db.fetch_one(query)
            
            value = 0.0 # Default to float 0.0 for sums, will convert to int for counts if applicable
            if raw_result is not None:
                if isinstance(raw_result, (tuple, list)):
                    if raw_result and raw_result[0] is not None:
                        try:
                            value = float(raw_result[0])
                        except (ValueError, TypeError):
                            self.logger.warning(f"Could not convert raw_result '{raw_result[0]}' to float for {description}. Defaulting to 0.0.")
                            value = 0.0
                elif isinstance(raw_result, dict):
                    if raw_result:
                        first_key = next(iter(raw_result), None)
                        if first_key is not None and raw_result[first_key] is not None:
                            try:
                                value = float(raw_result[first_key])
                            except (ValueError, TypeError):
                                self.logger.warning(f"Could not convert dict value '{raw_result[first_key]}' to float for {description}. Defaulting to 0.0.")
                                value = 0.0
                        else:
                            self.logger.warning(f"Dictionary result for {description} was empty or contained None value: {raw_result}. Defaulting to 0.0.")
                    else:
                        self.logger.warning(f"Empty dictionary result for {description}. Defaulting to 0.0.")
                else:
                    try:
                        value = float(raw_result)
                    except (ValueError, TypeError):
                        self.logger.warning(f"Could not convert raw_result '{raw_result}' to float for {description}. Defaulting to 0.0.")
                        value = 0.0
            
            self.logger.debug(f"Fetched {description}: {value}")
            if "count" in description.lower() or "orders" in description.lower():
                 return int(value)
            return value
        except Exception as e:
            self.logger.error(f"Error fetching {description}: {e}", exc_info=True)
            if "count" in description.lower() or "orders" in description.lower():
                return 0
            return 0.0 

    def _execute_query(self, query: str, params: tuple, description: str):
        """Execute a query that returns multiple rows (list of dicts/tuples)."""
        self.logger.debug(f"Fetching {description} with params: {params}")
        try:
            return self.db.fetch_all(query, params) or []
        except Exception as e:
            self.logger.error(f"Error fetching {description}: {e}", exc_info=True)
            return []