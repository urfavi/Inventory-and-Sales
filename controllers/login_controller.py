from gui_classes.ui_landing import Ui_JJ_LANDING  # Correct path
from gui_classes.ui_login import Ui_LOGIN  # Correct path
from gui_classes.ui_forgotpass import Ui_ForgotPass  # Correct path
from gui_classes.ui_owner import Ui_OWNER  # Correct path
from controllers.owner_controller import OwnerInterface  # Adjust the import path as needed
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LOGIN()
        self.ui.setupUi(self)

        self.ui.pushButton_LOGIN.clicked.connect(self.open_owner_interface)
        self.ui.pushButton_xtolanding.clicked.connect(self.return_to_landing)
        self.ui.pushButton_forgotPass_login_page.clicked.connect(self.open_forgot_password)

    def open_owner_interface(self):
        username = self.ui.login_usrname.text()  # Make sure the field name matches your .ui file
        password = self.ui.login_password.text()  # Same for password field
        
        if self.authenticate_user(username, password):
            self.owner_interface = OwnerInterface()  # Create an instance of OwnerInterface
            self.owner_interface.show()  # Show the Owner Interface
            self.close()  # Close the login window
        else:
            self.show_error_message("Invalid username or password!")
    
    def authenticate_user(self, username, password):
        # Hardcoded accounts for testing
        accounts = {
            "admin": "admin123",    # admin account
            "user1": "password1",   # another test user
            "user2": "password2",   # another test user
        }

        # Check if username exists and the password matches
        if username in accounts and accounts[username] == password:
            return True
        return False

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Login Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        
    def return_to_landing(self):
        self.landing_page = Ui_JJ_LANDING()
        self.landing_page.show()
        self.close()

    def open_forgot_password(self):
        self.landing_page = ForgotPassword()
        self.landing_page.show()
        self.close()


class ForgotPassword(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ForgotPass()
        self.ui.setupUi(self)
        
        # Connect buttons
        self.ui.pushButton_xtolanding_forgotpass.clicked.connect(self.backto_owner_login_after_reset)
        self.ui.pushButton_ChangePass.clicked.connect(self.change_password_back2login)
    
    def change_password_back2login(self):
        # TODO: add password reset logic here (Check if passwords match, etc.)
        self.close()
        
        # Show a message that password was reset
        msg = QMessageBox()
        msg.setWindowTitle("Success")
        msg.setText("Password has been reset successfully!")
        msg.setIcon(QMessageBox.Information)
        msg.exec_()
        self.backto_owner_login_after_reset()  # Return to log in page after reset
        
    def backto_owner_login_after_reset(self):
        self.owner_login = Login()
        self.owner_login.show()
        self.close() 

