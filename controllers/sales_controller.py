from models.order_model import OrderModel
from PyQt5.QtWidgets import QTableWidgetItem
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class SalesController:
    """Controller for sales and reporting operations"""
    
    def __init__(self):
        """Initialize the sales controller"""
        pass
    
    def get_sales_by_period(self, period='daily'):
        """
        Get sales data by time period
        
        Args:
            period (str): Period type (daily, weekly, monthly)
            
        Returns:
            list: Sales data
        """
        try:
            return OrderModel.get_sales_by_period(period)
        except Exception as e:
            print(f"Error retrieving sales data: {str(e)}")
            return []
    
    def get_sales_by_product_type(self, product_type=None, period='all'):
        """
        Get sales by product type
        
        Args:
            product_type (str, optional): Product type to filter by
            period (str): Time period (all, daily, weekly, monthly)
            
        Returns:
            list: Sales data
        """
        try:
            return OrderModel.get_sales_by_product_type(product_type, period)
        except Exception as e:
            print(f"Error retrieving product type sales: {str(e)}")
            return []
    
    def get_best_selling_products(self, limit=10, period='all'):
        """
        Get best selling products
        
        Args:
            limit (int): Maximum number of products to return
            period (str): Time period (all, daily, weekly, monthly)
            
        Returns:
            list: Best selling products
        """
        try:
            return OrderModel.get_best_selling_products(limit, period)
        except Exception as e:
            print(f"Error retrieving best sellers: {str(e)}")
            return []
    
    def create_sales_report_chart(self, figure, sales_data, period='daily'):
        """
        Create a sales report chart
        
        Args:
            figure (Figure): Matplotlib figure to draw on
            sales_data (list): Sales data from database
            period (str): Period type (daily, weekly, monthly)
            
        Returns:
            None
        """
        try:
            # Clear the figure
            figure.clear()
            
            # Create subplot
            ax = figure.add_subplot(111)
            
            # Extract x and y data
            if period == 'daily':
                x_values = [d['sale_date'].strftime('%m/%d') for d in sales_data]
            elif period == 'weekly':
                x_values = [f"Week {i+1}" for i in range(len(sales_data))]
            elif period == 'monthly':
                x_values = [d['sale_month'].strftime('%b %Y') for d in sales_data]
            else:
                x_values = ["All Time"]
                
            y_values = [float(d['total_sales']) for d in sales_data]
            
            # Create bar chart
            bars = ax.bar(x_values, y_values, color='lightgreen')
            
            # Add value labels on top of each bar
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'₱{height:.2f}',
                        ha='center', va='bottom', rotation=0)
            
            # Customize chart
            ax.set_title(f"Sales Report ({period.capitalize()})")
            ax.set_xlabel("Period")
            ax.set_ylabel("Total Sales (₱)")
            
            # Rotate x labels for better readability
            plt.xticks(rotation=45)
            
            # Adjust layout
            figure.tight_layout()
            
            # Draw the updated figure
            figure.canvas.draw()
            
        except Exception as e:
            print(f"Error creating sales chart: {str(e)}")
    
    def create_product_type_chart(self, figure, sales_data):
        """
        Create a product type breakdown chart
        
        Args:
            figure (Figure): Matplotlib figure to draw on
            sales_data (list): Sales data by product type
            
        Returns:
            None
        """
        try:
            # Clear the figure
            figure.clear()
            
            # Create subplot
            ax = figure.add_subplot(111)
            
            # Extract data
            labels = [d['prod_type_name'] for d in sales_data]
            sizes = [float(d['total_sales']) for d in sales_data]
            
            if not sizes:
                # No data, show empty chart
                ax.text(0.5, 0.5, 'No sales data available',
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform=ax.transAxes)
            else:
                # Create pie chart
                wedges, texts, autotexts = ax.pie(
                    sizes, 
                    labels=labels,
                    autopct='%1.1f%%',
                    startangle=90,
                    shadow=False
                )
                
                # Equal aspect ratio ensures that pie is drawn as a circle
                ax.axis('equal')
                
                # Set title
                ax.set_title("Sales by Product Type")
            
            # Draw the updated figure
            figure.tight_layout()
            figure.canvas.draw()
            
        except Exception as e:
            print(f"Error creating product type chart: {str(e)}")
    
    def create_best_sellers_chart(self, figure, sales_data):
        """
        Create a best sellers chart
        
        Args:
            figure (Figure): Matplotlib figure to draw on
            sales_data (list): Best selling products data
            
        Returns:
            None
        """
        try:
            # Clear the figure
            figure.clear()
            
            # Create subplot
            ax = figure.add_subplot(111)
            
            # Extract data
            products = [d['product_name'] for d in sales_data]
            quantities = [int(d['total_qty']) for d in sales_data]
            
            # Limit to top 5 for readability if there are more
            if len(products) > 5:
                products = products[:5]
                quantities = quantities[:5]
            
            if not quantities:
                # No data, show empty chart
                ax.text(0.5, 0.5, 'No sales data available',
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform=ax.transAxes)
            else:
                # Create horizontal bar chart
                bars = ax.barh(products, quantities, color='skyblue')
                
                # Add value labels on right of each bar
                for bar in bars:
                    width = bar.get_width()
                    ax.text(width, bar.get_y() + bar.get_height()/2.,
                           f'{width}',
                           ha='left', va='center')
                
                # Set title and labels
                ax.set_title("Best Selling Products")
                ax.set_xlabel("Units Sold")
                ax.set_ylabel("Product")
                
                # Adjust layout
                ax.invert_yaxis()  # Show highest values on top
            
            # Draw the updated figure
            figure.tight_layout()
            figure.canvas.draw()
            
        except Exception as e:
            print(f"Error creating best sellers chart: {str(e)}")