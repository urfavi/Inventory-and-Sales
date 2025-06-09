# models/OSales_pageModel.py
from datetime import datetime, timedelta

class OSales_pageModel:
    def __init__(self, database_class):
        self.database_class = database_class

    def get_sales_summary_data(self, filter_type, shop_id=None):
        """
        Fetch sales summary data from order_header and receipt tables.
        If shop_id is None, fetches from all shops.
        """
        date_condition = self._get_date_condition(filter_type, "oh.oh_created_at")
        shop_condition = ""
        params = []

        if shop_id is not None:
            shop_condition = " AND oh.shop_id = %s"
            params.append(shop_id)

        query = f"""
        SELECT
            oh.oh_id as report_id,
            sh.shop_branch_name,
            SUM(od.od_quantity) as total_quantity,
            SUM(od.od_total_amt) as total_revenue,
            MAX(oh.oh_created_at) as report_date
        FROM order_header oh
        JOIN order_detail od ON oh.oh_id = od.oh_id
        JOIN shop sh ON oh.shop_id = sh.shop_id
        WHERE {date_condition} {shop_condition}
        GROUP BY oh.oh_id, sh.shop_branch_name
        ORDER BY report_date DESC
        """
        print(f"Sales Summary Query: {query} with params: {params}") # Debug
        return self.database_class.fetch_all(query, tuple(params) if params else None)

    def get_order_details_data(self, filter_type, shop_id=None):
        """
        Fetch order details data from order_detail table.
        If shop_id is None, fetches from all shops.
        """
        date_condition = self._get_date_condition(filter_type, "oh.oh_created_at")
        shop_condition = ""
        params = []

        if shop_id is not None:
            shop_condition = " AND oh.shop_id = %s"
            params.append(shop_id)

        query = f"""
        SELECT
            od.od_id as detail_id,
            p.product_name,
            od.od_quantity as quantity_sold,
            od.od_total_amt as total_sales,
            od.od_created_at as date_recorded,
            sh.shop_branch_name # Added shop_branch_name to details
        FROM order_detail od
        JOIN product p ON od.product_id = p.product_id AND od.shop_id = p.shop_id
        JOIN order_header oh ON od.oh_id = oh.oh_id
        JOIN shop sh ON oh.shop_id = sh.shop_id # Join with shop table
        WHERE {date_condition} {shop_condition}
        ORDER BY od.od_created_at DESC
        """
        print(f"Order Details Query: {query} with params: {params}") # Debug
        return self.database_class.fetch_all(query, tuple(params) if params else None)

    def _get_date_condition(self, filter_type, date_column):
        today = datetime.now().date()
        
        if filter_type.lower() == "daily":
            return f"DATE({date_column}) = '{today}'"
        elif filter_type.lower() == "weekly":
            week_start = today - timedelta(days=today.weekday())
            return f"DATE({date_column}) >= '{week_start}'"
        elif filter_type.lower() == "monthly":
            month_start = today.replace(day=1)
            return f"DATE({date_column}) >= '{month_start}'"
        else:
            return "TRUE" # Default: no date filter