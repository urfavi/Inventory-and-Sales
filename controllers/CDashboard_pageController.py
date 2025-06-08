from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from models.CDashboard_pageModel import DashboardPageModel
from models.database import Database

class DashboardPageController:
    def __init__(self, dashboard_ui, parent_controller=None, current_user_id=None, 
                 current_username=None, current_shop_id=None, cashier_controller=None):
        """
        Initialize dashboard controller with flexible parameters to work with both:
        - Old code (cashier_controller parameter)
        - New code (parent_controller + user parameters)
        """
        self.ui = dashboard_ui
        self.current_user_id = current_user_id
        self.current_username = current_username
        self.current_shop_id = current_shop_id
        
        # Backward compatibility
        if cashier_controller is not None:
            self.parent_controller = cashier_controller
            if hasattr(cashier_controller, 'current_user_id'):
                self.current_user_id = cashier_controller.current_user_id
            if hasattr(cashier_controller, 'current_username'):
                self.current_username = cashier_controller.current_username
            if hasattr(cashier_controller, 'current_user_shop_id'):
                self.current_shop_id = cashier_controller.current_user_shop_id
        else:
            self.parent_controller = parent_controller

        self.model = DashboardPageModel(Database())

        # Initialize dashboard data
        self.update_dashboard_data()
        self.add_best_sellers_chart()

    def update_dashboard_data(self):
        """Update all dashboard metrics"""
        # Get today's data
        today_sales = self.model.get_today_sales()
        today_orders = self.model.get_today_orders()
        today_revenue = self.model.get_today_revenue()

        font = self.ui.value_Tod_sales.font()
        font.setPointSize(32)
        font.setBold(True)    

        # Apply the same font to both sales and revenue
        self.ui.value_Tod_sales.setFont(font)
        self.ui.value_Tod_revenue.setFont(font)

        # Update UI elements
        self.ui.value_Tod_sales.setText(f"₱{today_sales:,.2f}")
        self.ui.value_Tod_orders.setText(f"{today_orders}")
        self.ui.value_Tod_revenue.setText(f"₱{today_revenue:,.2f}")

    def add_best_sellers_chart(self):
        """Add best sellers chart to the dashboard"""
        # Clear existing widgets
        layout = self.ui.frameBestSellersChart.layout()
        if layout:
            QtWidgets.QWidget().setLayout(layout)
        
        # Create new layout
        layout = QtWidgets.QVBoxLayout(self.ui.frameBestSellersChart)
        self.ui.frameBestSellersChart.setLayout(layout)
        
        # Adjust frame size
        self.ui.frameBestSellersChart.setGeometry(QtCore.QRect(20, 80, 891, 555))
        
        # Create matplotlib figure
        fig = Figure(figsize=(6.5, 4.3), dpi=100, facecolor='none')
        ax = fig.add_subplot(111)
        
        # Make the plot area (axes) transparent
        ax.set_facecolor('none')  # <-- Set axes background to transparent
        
        # Get best sellers data
        best_sellers = self.model.get_best_sellers()
        items = [row['product_name'] for row in best_sellers]
        sales = [row['total_quantity'] for row in best_sellers]
        
        # Create bar chart
        bars = ax.bar(items, sales, color='#003366', width=0.6)
        
        # Customize chart
        ax.set_ylabel('Quantity Sold', fontsize=10)
        ax.tick_params(axis='x', labelsize=8, rotation=45)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}',
                    ha='center', va='bottom', fontsize=8)
        
        # Adjust spacing
        fig.tight_layout()
        
        # Create canvas and add to layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        
        # Set canvas size policy
        canvas.setSizePolicy(
            QtWidgets.QSizePolicy.Expanding, 
            QtWidgets.QSizePolicy.Expanding
        )