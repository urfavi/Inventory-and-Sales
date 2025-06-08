from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtCore import QSettings
from models.database import Database
from gui_classes.UI_LogIn import Ui_LOGIN
from gui_classes.UI_ForgotPass import Ui_ForgotPass
from gui_classes.UI_Landing import Ui_JJ_LANDING 
from controllers.auth_controller import authenticate_user
from controllers.owner_controller import OwnerController
from controllers.cashier_controller import CashierController  # Commented out for now
from controllers.forgotpass_controller import ForgotPasswordWindow
from cryptography.fernet import Fernet
import bcrypt

# Declare global window holders
active_windows = {}

class LandingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JJ_LANDING()
        self.ui.setupUi(self)
        self.ui.pushButton_cont_2Login.clicked.connect(self.return_to_login)

    def return_to_login(self):
        self.hide()
        if 'login' not in active_windows or active_windows['login'] is None:
            active_windows['login'] = Login()
        else:
            active_windows['login'].clear_login_info()
        active_windows['login'].show()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = Database() 
        self.ui = Ui_LOGIN()
        self.ui.setupUi(self)

        self.login_pass_visible = False
        self.ui.login_password.setEchoMode(QLineEdit.Password)
        self.set_button_text(self.ui.togglePasswordButton, self.login_pass_visible)

        try:
            self.settings = QSettings("YourApp", "LoginCredentials")
            self.cipher = self._initialize_encryption()
            self._load_saved_credentials()
        except Exception as e:
            print(f"Initialization error: {e}")
            self.settings = None
            self.cipher = None

        self.ui.pushButton_LOGIN.clicked.connect(self.handle_login_button_clicked)
        self.ui.pushButton_xtolanding.clicked.connect(self.return_to_landing)
        self.ui.pushButton_forgotPass_login_page.clicked.connect(self.open_forgot_password)
        self.ui.togglePasswordButton.clicked.connect(self.toggle_login_password_visibility)

        if hasattr(self.ui, 'pushButton_clearLogins'):
            self.ui.pushButton_clearLogins.clicked.connect(self.clear_input_fields)
        if hasattr(self.ui, 'checkBox_rememberme'):
            self.ui.checkBox_rememberme.stateChanged.connect(self._handle_remember_me_change)

    def _initialize_encryption(self):
        try:
            key = self.settings.value("encryption_key")
            if not key:
                key = Fernet.generate_key().decode()
                self.settings.setValue("encryption_key", key)
            return Fernet(key.encode())
        except Exception as e:
            print(f"Encryption init error: {e}")
            return None

    def _load_saved_credentials(self):
        if not self.cipher:
            return
        try:
            encrypted_user = self.settings.value("saved_username")
            encrypted_pass = self.settings.value("saved_password")
            if encrypted_user and encrypted_pass:
                username = self.cipher.decrypt(encrypted_user.encode()).decode()
                password = self.cipher.decrypt(encrypted_pass.encode()).decode()
                self.ui.login_usrname.setText(username)
                self.ui.login_password.setText(password)
                if hasattr(self.ui, 'checkBox_rememberme'):
                    self.ui.checkBox_rememberme.setChecked(True)
            else:
                if hasattr(self.ui, 'checkBox_rememberme'):
                    self.ui.checkBox_rememberme.setChecked(False)
        except Exception as e:
            print(f"Credential load error: {e}")
            self.clear_saved_credentials()

    def clear_saved_credentials(self):
        if not self.settings:
            return
        try:
            self.settings.remove("saved_username")
            self.settings.remove("saved_password")
            if hasattr(self.ui, 'checkBox_rememberme'):
                self.ui.checkBox_rememberme.setChecked(False)
            QMessageBox.information(self, "Success", "Saved logins cleared.")
        except Exception as e:
            print(f"Clear credentials error: {e}")

    def showEvent(self, event):
        super().showEvent(event)
        if hasattr(self.ui, 'checkBox_rememberme') and self.ui.checkBox_rememberme.isChecked():
            self._load_saved_credentials()

    def clear_input_fields(self):
        self.ui.login_usrname.clear()
        self.ui.login_password.clear()

    def _handle_remember_me_change(self, state):
        if state == 0:
            self.clear_saved_credentials()

    def _save_credentials(self, username, password):
        if not self.cipher:
            return False
        try:
            encrypted_user = self.cipher.encrypt(username.encode()).decode()
            encrypted_pass = self.cipher.encrypt(password.encode()).decode()
            self.settings.setValue("saved_username", encrypted_user)
            self.settings.setValue("saved_password", encrypted_pass)
            return True
        except Exception as e:
            print(f"Save credentials error: {e}")
            return False

    def handle_login_button_clicked(self):
        print("Login button clicked!")
        username = self.ui.login_usrname.text().strip()
        password = self.ui.login_password.text().strip()

        if not username or not password:
            self.show_error_message("Both username and password are required!")
            return

        try:  # Make sure this is properly indented and has a colon
            # Get user from database
            query = """SELECT user_acc_id, user_acc_username, user_acc_password_hash, user_acc_role 
                    FROM user_account WHERE user_acc_username = %s"""
            user = self.database.fetch_one(query, (username,))
            
            print("DEBUG - User query result:", user)  # Debug line

            if not user:
                self.show_error_message("Invalid username or password!")
                return

            # Verify password
            if not bcrypt.checkpw(password.encode(), user['user_acc_password_hash'].encode()):
                self.show_error_message("Invalid username or password!")
                return

            # Handle successful login
            self._handle_successful_login(user)

        except Exception as e:  # Make sure you have this except block
            print(f"Login error: {str(e)}")
            self.show_error_message("Login failed. Please try again.")

    def _handle_successful_login(self, user):
        try:
            if not user or not isinstance(user, dict):
                raise ValueError("Invalid user data received")
                
            required_fields = ['user_acc_username', 'user_acc_role', 'user_acc_id']
            for field in required_fields:
                if field not in user:
                    raise ValueError(f"Missing required field: {field}")

            username = user['user_acc_username']
            role = user['user_acc_role']
            user_id = user['user_acc_id']
            
            print(f"DEBUG - Logging in user: {username}, role: {role}")  # Debug line

            if hasattr(self.ui, 'checkBox_rememberme') and self.ui.checkBox_rememberme.isChecked():
                self._save_credentials(username, "")

            if role == 'OWNER':
                self._open_owner_interface(user)
            elif role == 'CASHIER':
                self._open_cashier_interface(user)
            else:
                raise ValueError(f"Unknown role: {role}")
                
        except Exception as e:
            print(f"Login flow error details: {str(e)}")
            self.show_error_message("Login failed. Please contact support.")

    def _open_owner_interface(self, user):
        try:
            self.hide()
            if 'owner' not in active_windows or active_windows['owner'] is None:
                active_windows['owner'] = OwnerController(
                    main_controller=self,
                    current_user_id=user['user_acc_id'],
                    current_username=user['user_acc_username']
                )
            active_windows['owner'].show()
        except Exception as e:
            print(f"Error opening owner interface: {e}")
            self.show_error_message("Could not open owner interface")

    def _open_cashier_interface(self, user):
        try:
            self.hide()
            if 'cashier' not in active_windows or active_windows['cashier'] is None:
                active_windows['cashier'] = CashierController(
                    main_controller=self,
                    database=self.database,  # Make sure this is the correct database instance
                    user_id=user['user_acc_id']
                )
            active_windows['cashier'].show()
        except Exception as e:
            print(f"Error opening cashier interface: {e}")
            self.show_error_message("Could not open cashier interface")
            self.show()  # Show login window again if cashier window fails
    
    def _get_user_data(self, username, role):
        """Helper method to get user data"""
        query = """
            SELECT user_acc_id, user_acc_username 
            FROM user_account 
            WHERE user_acc_username = %s AND user_acc_role = %s
        """
        return self.database.fetch_one(query, (username, role))

    def return_to_landing(self):
        self.hide()
        if 'landing' not in active_windows:
            active_windows['landing'] = LandingWindow()
        active_windows['landing'].show()

    def open_forgot_password(self):
        self.forgot_window = ForgotPasswordWindow(self)
        self.forgot_window.show()
        self.hide()

    def toggle_login_password_visibility(self):
        self.login_pass_visible = not self.login_pass_visible
        self.ui.login_password.setEchoMode(QLineEdit.Normal if self.login_pass_visible else QLineEdit.Password)
        self.set_button_text(self.ui.togglePasswordButton, self.login_pass_visible)

    def set_button_text(self, button, visible):
        button.setText("Hide" if visible else "Show")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle("Login Error")
        msg.setText(message)
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def clear_login_info(self):
        self.clear_input_fields()
        self.ui.login_password.setEchoMode(QLineEdit.Password)
        self.set_button_text(self.ui.togglePasswordButton, False)
        self.login_pass_visible = False

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    active_windows['login'] = Login()
    active_windows['login'].show()
    sys.exit(app.exec_())