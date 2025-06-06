class OrdersPageController:
    # Add current_user_shop_id (and optionally current_user_id, current_username) to the __init__ signature
    def __init__(self, orders_ui, owner_controller, current_user_shop_id=None, current_user_id=None, current_username=None):
        self.ui = orders_ui
        self.owner_controller = owner_controller

        # Store the user and shop information
        # Provide temporary defaults for testing if the full login flow isn't complete yet.
        self.current_user_shop_id = current_user_shop_id if current_user_shop_id is not None else 1 # Default to 1
        self.current_user_id = current_user_id if current_user_id is not None else 1 # Default to 1 (example ID)
        self.current_username = current_username if current_username is not None else "admin_user" # Default username

        print(f"DEBUG: OrdersPageController initialized for Shop ID: {self.current_user_shop_id}, User ID: {self.current_user_id}, Username: {self.current_username}")

        # Connect the filter combo box to update the label
        self.ui.comboBox_filterOrders.currentTextChanged.connect(self.update_order_history_label)

        # Initialize label text based on the default combo box selection
        self.update_order_history_label(self.ui.comboBox_filterOrders.currentText())

    def update_order_history_label(self, filter_text):
        """Update the order history label based on the selected filter"""
        if filter_text == "Roof":
            self.ui.orderReportText.setText("Roof Order History")
        elif filter_text == "Spandrel":
            self.ui.orderReportText.setText("Spandrel Order History")
        elif filter_text == "Gutter":
            self.ui.orderReportText.setText("Gutter Order History")
        elif filter_text == "Others":
            self.ui.orderReportText.setText("Other Orders History")
        else:
            self.ui.orderReportText.setText("Order History")  # Default/fallback