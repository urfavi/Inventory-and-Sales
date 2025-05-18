from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtCore import QSettings
from gui_classes.ui_login import Ui_LOGIN
from gui_classes.ui_forgotPass import Ui_ForgotPass
from gui_classes.ui_landing import Ui_JJ_LANDING
from controllers.auth_controller import authenticate_user
from controllers.owner_controller import OwnerInterface
from controllers.forgotpass_controller import ForgotPasswordWindow
from cryptography.fernet import Fernet

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
            # Clear the fields before showing again
            active_windows['login'].clear_login_info()
        active_windows['login'].show()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LOGIN()
        self.ui.setupUi(self)

        self.login_pass_visible = False
        self.ui.login_password.setEchoMode(QLineEdit.Password)
        self.set_button_text(self.ui.togglePasswordButton, self.login_pass_visible)

        try:
            self.settings = QSettings("YourApp", "LoginCredentials")
            self.cipher = self._initialize_encryption()
            # Always load saved credentials at init
            self._load_saved_credentials()
        except Exception as e:
            print(f"Initialization error: {e}")
            self.settings = None
            self.cipher = None

        # Connect signals
        self.ui.pushButton_LOGIN.clicked.connect(self.open_owner_interface)
        self.ui.pushButton_xtolanding.clicked.connect(self.return_to_landing)
        self.ui.pushButton_forgotPass_login_page.clicked.connect(self.open_forgot_password)
        self.ui.togglePasswordButton.clicked.connect(self.toggle_login_password_visibility)

        if hasattr(self.ui, 'pushButton_clearLogins'):
            self.ui.pushButton_clearLogins.clicked.connect(self.clear_input_fields)
        if hasattr(self.ui, 'checkBox_rememberme'):
            self.ui.checkBox_rememberme.stateChanged.connect(self._handle_remember_me_change)

    def _initialize_encryption(self):
        """Initialize encryption key"""
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
        """Load saved credentials if available"""
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
                # Check the checkbox if credentials loaded
                if hasattr(self.ui, 'checkBox_rememberme'):
                    self.ui.checkBox_rememberme.setChecked(True)
            else:
                # No saved credentials — uncheck box
                if hasattr(self.ui, 'checkBox_rememberme'):
                    self.ui.checkBox_rememberme.setChecked(False)
        except Exception as e:
            print(f"Credential load error: {e}")
            self.clear_saved_credentials()

    def clear_saved_credentials(self):
        """Safely clear stored credentials"""
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
        # Optional: reload saved credentials on show if checkbox checked
        if hasattr(self.ui, 'checkBox_rememberme') and self.ui.checkBox_rememberme.isChecked():
            self._load_saved_credentials()

    def clear_input_fields(self):
        """Clear username and password input fields only"""
        self.ui.login_usrname.clear()
        self.ui.login_password.clear()

    def _handle_remember_me_change(self, state):
        """Clear credentials only when user unchecks Remember Me"""
        if state == 0:
            self.clear_saved_credentials()

    def _save_credentials(self, username, password):
        """Encrypt and save credentials"""
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

    def open_owner_interface(self):
        try:
            username = self.ui.login_usrname.text()
            password = self.ui.login_password.text()
            if authenticate_user(username, password):
                if hasattr(self.ui, 'checkBox_rememberme') and self.ui.checkBox_rememberme.isChecked():
                    self._save_credentials(username, password)
                self.close()
                active_windows['owner'] = OwnerInterface()
                active_windows['owner'].show()
            else:
                self.show_error_message("Invalid username or password!")
        except Exception as e:
            print(f"Login crash: {e}")
            self.show_error_message("Login failed. Check console.")

    def return_to_landing(self):
        self.hide()
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
        """External call to reset inputs without affecting saved credentials"""
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
