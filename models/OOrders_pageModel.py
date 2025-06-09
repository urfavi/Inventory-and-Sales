# models/OOrders_pageModel.py
from datetime import datetime, timedelta

class OOrders_pageModel:
    def __init__(self, database_class):
        self.database_class = database_class

    def get_all_orders(self, product_type=None, search_term=None, shop_id=None):
        """
        Fetches order details, filtering by product type, search term, and shop_id.
        If shop_id is None, fetches orders from all shops.
        """
        query = """
            SELECT
                oh.oh_id AS order_id,
                p.product_name AS product,
                od.od_product_price AS price,
                od.od_quantity AS quantity,
                (od.od_product_price * od.od_quantity) AS subtotal,
                od.od_total_amt AS total_amount,
                pt.prod_type_name AS product_type,
                sh.shop_branch_name AS shop_branch_name # Added shop_branch_name alias for consistency
            FROM order_header oh
            JOIN order_detail od ON oh.oh_id = od.oh_id
            JOIN product p ON od.product_id = p.product_id AND od.shop_id = p.shop_id
            JOIN product_type pt ON p.product_type_id = pt.prod_type_id
            JOIN shop sh ON oh.shop_id = sh.shop_id # Join with shop table
            WHERE 1=1
        """
        params = []

        if product_type and product_type != "All Orders": # Ensure this matches your combobox text
            query += " AND pt.prod_type_name = %s"
            params.append(product_type)
        
        if search_term:
            query += " AND (p.product_name ILIKE %s OR oh.oh_id::text ILIKE %s)" # Search by name or order ID
            params.append(f"%{search_term}%")
            params.append(f"%{search_term}%")
        
        # Handle shop_id: If None, no shop filter is applied. Otherwise, filter by shop_id.
        if shop_id is not None:
            query += " AND oh.shop_id = %s"
            params.append(shop_id)

        query += " ORDER BY oh.oh_created_at DESC"

        print(f"Model getting orders - Product Type: {product_type}, Search Term: {search_term}, Shop ID: {shop_id}")
        print(f"Final query:\n {query}")
        print(f"Query params: {params}")

        return self.database_class.fetch_all(query, tuple(params) if params else None)

    def get_all_product_types(self):
        """Fetches all product types."""
        query = "SELECT prod_type_name FROM product_type ORDER BY prod_type_name"
        result = self.database_class.fetch_all(query)
        return [row['prod_type_name'] for row in result] if result else []