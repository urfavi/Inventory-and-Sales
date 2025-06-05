from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit
from gui_classes.UI_ForgotPass import Ui_ForgotPass
import re
from models.user_model import get_user_by_username, update_user_password
import bcrypt

class ForgotPasswordWindow(QMainWindow):
    def __init__(self, login_window=None):
        super().__init__()
        self.ui = Ui_ForgotPass()
        self.ui.setupUi(self)

        self.login_window = login_window

        # Hide new pass inputs until verified
        self.ui.setNewPass.setEnabled(False)
        self.ui.confirmNewPass.setEnabled(False)
        self.ui.pushButton_confirmPass_reset.setEnabled(False)
        self.ui.securityAnswerField.setEnabled(False)

        # Set password fields as hidden
        self.ui.setNewPass.setEchoMode(QLineEdit.Password)
        self.ui.confirmNewPass.setEchoMode(QLineEdit.Password)

        # Connect buttons
        self.ui.pushButton_checkUsername.clicked.connect(self.check_username)
        self.ui.pushButton_confirmPass_reset.clicked.connect(self.reset_password)
        self.ui.pushButton_cancelPass.clicked.connect(self.back_to_login)
        self.ui.pushButton_xtolanding_forgotpass_2.clicked.connect(self.back_to_login)

        self.ui.toggleNewPass.clicked.connect(self.toggle_new_password_visibility)
        self.ui.toggleConfirmPass.clicked.connect(self.toggle_confirm_new_password_visibility)

        self.new_pass_visible = False
        self.confirm_pass_visible = False

        self.set_button_text(self.ui.toggleNewPass, False)
        self.set_button_text(self.ui.toggleConfirmPass, False)

        self.stored_hashed_answer = None  # to hold hashed answer

    def set_button_text(self, button, visible):
        button.setText("Hide" if visible else "Show")

    def check_username(self):
        try:
            username = self.ui.checkUser.text().strip()
            user = get_user_by_username(username)

            if user:
                _, _, role, security_question, security_answer = user  # unpack user tuple

                if role.upper() != "OWNER":
                    QMessageBox.warning(self, "Access Denied", 
                        "Only OWNER accounts can reset passwords.")
                    return

                if not security_question or not security_answer:
                    QMessageBox.warning(self, "Unavailable", 
                        "Security question is not set for this account.")
                    return

                # Display security question
                self.ui.label_secQuestionText.setText("Security Question:")
                self.ui.label_secQuestion.setText(security_question)
                self.ui.securityAnswerField.setEnabled(True)
                self.ui.setNewPass.setEnabled(True)
                self.ui.confirmNewPass.setEnabled(True)
                self.ui.pushButton_confirmPass_reset.setEnabled(True)

                self.stored_hashed_answer = security_answer
                QMessageBox.information(self, "Continue", "Please answer your security question.")
            else:
                QMessageBox.warning(self, "Error", "Username not found.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Something went wrong:\n{str(e)}")

    def reset_password(self):
        username = self.ui.checkUser.text().strip()
        answer = self.ui.securityAnswerField.text().strip().lower()  # normalize input answer
        new_pass = self.ui.setNewPass.text()
        confirm_pass = self.ui.confirmNewPass.text()

        if not self.stored_hashed_answer:
            QMessageBox.critical(self, "Error", "No stored security answer. Start again.")
            return

        stored_hash = self.stored_hashed_answer.strip()  # clean stored hash

        # Debug print to help you see what is compared
        print(f"User input answer: '{answer}'")
        print(f"Stored hashed answer: '{stored_hash}'")

        if not bcrypt.checkpw(answer.encode(), stored_hash.encode()):
            QMessageBox.warning(self, "Error", "Incorrect security answer.")
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(self, "Error", "New passwords don't match.")
            return

        if len(new_pass) < 8:
            QMessageBox.warning(self, "Error", "Password must be at least 8 characters.")
            return

        if not (re.search(r"[A-Z]", new_pass) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_pass)):
            QMessageBox.warning(self, "Error", "Password must contain at least one uppercase letter and one special character.")
            return

        try:
            hashed = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt()).decode('utf-8')
            if update_user_password(username, hashed):
                QMessageBox.information(self, "Success", "Password updated successfully!")
                self.back_to_login()
            else:
                QMessageBox.critical(self, "Error", "Failed to update password.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Technical error:\n{str(e)}")

    def back_to_login(self):
        if self.login_window:
            self.login_window.show()
        self.close()

    def toggle_new_password_visibility(self):
        self.new_pass_visible = not self.new_pass_visible
        self.ui.setNewPass.setEchoMode(QLineEdit.Normal if self.new_pass_visible else QLineEdit.Password)
        self.set_button_text(self.ui.toggleNewPass, self.new_pass_visible)

    def toggle_confirm_new_password_visibility(self):
        self.confirm_pass_visible = not self.confirm_pass_visible
        self.ui.confirmNewPass.setEchoMode(QLineEdit.Normal if self.confirm_pass_visible else QLineEdit.Password)
        self.set_button_text(self.ui.toggleConfirmPass, self.confirm_pass_visible)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = ForgotPasswordWindow()
    win.show()
    sys.exit(app.exec_())
