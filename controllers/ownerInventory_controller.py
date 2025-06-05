# core/controllers/OInventoryController.py

class InventoryController:
    def __init__(self, ui, db_conn):
        self.ui = ui
        from core.models.OInventoryModel import InventoryModel
        self.model = InventoryModel(db_conn)

        self.load_products()

        # Example: Connect add button
        self.ui.pushButton_AddProduct.clicked.connect(self.add_product)
        self.ui.pushButton_DeleteProduct.clicked.connect(self.delete_selected_product)

    def load_products(self):
        self.ui.tableWidget.setRowCount(0)  # Clear table
        products = self.model.get_all_products()
        for row_index, row_data in enumerate(products):
            self.ui.tableWidget.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, col_index, QTableWidgetItem(str(col_data)))

    def add_product(self):
        name = self.ui.lineEdit_ProductName.text()
        category = self.ui.comboBox_Category.currentText()
        quantity = int(self.ui.spinBox_Quantity.value())
        price = float(self.ui.lineEdit_Price.text())

        self.model.add_product(name, category, quantity, price)
        self.load_products()

    def delete_selected_product(self):
        selected = self.ui.tableWidget.currentRow()
        product_id = self.ui.tableWidget.item(selected, 0).text()  # Assuming ID is in col 0
        self.model.delete_product(product_id)
        self.load_products()
