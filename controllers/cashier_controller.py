from db.database import connect_db  # Import the function to connect to your database
import bcrypt
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from gui_classes.login import Ui_CashrLOGIN
from gui_classes.login import Ui_CASHIER_DASHBOARD

class CashierLoginPage(QMainWindow):  # ENTER CASHIER LOG IN INFO.
    def __init__(self):
        super().__init__()
        self.ui = Ui_CashrLOGIN()
        self.ui.setupUi(self)

        # When the cashier clicks the login button
        self.ui.pushButton_CASHIERLOGIN.clicked.connect(self.open_cashier_dashboard)

    def open_cashier_dashboard(self):
        username = self.ui.lineEdit_username.text().strip()
        password = self.ui.lineEdit_password.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        try:
            # Connect to the database
            conn = connect_db()
            if conn:
                cursor = conn.cursor()
                # Check if the username exists in the database
                cursor.execute("SELECT password FROM cashier_accounts WHERE username = %s", (username,))
                result = cursor.fetchone()

                if result:
                    # If the username is found, check the password
                    if bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
                        # If login is successful, show the Cashier Dashboard
                        self.cashier_dashboard = CashierDashboard()
                        self.cashier_dashboard.show()
                        self.close()
                    else:
                        # If the password doesn't match, show error
                        QMessageBox.warning(self, "Login Failed", "Invalid password.")
                else:
                    # If the username is not found, show error
                    QMessageBox.warning(self, "Login Failed", "Account not found. Please sign up first.")

                cursor.close()
                conn.close()
            else:
                QMessageBox.critical(self, "Database Error", "Could not connect to the database.")

        except Exception as e:
            QMessageBox.critical(self, "Database Error", str(e))

class CashierDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CASHIER_DASHBOARD()
        self.ui.setupUi(self)