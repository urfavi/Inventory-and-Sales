from datetime import date

def get_todays_sales(conn):
    cursor = conn.cursor()
    today = date.today()
    query = "SELECT SUM(total_amount) FROM sales WHERE DATE(sale_date) = %s"
    cursor.execute(query, (today,))
    return cursor.fetchone()[0] or 0

def get_todays_orders(conn):
    cursor = conn.cursor()
    today = date.today()
    query = "SELECT COUNT(*) FROM orders WHERE DATE(order_date) = %s"
    cursor.execute(query, (today,))
    return cursor.fetchone()[0]

def get_todays_revenue(conn):
    cursor = conn.cursor()
    today = date.today()
    query = "SELECT SUM(payment_amount) FROM payments WHERE DATE(payment_date) = %s"
    cursor.execute(query, (today,))
    return cursor.fetchone()[0] or 0

def get_best_sellers(conn):
    cursor = conn.cursor()
    query = """
        SELECT product_name, SUM(quantity_sold) AS total
        FROM sales
        GROUP BY product_name
        ORDER BY total DESC
        LIMIT 5;
    """
    cursor.execute(query)
    return cursor.fetchall()

def get_low_stock_products(conn):
    cursor = conn.cursor()
    query = "SELECT product_name, stock_quantity FROM inventory WHERE stock_quantity < 10"
    cursor.execute(query)
    return cursor.fetchall()
