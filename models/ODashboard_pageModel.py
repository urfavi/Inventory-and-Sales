from models.database import Database
import logging

class DashboardModel:
    LOW_STOCK_THRESHOLD = 20

    def __init__(self, database_connection):
        self.db = database_connection # This is the Database instance
        print("DEBUG: DashboardModel initialized with database connection.")
        # It's good practice to initialize logger if you use self.logger.debug
        self.logger = logging.getLogger(__name__)


    def get_today_sales(self, shop_id):
        # Query for total sales amount from order_detail for today
        # Summing od_total_amt from order_detail via join
        query = """
        SELECT COALESCE(SUM(od.od_total_amt), 0.00)
        FROM order_header oh
        JOIN order_detail od ON oh.oh_id = od.oh_id AND oh.shop_id = od.shop_id
        WHERE oh.shop_id = %s AND DATE(oh.oh_created_at) = CURRENT_DATE;
        """
        result = self.db.fetch_one(query, (shop_id,))
        print(f"DEBUG: get_today_sales result for shop {shop_id}: {result}")
        # Assuming fetch_one returns a dict like {'coalesce': value} or a tuple (value,)
        if isinstance(result, dict) and 'coalesce' in result:
            return result['coalesce'] if result['coalesce'] is not None else 0.0
        elif isinstance(result, (tuple, list)) and len(result) > 0:
            return result[0] if result[0] is not None else 0.0
        return 0.0


    def get_today_orders(self, shop_id):
        # Query for total number of orders from order_header for today
        query = """
        SELECT COALESCE(COUNT(oh.oh_id), 0)
        FROM order_header oh
        WHERE oh.shop_id = %s AND DATE(oh.oh_created_at) = CURRENT_DATE;
        """
        result = self.db.fetch_one(query, (shop_id,))
        print(f"DEBUG: get_today_orders result for shop {shop_id}: {result}")
        # Assuming fetch_one returns a dict like {'coalesce': value} or a tuple (value,)
        if isinstance(result, dict) and 'coalesce' in result:
            return result['coalesce'] if result['coalesce'] is not None else 0
        elif isinstance(result, (tuple, list)) and len(result) > 0:
            return result[0] if result[0] is not None else 0
        return 0


    def get_today_revenue(self, shop_id):
        # This will be the same as get_today_sales, as "Today's Revenue" and "Today's Sales"
        # usually refer to the same sum of money for a single day in a dashboard context.
        query = """
        SELECT COALESCE(SUM(od.od_total_amt), 0.00)
        FROM order_header oh
        JOIN order_detail od ON oh.oh_id = od.oh_id AND oh.shop_id = od.shop_id
        WHERE oh.shop_id = %s AND DATE(oh.oh_created_at) = CURRENT_DATE;
        """
        result = self.db.fetch_one(query, (shop_id,))
        print(f"DEBUG: get_today_revenue result for shop {shop_id}: {result}")
        # Assuming fetch_one returns a dict like {'coalesce': value} or a tuple (value,)
        if isinstance(result, dict) and 'coalesce' in result:
            return result['coalesce'] if result['coalesce'] is not None else 0.0
        elif isinstance(result, (tuple, list)) and len(result) > 0:
            return result[0] if result[0] is not None else 0.0
        return 0.0
    
    def get_best_sellers(self, shop_id): # Renamed and added shop_id
        query = """
        SELECT p.product_name, SUM(od.od_quantity) AS total_quantity
        FROM order_detail od
        JOIN order_header oh ON od.oh_id = oh.oh_id AND od.shop_id = oh.shop_id
        JOIN product p ON od.product_id = p.product_id
        WHERE oh.shop_id = %s
        AND oh.oh_created_at >= CURRENT_DATE - INTERVAL '7 days' -- Assuming last 7 days for best sellers
        GROUP BY p.product_name
        ORDER BY total_quantity DESC
        LIMIT 5;
        """
        # Ensure the execute_query method returns dictionaries if that's what your chart expects
        # If it returns tuples, you'll need to adjust `items` and `sales` extraction in the chart code.
        result = self.db.fetch_all(query, (shop_id,)) # Assuming fetch_all returns list of dicts

        # Debug print
        print(f"DEBUG: get_best_sellers query result: {result}")

        return result


    def get_low_stock_products(self, shop_id: int, limit: int = 4):
        if not isinstance(shop_id, int) or shop_id <= 0:
            raise ValueError("shop_id must be a positive integer")
        if not isinstance(limit, int) or limit <= 0:
            raise ValueError("limit must be a positive integer")
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
        return self._execute_query(query, (shop_id, self.LOW_STOCK_THRESHOLD, limit), "low stock products")

    def get_low_stock_count(self, shop_id: int) -> int:
        if not isinstance(shop_id, int) or shop_id <= 0:
            raise ValueError("shop_id must be a positive integer")
        query = """
        SELECT COUNT(*)
        FROM product_specification ps
        JOIN product p ON ps.product_id = p.product_id AND ps.shop_id = p.shop_id
        WHERE ps.shop_id = %s AND ps.prod_spec_stock_qty < %s;
        """
        return self._execute_single_value_query(query, "total low stock count", (shop_id, self.LOW_STOCK_THRESHOLD))

    def _execute_single_value_query(self, query: str, description: str, params: tuple = None):
        # Added a logger initialization to prevent potential AttributeError if logger is not set
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Fetching {description} with params: {params}")
        try:
            raw_result = self.db.fetch_one(query, params) if params else self.db.fetch_one(query)
            value = 0
            if raw_result is not None:
                if isinstance(raw_result, (tuple, list)):
                    if raw_result and raw_result[0] is not None:
                        value = int(raw_result[0])
                elif isinstance(raw_result, dict):
                    # For a COUNT(*) or SUM() query, the key might be 'count' or 'sum'
                    # or it might be the column alias if specified (e.g., AS total_count)
                    # For COALESCE(SUM(od.od_total_amt), 0.00), the default key might be 'coalesce'
                    if 'coalesce' in raw_result and raw_result['coalesce'] is not None:
                        value = raw_result['coalesce'] # Keep as float for sales/revenue
                    elif 'count' in raw_result and raw_result['count'] is not None:
                        value = raw_result['count'] # Keep as int for count
                    elif len(raw_result) == 1: # If it's a dict with one key, use its value
                        value = list(raw_result.values())[0]
                    else:
                        self.logger.warning(f"Dictionary result for {description} did not contain expected keys ('coalesce', 'count') or its value was None: {raw_result}. Defaulting to 0.")
                else:
                    try:
                        # Attempt to convert directly if it's a single value returned directly (e.g., from fetch_one returning a scalar)
                        value = raw_result
                    except (ValueError, TypeError):
                        self.logger.warning(f"Could not convert raw_result '{raw_result}' to numerical type for {description}. Defaulting to 0.")
                        value = 0
            self.logger.debug(f"Fetched {description}: {value}")
            return value
        except Exception as e:
            self.logger.error(f"Error fetching {description}: {e}", exc_info=True)
            return 0.0 if "sales" in description or "revenue" in description else 0 # Return 0.0 for money, 0 for count


    def _execute_query(self, query: str, params: tuple, description: str):
        # Added a logger initialization to prevent potential AttributeError if logger is not set
        if not hasattr(self, 'logger'):
            self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Fetching {description} with params: {params}")
        try:
            return self.db.fetch_all(query, params) or []
        except Exception as e:
            self.logger.error(f"Error fetching {description}: {e}")
            return []