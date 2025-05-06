from PyQt5 import QtCore, QtGui, QtWidgets
import resources.jj_owner_resources_rc

# FORGOT PASSWORD-----------------------------------------------------------------------------------------------------
class Ui_ForgotPass(object):  # THIS PART CORRESPONDS TO class ForgotPassword(QMainWindow) in main_app.py
    def setupUi(self, ForgotPass):
        ForgotPass.setObjectName("ForgotPass")
        ForgotPass.resize(1925, 1033)
        ForgotPass.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(ForgotPass)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.PIC = QtWidgets.QLabel(self.centralwidget)
        self.PIC.setGeometry(QtCore.QRect(0, 0, 1921, 982))
        self.PIC.setMinimumSize(QtCore.QSize(100, 40))
        self.PIC.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PIC.setText("")
        self.PIC.setPixmap(QtGui.QPixmap(":/resources/images/login_pic.png"))
        self.PIC.setScaledContents(True)
        self.PIC.setObjectName("PIC")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 130, 451, 331))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resources/images/J&J logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(990, 0, 931, 982))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_xtolanding_forgotpass = QtWidgets.QPushButton(self.frame)
        self.pushButton_xtolanding_forgotpass.setGeometry(QtCore.QRect(830, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_xtolanding_forgotpass.setFont(font)
        self.pushButton_xtolanding_forgotpass.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_xtolanding_forgotpass.setObjectName("pushButton_xtolanding_forgotpass")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(150, 30, 681, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(60, 70, 761, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_10.setObjectName("label_10")
        self.ResetPass_enter_username = QtWidgets.QLineEdit(self.frame)
        self.ResetPass_enter_username.setGeometry(QtCore.QRect(40, 160, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.ResetPass_enter_username.setFont(font)
        self.ResetPass_enter_username.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ResetPass_enter_username.setPlaceholderText("")
        self.ResetPass_enter_username.setObjectName("ResetPass_enter_username")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(60, 200, 771, 101))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_12.setObjectName("label_12")
        self.ResetPass_enter_email = QtWidgets.QLineEdit(self.frame)
        self.ResetPass_enter_email.setGeometry(QtCore.QRect(40, 280, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.ResetPass_enter_email.setFont(font)
        self.ResetPass_enter_email.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ResetPass_enter_email.setPlaceholderText("")
        self.ResetPass_enter_email.setObjectName("ResetPass_enter_email")
        self.pushButton_ResetPass_send_code = QtWidgets.QPushButton(self.frame)
        self.pushButton_ResetPass_send_code.setGeometry(QtCore.QRect(650, 360, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_ResetPass_send_code.setFont(font)
        self.pushButton_ResetPass_send_code.setStyleSheet("QPushButton {\n"
"background-color: #374550;\n"
"border-radius: 15px; \n"
"padding: 4px;\n"
"border: none;\n"
"color: white;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;\n"
"                }\n"
"QPushButton:hover {\n"
"                    background-color:black;\n"
"                    color:white;\n"
"font-weight: 700;\n"
"                    text-align: center;\n"
"                }\n"
"")
        self.pushButton_ResetPass_send_code.setObjectName("pushButton_ResetPass_send_code")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(60, 390, 771, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_13.setObjectName("label_13")
        self.ResetPass_enter_code = QtWidgets.QLineEdit(self.frame)
        self.ResetPass_enter_code.setGeometry(QtCore.QRect(40, 460, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.ResetPass_enter_code.setFont(font)
        self.ResetPass_enter_code.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ResetPass_enter_code.setPlaceholderText("")
        self.ResetPass_enter_code.setObjectName("ResetPass_enter_code")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(60, 590, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_14.setObjectName("label_14")
        self.setNewPass_enter_new_pass = QtWidgets.QLineEdit(self.frame)
        self.setNewPass_enter_new_pass.setGeometry(QtCore.QRect(40, 640, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.setNewPass_enter_new_pass.setFont(font)
        self.setNewPass_enter_new_pass.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.setNewPass_enter_new_pass.setPlaceholderText("")
        self.setNewPass_enter_new_pass.setObjectName("setNewPass_enter_new_pass")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(60, 720, 791, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_15.setObjectName("label_15")
        self.setNewPass_confirmNewPass = QtWidgets.QLineEdit(self.frame)
        self.setNewPass_confirmNewPass.setGeometry(QtCore.QRect(40, 760, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.setNewPass_confirmNewPass.setFont(font)
        self.setNewPass_confirmNewPass.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.setNewPass_confirmNewPass.setPlaceholderText("")
        self.setNewPass_confirmNewPass.setObjectName("setNewPass_confirmNewPass")
        self.pushButton_ChangePass = QtWidgets.QPushButton(self.frame)
        self.pushButton_ChangePass.setGeometry(QtCore.QRect(40, 860, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_ChangePass.setFont(font)
        self.pushButton_ChangePass.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_ChangePass.setObjectName("pushButton_ChangePass")
        self.pushButton_ResetPass_confirm_code = QtWidgets.QPushButton(self.frame)
        self.pushButton_ResetPass_confirm_code.setGeometry(QtCore.QRect(650, 540, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_ResetPass_confirm_code.setFont(font)
        self.pushButton_ResetPass_confirm_code.setStyleSheet("QPushButton {\n"
"background-color: #374550;\n"
"border-radius: 15px; \n"
"padding: 4px;\n"
"border: none;\n"
"color: white;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;\n"
"                }\n"
"QPushButton:hover {\n"
"                    background-color:black;\n"
"                    color:white;\n"
"font-weight: 700;\n"
"                    text-align: center;\n"
"                }\n"
"")
        self.pushButton_ResetPass_confirm_code.setObjectName("pushButton_ResetPass_confirm_code")
        self.pushButton_xtolanding_forgotpass.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.ResetPass_enter_username.raise_()
        self.label_12.raise_()
        self.ResetPass_enter_email.raise_()
        self.label_13.raise_()
        self.ResetPass_enter_code.raise_()
        self.label_14.raise_()
        self.setNewPass_enter_new_pass.raise_()
        self.label_15.raise_()
        self.setNewPass_confirmNewPass.raise_()
        self.pushButton_ChangePass.raise_()
        self.pushButton_ResetPass_send_code.raise_()
        self.pushButton_ResetPass_confirm_code.raise_()
        self.jframe = QtWidgets.QFrame(self.centralwidget)
        self.jframe.setGeometry(QtCore.QRect(-10, 460, 951, 431))
        self.jframe.setStyleSheet("background: transparent;")
        self.jframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.jframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.jframe.setObjectName("jframe")
        self.label_18 = QtWidgets.QLabel(self.jframe)
        self.label_18.setGeometry(QtCore.QRect(120, 20, 771, 111))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(87)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: #ffffff;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_18.setObjectName("label_18")
        self.label_6 = QtWidgets.QLabel(self.jframe)
        self.label_6.setGeometry(QtCore.QRect(340, 110, 291, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(87)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #ffffff;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.jframe)
        self.label_11.setGeometry(QtCore.QRect(170, 250, 631, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(87)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: #fff2bd; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent; \n"
"")
        self.label_11.setObjectName("label_11")
        ForgotPass.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ForgotPass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1925, 26))
        self.menubar.setObjectName("menubar")
        ForgotPass.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ForgotPass)
        self.statusbar.setObjectName("statusbar")
        ForgotPass.setStatusBar(self.statusbar)

        self.retranslateUi(ForgotPass)
        QtCore.QMetaObject.connectSlotsByName(ForgotPass)

    def retranslateUi(self, ForgotPass):
        _translate = QtCore.QCoreApplication.translate
        ForgotPass.setWindowTitle(_translate("ForgotPass", "Inventory and Sales Management System"))
        self.pushButton_xtolanding_forgotpass.setText(_translate("ForgotPass", "x"))
        self.label_9.setText(_translate("ForgotPass", "Reset Password"))
        self.label_10.setText(_translate("ForgotPass", "Username"))
        self.label_12.setText(_translate("ForgotPass", "Email"))
        self.pushButton_ResetPass_send_code.setText(_translate("ForgotPass", "Send code to Email"))
        self.label_13.setText(_translate("ForgotPass", "Input Code"))
        self.label_14.setText(_translate("ForgotPass", "Set new password"))
        self.label_15.setText(_translate("ForgotPass", "Confirm new password"))
        self.pushButton_ChangePass.setText(_translate("ForgotPass", "CHANGE PASSWORD"))
        self.pushButton_ResetPass_confirm_code.setText(_translate("ForgotPass", "Confirm Code"))
        self.label_18.setText(_translate("ForgotPass", "J & J Roofsteel and Gutter Supply"))
        self.label_6.setText(_translate("ForgotPass", "Moalboal Branch"))
        self.label_11.setText(_translate("ForgotPass", "Supply       |         Install       |         Repair    "))
import resources.jj_owner_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ForgotPass = QtWidgets.QMainWindow()
    ui = Ui_ForgotPass()
    ui.setupUi(ForgotPass)
    ForgotPass.show()
    sys.exit(app.exec_())