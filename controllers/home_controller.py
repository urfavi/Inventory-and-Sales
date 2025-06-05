from models.dashboard_model import get_todays_sales, get_todays_orders, get_todays_revenue
from models.dashboard_model import get_best_sellers
from models.dashboard_model import get_low_stock_products

def load_dashboard_widgets(conn):
    sales = get_todays_sales(conn)
    orders = get_todays_orders(conn)
    revenue = get_todays_revenue(conn)
    return sales, orders, revenue

def prepare_best_sellers_graph_data(conn):
    data = get_best_sellers(conn)
    products = [item[0] for item in data]
    totals = [item[1] for item in data]
    return products, totals

def load_low_stock_panel(conn):
    return get_low_stock_products(conn)
