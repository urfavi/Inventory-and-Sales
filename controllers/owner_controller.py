from gui_classes.ui_landing import Ui_JJ_LANDING  # Correct path
from gui_classes.ui_login import Ui_LOGIN # Correct path
from gui_classes.ui_owner import Ui_OWNER  # Correct path
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class OwnerInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_OWNER()
        self.ui.setupUi(self)

        # Initialize UI components
        self.setup_ui()
        self.connect_navigation_buttons()
        self.connect_dashboard_buttons()
        self.connect_inventory_buttons()
        self.connect_orders_buttons()
        self.connect_sales_buttons()
        self.connect_account_buttons()
        
        # Set initial view to dashboard when the owner logs in
        self.show_dashboard()
        
        # Add sample chart to dashboard. NOTE: EDIT CHART LATER
        self.add_best_sellers_chart()

    # --------------------- UI Initialization Methods ---------------------
    def setup_ui(self):
        # Configure date/time labels to support rich text
        self.ui.dateLabel.setTextFormat(Qt.RichText)
        self.ui.timeLabel.setTextFormat(Qt.RichText)
        self.ui.dateLabel_inAccount.setTextFormat(Qt.RichText) 
        self.ui.timeLabel_inAccount.setTextFormat(Qt.RichText)

        # Initialize date/time displays
        self.update_date()
        self.update_time()

        # Set up timer to update time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_all)
        self.timer.start(1000)  # Update every 1000ms (1 second)
        
        # Set default views
        self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)  # Blank sales report
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(0)  # Owner account view

    # --------------------- Navigation Methods ---------------------
    
    def connect_navigation_buttons(self):
        """Connect all navigation menu buttons to their handlers"""
        self.ui.pushButton_Dashboard.clicked.connect(self.show_dashboard)
        self.ui.pushButton_Inventory.clicked.connect(self.show_inventory)
        self.ui.pushButton_Orders.clicked.connect(self.show_orders)
        self.ui.pushButton_Sales.clicked.connect(self.show_sales)
        self.ui.pushButton_Account.clicked.connect(self.show_account)
        self.ui.pushButton_LogOut.clicked.connect(self.logout_back2landing)

    def connect_dashboard_buttons(self):
        """Connect buttons on the dashboard section"""
        self.ui.btnViewSalesReport.clicked.connect(self.show_sales)
        self.ui.btnViewMore_Inventory.clicked.connect(self.show_inventory)

    def connect_inventory_buttons(self):
        # OWNER Inventory Table view buttons
        self.ui.pushButton_Inventory_ALL_ITEMS_table.clicked.connect(
            self.view_all_items_table_inventory)
        
        self.ui.pushButton_Inventory_ROOF_table.clicked.connect(
            self.view_roof_table_inventory)
        
        self.ui.pushButton_Inventory_SPANDREL_table.clicked.connect(
            self.view_spandrel_table_inventory)
        
        self.ui.pushButton_Inventory_GUTTER_table.clicked.connect(
            self.view_gutter_table_inventory)
        
        # OWNER Inventory action buttons
        self.ui.pushButton_OWNER_Add_Inventory.clicked.connect(
            self.show_form_add_inventory)
        
        self.ui.pushButton_OWNER_Edit_Inventory.clicked.connect(
            self.show_form_edit_inventory)
        
        self.ui.pushButton_OWNER_Delete_Inventory.clicked.connect(
            self.show_form_delete_inventory)
        
        # Add stock form connections
        self.ui.comboBox_Select_Prod_Type_toAdd.currentIndexChanged.connect(self.switch_add_stock_form)
        
        self.ui.pushButton_Confirm_ROOFadd.clicked.connect(lambda: self.confirm_add_stock("ROOF"))
        self.ui.pushButton_Close_ROOFadd.clicked.connect(self.close_add_stock_form)
        
        self.ui.pushButton_Confirm_SPANDRELadd.clicked.connect(lambda: self.confirm_add_stock("SPANDREL"))
        self.ui.pushButton_Close_SPANDRELadd.clicked.connect(self.close_add_stock_form)
        
        self.ui.pushButton_Confirm_GUTTERadd.clicked.connect(lambda: self.confirm_add_stock("GUTTER"))
        self.ui.pushButton_Close_GUTTERadd.clicked.connect(self.close_add_stock_form)
        
        # Edit stock form connections
        self.ui.comboBox_Select_Prod_Type_toEdit.currentIndexChanged.connect(self.switch_edit_stock_form)
        
        self.ui.pushButton_Save_ROOFedit.clicked.connect(lambda: self.save_edit_stock("ROOF"))
        self.ui.pushButton_Discard_ROOFedit.clicked.connect(self.close_edit_stock_form)
        
        self.ui.pushButton_Save_SPANDRELedit.clicked.connect(lambda: self.save_edit_stock("SPANDREL"))
        self.ui.pushButton_Discard_SPANDRELedit.clicked.connect(self.close_edit_stock_form)
        
        self.ui.pushButton_Save_GUTTERedit.clicked.connect(lambda: self.save_edit_stock("GUTTER"))
        self.ui.pushButton_Discard_GUTTERedit.clicked.connect(self.close_edit_stock_form)        
        
        # Delete stock form connections
        self.ui.comboBox_Select_Prod_Type_toDelete.currentIndexChanged.connect(self.switch_delete_stock_form)
        
        self.ui.pushButton_Confirm_ROOFdelete.clicked.connect(lambda: self.confirm_delete_stock("ROOF"))
        self.ui.pushButton_Close_ROOFdelete.clicked.connect(self.close_delete_stock_form)
        
        self.ui.pushButton_Confirm_SPANDRELdelete.clicked.connect(lambda: self.confirm_delete_stock("SPANDREL"))
        self.ui.pushButton_Close_SPANDRELdelete.clicked.connect(self.close_delete_stock_form)
        
        self.ui.pushButton_Confirm_GUTTERdelete.clicked.connect(lambda: self.confirm_delete_stock("GUTTER"))
        self.ui.pushButton_Close_GUTTERdelete.clicked.connect(self.close_delete_stock_form) 

    def connect_orders_buttons(self):
        # Sort orders by amount (high-low or low-high)
        self.ui.comboBox_SortORDERS_high_low.currentIndexChanged.connect(
            self.sort_orders_by_amount) 

    def connect_sales_buttons(self):
        # Filter sales report by time period (daily, weekly, monthly)
        self.ui.comboBox_SR_all_items.currentIndexChanged.connect(self.show_sales_report)
            
        # Filter sales report by product type (roof, spandrel, gutter)
        self.ui.comboBox_SR_prodType.currentIndexChanged.connect(self.show_product_report)

    def connect_account_buttons(self):
        # Owner account buttons
        self.ui.pushButton_VIEW.clicked.connect(self.view_owner_account)
        self.ui.pushButton_EditAccount.clicked.connect(self.edit_owner_account)
        self.ui.pushButton_ChangePassword.clicked.connect(self.change_password)

        # Cashier account buttons in OWNER INTERFACE
        self.ui.pushButton_VIEW_C.clicked.connect(self.view_cashier_account)
        self.ui.pushButton_EditAccount_cashier.clicked.connect(self.edit_cashier_account)
        self.ui.pushButton_ChangePassword_cashier.clicked.connect(self.change_cashier_password)
        self.ui.pushButton_CREATE_C.clicked.connect(self.create_cashier_account)

    # --------------------- Date/Time Methods ---------------------
    
    def update_all(self):
        """Update both date and time displays"""
        self.update_date()
        self.update_time()

    def update_date(self):
        """Update the date display with current date"""
        current_date = QDate.currentDate()
        formatted_date = current_date.toString("MMMM dd, yyyy")
        formatted_day = current_date.toString("dddd")
        
        # Update OWNER main dashboard date display
        self.ui.dateLabel.setText(
            f"<html><head/><body>"
            f"<p align='right'><span style='font-size:48pt;'>{formatted_date}</span>"
            f"<span style='font-size:48pt; color:#ffffff;'>.....</span></p>"
            f"<p align='center'><span style='font-size:20pt;'>{formatted_day}</span>"
            f"<span style='font-size:20pt; color:#ffffff;'>...............................</span></p>"
            f"</body></html>"
        )

        # Update OWNER account section date display
        self.ui.dateLabel_inAccount.setText(
            f"<html><head/><body>"
            f"<p align='right'><span style='font-size:48pt;'>{formatted_date}</span>"
            f"<span style='font-size:48pt; color:#ffffff;'>.....</span></p>"
            f"<p align='center'><span style='font-size:20pt;'>{formatted_day}</span>"
            f"<span style='font-size:20pt; color:#ffffff;'>...............................</span></p>"
            f"</body></html>"
        )

    def update_time(self):
        """Update the time display with current time"""
        current_time = QTime.currentTime()
        formatted_time = current_time.toString("hh:mm:ss AP")
        
        self.ui.timeLabel.setText(formatted_time)
        self.ui.timeLabel_inAccount.setText(formatted_time)

    # --------------------- Navigation Section Methods ---------------------
    
    def show_dashboard(self):
        """Show dashboard section and set active button state"""
        self.ui.stackedWidget.setCurrentIndex(0)
        self.set_active_button(self.ui.pushButton_Dashboard)

    def show_inventory(self):
        """Show inventory section and set active button state"""
        self.ui.stackedWidget.setCurrentIndex(1)
        self.set_active_button(self.ui.pushButton_Inventory)
        self.view_all_items_table_inventory()  # Show all items by default

    def show_orders(self):
        """Show orders section and set active button state"""
        self.ui.stackedWidget.setCurrentIndex(2)
        self.set_active_button(self.ui.pushButton_Orders)

    def show_sales(self):
        """Show sales section and set active button state"""
        self.ui.stackedWidget.setCurrentIndex(3)
        self.set_active_button(self.ui.pushButton_Sales)
        # Reset filters when showing sales page
        self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)

    def show_account(self):
        """Show account section and set active button state"""
        self.ui.stackedWidget.setCurrentIndex(4)
        self.set_active_button(self.ui.pushButton_Account)
        self.view_owner_account()  # Show owner account by default

    def logout_back2landing(self):
        """Return to landing page and close current window"""
        self.landing_page = Ui_JJ_LANDING()
        self.landing_page.show()
        self.close()

    # --------------------- Inventory Section Methods ---------------------
    
    def view_all_items_table_inventory(self):
        """Show all items inventory table view"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(0)
        self.set_active_inventorytable_button(self.ui.pushButton_Inventory_ALL_ITEMS_table)

    def view_roof_table_inventory(self):
        """Show roof items inventory table view"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(1)
        self.set_active_inventorytable_button(self.ui.pushButton_Inventory_ROOF_table)
        
    def view_spandrel_table_inventory(self):
        """Show spandrel items inventory table view"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(2)
        self.set_active_inventorytable_button(self.ui.pushButton_Inventory_SPANDREL_table)

    def view_gutter_table_inventory(self):
        """Show gutter items inventory table view"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(3)
        self.set_active_inventorytable_button(self.ui.pushButton_Inventory_GUTTER_table)
        
    def show_form_add_inventory(self):
        """Show form to add new inventory items"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(4)
        self.set_active_inventory_updateStock_button(self.ui.pushButton_OWNER_Add_Inventory) 
            # Reset ADD STOCK form to default state
        self.ui.comboBox_Select_Prod_Type_toAdd.setCurrentIndex(0)
        self.ui.Add_Select_Prod_Type.setCurrentIndex(0)
        self.ui.addStocklabel.setText("ADD STOCK")                    

    def show_form_edit_inventory(self):
        """Show form to edit existing inventory items"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(5)
        self.set_active_inventory_updateStock_button(self.ui.pushButton_OWNER_Edit_Inventory)
            # Reset EDIT STOCK form to default state
        self.ui.comboBox_Select_Prod_Type_toEdit.setCurrentIndex(0)
        self.ui.Edit_Select_Prod_Type.setCurrentIndex(0)
        self.ui.editStocklabel.setText("EDIT STOCK")

    def show_form_delete_inventory(self):
        """Show form to delete inventory items"""
        self.ui.INVENTORY_afterBUTTONSclick.setCurrentIndex(6)
        self.set_active_inventory_updateStock_button(self.ui.pushButton_OWNER_Delete_Inventory)
            # Reset EDIT STOCK form to default state
        self.ui.comboBox_Select_Prod_Type_toDelete.setCurrentIndex(0)
        self.ui.Delete_Select_Prod_Type.setCurrentIndex(0)
        self.ui.deleteStocklabel.setText("DELETE STOCK")

    # --------------------- Add Stock Methods ---------------------
    def switch_add_stock_form(self, index):
        """ Switch between different add stock forms based on product type selection
        
        Args:
            index: The index of the selected item in the combo box
        """
        selected_type = self.ui.comboBox_Select_Prod_Type_toAdd.currentText()
        
        if selected_type == "ROOF":
            self.ui.Add_Select_Prod_Type.setCurrentIndex(1)
            self.ui.addStocklabel.setText("ADD ROOF STOCK")
        elif selected_type == "SPANDREL":
            self.ui.Add_Select_Prod_Type.setCurrentIndex(2)
            self.ui.addStocklabel.setText("ADD SPANDREL STOCK")
        elif selected_type == "GUTTER":
            self.ui.Add_Select_Prod_Type.setCurrentIndex(3)
            self.ui.addStocklabel.setText("ADD GUTTER STOCK")
        else:
            self.ui.Add_Select_Prod_Type.setCurrentIndex(0)
            self.ui.addStocklabel.setText("ADD STOCK")
            
    def confirm_add_stock(self, product_type):
        """
        Handle confirmation of adding new stock
        
        Args:
            product_type: Type of product being added (ROOF, SPANDREL, GUTTER)
        """
        # TODO: Implement actual stock addition logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText(f"{product_type} stock added successfully!")
        msg.exec_()
        
        # Return to inventory table view
        self.view_all_items_table_inventory()

    def close_add_stock_form(self):
        """Close the add stock form without saving changes"""
        self.view_all_items_table_inventory()

    # --------------------- Edit Stock Methods ---------------------
    
    def switch_edit_stock_form(self, index):
        """
        Switch between different edit stock forms based on product type selection
        
        Args:
            index: The index of the selected item in the combo box
        """
        selected_type = self.ui.comboBox_Select_Prod_Type_toEdit.currentText()
        
        if selected_type == "ROOF":
            self.ui.Edit_Select_Prod_Type.setCurrentIndex(1)
            self.ui.editStocklabel.setText("EDIT ROOF STOCK")
        elif selected_type == "SPANDREL":
            self.ui.Edit_Select_Prod_Type.setCurrentIndex(2)
            self.ui.editStocklabel.setText("EDIT SPANDREL STOCK")
        elif selected_type == "GUTTER":
            self.ui.Edit_Select_Prod_Type.setCurrentIndex(3)
            self.ui.editStocklabel.setText("EDIT GUTTER STOCK")
        else:
            self.ui.Edit_Select_Prod_Type.setCurrentIndex(0)
            self.ui.editStocklabel.setText("EDIT STOCK")
            
    def save_edit_stock(self, product_type):
        """
        Handle saving of edited stock information
        
        Args:
            product_type: Type of product being edited (ROOF, SPANDREL, GUTTER)
        """
        # TODO: Implement actual stock editing logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText(f"{product_type} stock updated successfully!")
        msg.exec_()
        
        # Return to inventory table view
        self.view_all_items_table_inventory()

    def close_edit_stock_form(self):
        """Close the edit stock form without saving changes"""
        self.view_all_items_table_inventory()
        
    # --------------------- Delete Stock Methods ---------------------
    
    def switch_delete_stock_form(self, index):
        """
        Switch between different delete stock forms based on product type selection
        
        Args:
            index: The index of the selected item in the combo box
        """
        selected_type = self.ui.comboBox_Select_Prod_Type_toDelete.currentText()
        
        if selected_type == "ROOF":
            self.ui.Delete_Select_Prod_Type.setCurrentIndex(1)
            self.ui.deleteStocklabel.setText("DELETE ROOF STOCK")
        elif selected_type == "SPANDREL":
            self.ui.Delete_Select_Prod_Type.setCurrentIndex(2)
            self.ui.deleteStocklabel.setText("DELETE SPANDREL STOCK")
        elif selected_type == "GUTTER":
            self.ui.Delete_Select_Prod_Type.setCurrentIndex(3)
            self.ui.deleteStocklabel.setText("DELETE GUTTER STOCK")
        else:
            self.ui.Delete_Select_Prod_Type.setCurrentIndex(0)
            self.ui.deleteStocklabel.setText("DELETE STOCK")
            
    def confirm_delete_stock(self, product_type):
        """
        Handle confirmation of deleting stock
        
        Args:
            product_type: Type of product being deleted (ROOF, SPANDREL, GUTTER)
        """
        # Create confirmation dialog
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Confirm Deletion")
        msg.setText(f"Are you sure you want to delete this {product_type} stock?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        # Show dialog and get response
        response = msg.exec_()
        
        if response == QMessageBox.Yes:
            # TODO: Implement actual stock deletion logic
            success_msg = QMessageBox()
            success_msg.setIcon(QMessageBox.Information)
            success_msg.setWindowTitle("Success")
            success_msg.setText(f"{product_type} stock deleted successfully!")
            success_msg.exec_()
            
            # Return to inventory table view
            self.view_all_items_table_inventory()

    def close_delete_stock_form(self):
        """Close the delete stock form without deleting"""
        self.view_all_items_table_inventory()
        
    # --------------------- Orders Section Methods ---------------------
    
    def sort_orders_by_amount(self, index):
        """ Sort orders by total amount (high-low or low-high)
        Args:
            index: Selected index from comboBox_SortORDERS_high_low
        """
        selected_sort = self.ui.comboBox_SortORDERS_high_low.currentText()
        
        if selected_sort == "TOTAL AMOUNT (HIGHEST TO LOWEST)":
            # TODO: Implement sorting logic (high to low)
            pass
        elif selected_sort == "TOTAL AMOUNT (LOWEST TO HIGHEST)":
            # TODO: Implement sorting logic (low to high)
            pass        
        
    # --------------------- Sales Report Section Methods ---------------------
    
    def show_sales_report(self, index):
        """ Filter sales report by time period (daily, weekly, monthly) 
        Args:
            index: Selected index from comboBox_SR_all_items
        """
        if index == 0:  # "Generate Sales Report for All Items"
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)  # Blank page
        
        elif index == 1:  # DAILY
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(1)
            self.ui.SALES_label.setText("DAILY SALES")
            # TODO: Load daily sales data into tableWidget_SR_DAILY
            
        elif index == 2:  # WEEKLY
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(2)
            self.ui.SALES_label.setText("WEEKLY SALES")
            # TODO: Load weekly sales data into tableWidget_SR_WEEKLY
            
        elif index == 3:  # MONTHLY
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(3)
            self.ui.SALES_label.setText("MONTHLY SALES")
            # TODO: Load monthly sales data into tableWidget_SR_MONTHLY
            
        else:
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)

    def show_product_report(self, index):
        """ Filter sales report by product type (roof, spandrel, gutter)
        Args:
            index: Selected index from comboBox_SR_prodType
        """
        if index == 0:  # "Generate Sales Report for Product Type"
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)  # Blank page
        
        elif index == 1:  # ROOF
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(4)
            self.ui.SALES_label.setText("ROOF SALES")
            # TODO: Load roof sales data into tableWidget_SR_ROOF
            
        elif index == 2:  # SPANDREL
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(5)
            self.ui.SALES_label.setText("SPANDREL SALES")
            # TODO: Load spandrel sales data into tableWidget_SR_SPANDREL
            
        elif index == 3:  # GUTTER
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(6)
            self.ui.SALES_label.setText("GUTTER SALES")
            # TODO: Load gutter sales data into tableWidget_SR_GUTTER
            
        else:
            self.ui.stackedWidget_choose_SALES_REPORT.setCurrentIndex(0)      
                

    # --------------------- Account Section Methods ---------------------
    
    def view_owner_account(self): # Show owner account information
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(0)
        self.set_active_account_button(self.ui.pushButton_VIEW)
        # Reset the edit/password buttons to inactive state
        self.set_button_inactive_inside_buttons_owner_account(self.ui.pushButton_EditAccount)
        self.set_button_inactive_inside_buttons_owner_account(self.ui.pushButton_ChangePassword)

    def edit_owner_account(self): # Show edit owner account page
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(1)
        self.set_active_inside_account_button(self.ui.pushButton_EditAccount)
       # Connect save and cancel buttons
        self.ui.pushButton_saveEditaccount.clicked.connect(self.save_owner_edit)
        self.ui.pushButton_cancelEditaccount.clicked.connect(self.cancel_owner_edit)

    def save_owner_edit(self):
        # TODO: Add actual save logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Owner account has been updated!")
        msg.exec_()
        self.view_owner_account()  # Return to view page after save

    def cancel_owner_edit(self):
        self.view_owner_account()  # Return to view page on cancel

    def change_password(self): # Show change password form
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(2)
        self.set_active_account_button(self.ui.pushButton_ChangePassword)
        # Connect save and cancel buttons
        self.ui.pushButton_saveNEWpassword.clicked.connect(self.save_new_password)
        self.ui.pushButton_cancelNEWpassword.clicked.connect(self.cancel_password_change)

    def save_new_password(self):
        # TODO: Add actual password change logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Owner password has been changed!")
        msg.exec_()
        self.view_owner_account()  # Return to view page after save

    def cancel_password_change(self):
        self.view_owner_account()  # Return to view page on cancel

    def view_cashier_account(self): # Show cashier account information 
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(3)
        self.set_active_account_button(self.ui.pushButton_VIEW_C)
        # Reset the edit/password/create buttons to inactive state
        self.set_button_inactive_inside_buttons_owner_account(self.ui.pushButton_EditAccount_cashier)
        self.set_button_inactive_inside_buttons_owner_account(self.ui.pushButton_ChangePassword_cashier)

    def edit_cashier_account(self): # Show edit cashier account page
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(4)
        self.set_active_inside_account_button(self.ui.pushButton_EditAccount_cashier)
        # Connect save and cancel buttons
        self.ui.pushButton_saveEditaccount_cashier.clicked.connect(self.save_cashier_edit)
        self.ui.pushButton_cancelEditaccount_cashier.clicked.connect(self.cancel_cashier_edit)

    def save_cashier_edit(self):
        # TODO: Add actual save logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Cashier account has been updated!")
        msg.exec_()
        self.view_cashier_account()  # Return to view page after save

    def cancel_cashier_edit(self):
        self.view_cashier_account()  # Return to view page on cancel

    def change_cashier_password(self): # Show change cashier password form
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(5)
        self.set_active_inside_account_button(self.ui.pushButton_ChangePassword_cashier)
        # Connect save and cancel buttons
        self.ui.pushButton_saveNEWpassword_cashier.clicked.connect(self.save_new_cashier_password)
        self.ui.pushButton_cancelNEWpassword_cashier.clicked.connect(self.cancel_cashier_password_change)

    def save_new_cashier_password(self):
        # TODO: Add actual password change logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("Cashier password has been changed!")
        msg.exec_()
        self.view_cashier_account()  # Return to view page after save

    def cancel_cashier_password_change(self):
        self.view_cashier_account()  # Return to view page on cancel


    def create_cashier_account(self): # Show cashier account creation form
        self.ui.stackedWidget_AccountBtns.setCurrentIndex(6)
        self.set_active_account_button(self.ui.pushButton_CREATE_C)
        
        # Connect the create button to the actual creation handler
        self.ui.pushButton_CreateAccount_cashier.clicked.connect(self.handle_cashier_account_creation) 
        # Connect the cancel button to return to view cashier page
        self.ui.pushButton_cancelCreateAccount_cashier.clicked.connect(self.view_cashier_account)
        
    def handle_cashier_account_creation(self):           
        # TODO: Add actual account creation logic
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success")
        msg.setText("CASHIER account has been created!")
        msg.exec_()
        self.view_cashier_account()  # Return to view page after save

    # --------------------- UI Styling Methods ---------------------
    
    def set_active_button(self, button):
        """ Set the active state for a navigation menu button """
        buttons = [
            self.ui.pushButton_Dashboard, 
            self.ui.pushButton_Inventory,
            self.ui.pushButton_Orders, 
            self.ui.pushButton_Sales, 
            self.ui.pushButton_Account,
            self.ui.pushButton_LogOut
        ]

        # Reset all buttons to default style
        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    color: black;
                    border-radius: 15px;
                    border: 1px solid #000000;
                    padding: 9px;
                    font-size: 14;
                    font-family: "Verdana", sans-serif; 
                    text-align: left;
                }
                QPushButton:hover {
                    background-color:#8d2721;
                    color:white;
                    text-align: left;
                    font-weight: 500;
                }
            """)

        # Set active button style
        button.setStyleSheet("""
            QPushButton {
                background-color: #8d2721;
                color: white;
                border-radius: 15px;
                border: 1px solid #000000;
                padding: 9px;
                font-size: 14;
                font-family: "Verdana", sans-serif; 
                text-align: left;
                font-weight: 500;
            }
        """)

    def set_active_inventorytable_button(self, button):
        """ Set the active state for an inventory table view button """
        table_buttons = [
            self.ui.pushButton_Inventory_ALL_ITEMS_table, 
            self.ui.pushButton_Inventory_ROOF_table,
            self.ui.pushButton_Inventory_SPANDREL_table,
            self.ui.pushButton_Inventory_GUTTER_table,            
        ]
        
        # Reset all table buttons to default style
        for btn in table_buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    color: black;
                    border: 1px solid #000000; 
                    padding: 10px;
                    font-family: "Verdana", sans-serif; 
                    text-align: center;
                    border-top-left-radius: 15px;
                    border-top-right-radius: 15px;
                    border-bottom-left-radius: 0px;
                    border-bottom-right-radius: 0px;
                }
                QPushButton:hover {
                    background-color: #903929;
                    color: white;
                    font-weight: 700;
                }
            """)
        
        # Reset inventory action buttons to default style
        action_buttons = [
            self.ui.pushButton_OWNER_Add_Inventory,
            self.ui.pushButton_OWNER_Edit_Inventory,
            self.ui.pushButton_OWNER_Delete_Inventory
        ]
        
        for btn in action_buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ebe0cc;
                    color: black;
                    border: 1px solid #000000; 
                    padding: 10px;
                    font-family: "Verdana", sans-serif; 
                    text-align: center;
                }
                QPushButton:hover {
                    background-color:#d7a613;
                    color:black;
                }
            """)
        
        # Set active button style
        button.setStyleSheet("""
            QPushButton {
                background-color: #903929;
                color: white;
                font-weight: 700;
                border: 1px solid #000000; 
                padding: 10px;
                font-family: "Verdana", sans-serif; 
                text-align: center;
                border-top-left-radius: 15px;
                border-top-right-radius: 15px;
                border-bottom-left-radius: 0px;
                border-bottom-right-radius: 0px;
            }
        """)

    def set_active_inventory_updateStock_button(self, button):
        """ Set the active state for an inventory action button """
        table_buttons = [
            self.ui.pushButton_Inventory_ALL_ITEMS_table, 
            self.ui.pushButton_Inventory_ROOF_table,
            self.ui.pushButton_Inventory_SPANDREL_table,
            self.ui.pushButton_Inventory_GUTTER_table,            
        ]
        
        for btn in table_buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    color: black;
                    border: 1px solid #000000; 
                    padding: 10px;
                    font-family: "Verdana", sans-serif; 
                    text-align: center;
                    border-top-left-radius: 15px;
                    border-top-right-radius: 15px;
                    border-bottom-left-radius: 0px;
                    border-bottom-right-radius: 0px;
                }
                QPushButton:hover {
                    background-color: #903929;
                    color: white;
                    font-weight: 700;
                }
            """)
        
        # Reset all action buttons to default style
        action_buttons = [
            self.ui.pushButton_OWNER_Add_Inventory,
            self.ui.pushButton_OWNER_Edit_Inventory,
            self.ui.pushButton_OWNER_Delete_Inventory
        ]
        
        for btn in action_buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ebe0cc;
                    color: black;
                    border: 1px solid #000000; 
                    padding: 10px;
                    font-family: "Verdana", sans-serif; 
                    text-align: center;
                }
                QPushButton:hover {
                    background-color:#d7a613;
                    color:black;
                }
            """)
        
        # Set active button style
        button.setStyleSheet("""
            QPushButton {
                background-color: #d7a613;
                color: black;
            }
        """)

    def set_active_account_button(self, button):
        """ Set the active state for an account section button """
        buttons = [
            self.ui.pushButton_VIEW, 
            self.ui.pushButton_VIEW_C,
            self.ui.pushButton_CREATE_C
        ]

        # Reset all buttons to default style
        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #f6f3ee;
                    color: black;
                    border: 1px solid #000000; 
                    padding: 9px;
                    font-family: "Verdana", sans-serif; 
                    text-align: center;
                }
                QPushButton:hover {
                    background-color:#374550;
                    color:white;
                }
            """)

        # Set active button style
        button.setStyleSheet("""
            QPushButton {
                background-color: #374550;
                color: white;
                border: 1px solid #000000; 
                padding: 9px;
                font-family: "Verdana", sans-serif; 
                text-align: center;
            }
        """)

    def set_active_inside_account_button(self, button):
        buttons = [
            self.ui.pushButton_EditAccount, 
            self.ui.pushButton_ChangePassword,
            self.ui.pushButton_EditAccount_cashier,
            self.ui.pushButton_ChangePassword_cashier
        ]

        # Reset all buttons to default style
        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    color: #000000;
                    border: 1px solid #000000; 
                    border-radius: 9px; 
                    padding: 3px; 
                    background-color: #ffffff; 
                }
                QPushButton:hover {
                    background-color:#12245c;
                    color:white;
                    font-weight: 500;
                    border-radius: 9px; 
                }
            """)        
            
            # Set active button style
            button.setStyleSheet("""
                QPushButton {
                    background-color: #12245c;
                    color: white;
                    font-weight: 500;
                    border-radius: 9px; 
                }
            """)         

    def set_button_inactive_inside_buttons_owner_account(self, button):
        """Set a button to inactive state visually"""
        button.setChecked(False)
        button.setStyleSheet("""
                QPushButton {
                    color: #000000;
                    border: 1px solid #000000; 
                    border-radius: 9px; 
                    padding: 3px; 
                    background-color: #ffffff; 
                }
                QPushButton:hover {
                    background-color:#12245c;
                    color:white;
                    font-weight: 500;
                    border-radius: 9px; 
                }
            """)   

    # --------------------- Dashboard Methods ---------------------
    
    def add_best_sellers_chart(self): 
        """Add a sample best sellers chart to the dashboard"""
        # Clear any existing widgets from the frame
        layout = self.ui.frameBestSellersChart.layout()
        if layout:
            QtWidgets.QWidget().setLayout(layout)
        
        # Create a new layout
        layout = QtWidgets.QVBoxLayout(self.ui.frameBestSellersChart)
        self.ui.frameBestSellersChart.setLayout(layout)
        
        # Adjust frame size
        self.ui.frameBestSellersChart.setGeometry(QtCore.QRect(20, 80, 691, 431))
        
        # Create matplotlib figure
        fig = Figure(figsize=(6.5, 4.3), dpi=100)
        ax = fig.add_subplot(111)
        
        # Sample data
        items = ['Item 1', 'Item 2', 'Item 3', 'Item 4']
        sales = [7, 11, 16, 20]
        
        # Create bar chart
        bars = ax.bar(items, sales, color='#003366', width=0.6)
        
        # Customize chart
        ax.set_ylabel('Sales', fontsize=10)
        ax.tick_params(axis='x', labelsize=8, rotation=45)
        
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