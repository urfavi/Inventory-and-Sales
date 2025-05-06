from PyQt5 import QtCore, QtGui, QtWidgets
import resources.jj_owner_resources_rc

# LOGIN--------------------------------------------------------------------------------------------------------
class Ui_LOGIN(object):  # THIS PART CORRESPONDS TO class Login(QMainWindow) in main_app.py
    def setupUi(self, OwnrLOGIN):
        OwnrLOGIN.setObjectName("OwnrLOGIN")
        OwnrLOGIN.resize(1925, 1033)
        OwnrLOGIN.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(OwnrLOGIN)
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
        self.checkBox_rememberme = QtWidgets.QCheckBox(self.frame)
        self.checkBox_rememberme.setGeometry(QtCore.QRect(60, 580, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.checkBox_rememberme.setFont(font)
        self.checkBox_rememberme.setStyleSheet("color: #022162;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.checkBox_rememberme.setObjectName("checkBox_rememberme")
        self.pushButton_xtolanding_owner = QtWidgets.QPushButton(self.frame)
        self.pushButton_xtolanding_owner.setGeometry(QtCore.QRect(830, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_xtolanding_owner.setFont(font)
        self.pushButton_xtolanding_owner.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_xtolanding_owner.setObjectName("pushButton_xtolanding_owner")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 90, 261, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(47)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(60, 420, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_9.setObjectName("label_9")
        self.ownr_login_usrname = QtWidgets.QLineEdit(self.frame)
        self.ownr_login_usrname.setGeometry(QtCore.QRect(42, 310, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.ownr_login_usrname.setFont(font)
        self.ownr_login_usrname.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ownr_login_usrname.setObjectName("ownr_login_usrname")
        self.ownr_login_password = QtWidgets.QLineEdit(self.frame)
        self.ownr_login_password.setGeometry(QtCore.QRect(40, 500, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.ownr_login_password.setFont(font)
        self.ownr_login_password.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.ownr_login_password.setObjectName("ownr_login_password")
        self.pushButton_LOGIN = QtWidgets.QPushButton(self.frame)
        self.pushButton_LOGIN.setGeometry(QtCore.QRect(42, 680, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_LOGIN.setFont(font)
        self.pushButton_LOGIN.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_LOGIN.setObjectName("pushButton_LOGIN")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(340, 750, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #022162;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_10.setObjectName("label_10")
        self.pushButton_signup = QtWidgets.QPushButton(self.frame)
        self.pushButton_signup.setGeometry(QtCore.QRect(410, 790, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_signup.setFont(font)
        self.pushButton_signup.setStyleSheet("border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: transparent; \n"
"color: #022162;")
        self.pushButton_signup.setObjectName("pushButton_signup")
        self.pushButton_forgotPass_login_page = QtWidgets.QPushButton(self.frame)
        self.pushButton_forgotPass_login_page.setGeometry(QtCore.QRect(670, 570, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_forgotPass_login_page.setFont(font)
        self.pushButton_forgotPass_login_page.setStyleSheet("border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: transparent; \n"
"color: #d75413;")
        self.pushButton_forgotPass_login_page.setObjectName("pushButton_forgotPass_login_page")
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
        OwnrLOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OwnrLOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1925, 26))
        self.menubar.setObjectName("menubar")
        OwnrLOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OwnrLOGIN)
        self.statusbar.setObjectName("statusbar")
        OwnrLOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(OwnrLOGIN)
        QtCore.QMetaObject.connectSlotsByName(OwnrLOGIN)

    def retranslateUi(self, OwnrLOGIN):
        _translate = QtCore.QCoreApplication.translate
        OwnrLOGIN.setWindowTitle(_translate("OwnrLOGIN", "Inventory and Sales Management System"))
        self.checkBox_rememberme.setText(_translate("OwnrLOGIN", "Remember me"))
        self.pushButton_xtolanding_owner.setText(_translate("OwnrLOGIN", "x"))
        self.label_2.setText(_translate("OwnrLOGIN", "Login"))
        self.label_3.setText(_translate("OwnrLOGIN", "Username"))
        self.label_9.setText(_translate("OwnrLOGIN", "Password"))
        self.ownr_login_usrname.setPlaceholderText(_translate("OwnrLOGIN", "Enter your username"))
        self.ownr_login_password.setPlaceholderText(_translate("OwnrLOGIN", "Enter your password"))
        self.pushButton_LOGIN.setText(_translate("OwnrLOGIN", "Login"))
        self.label_10.setText(_translate("OwnrLOGIN", "Don\'t have an account?"))
        self.pushButton_signup.setText(_translate("OwnrLOGIN", "Sign Up"))
        self.pushButton_forgotPass_login_page.setText(_translate("OwnrLOGIN", "Forgot Password?"))
        self.label_18.setText(_translate("OwnrLOGIN", "J & J Roofsteel and Gutter Supply"))
        self.label_6.setText(_translate("OwnrLOGIN", "Moalboal Branch"))
        self.label_11.setText(_translate("OwnrLOGIN", "Supply       |         Install       |         Repair    "))
    def setupUi(self, LOGIN):
        LOGIN.setObjectName("LOGIN")
        LOGIN.resize(1925, 1033)
        LOGIN.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(LOGIN)
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
        self.checkBox_rememberme = QtWidgets.QCheckBox(self.frame)
        self.checkBox_rememberme.setGeometry(QtCore.QRect(60, 580, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.checkBox_rememberme.setFont(font)
        self.checkBox_rememberme.setStyleSheet("color: #022162;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.checkBox_rememberme.setObjectName("checkBox_rememberme")
        self.pushButton_xtolanding = QtWidgets.QPushButton(self.frame)
        self.pushButton_xtolanding.setGeometry(QtCore.QRect(830, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_xtolanding.setFont(font)
        self.pushButton_xtolanding.setStyleSheet("border-radius: 13px; \n"
"padding: 1px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_xtolanding.setObjectName("pushButton_xtolanding")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(350, 90, 261, 131))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(47)
        font.setBold(True)
        font.setWeight(87)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 240, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(87)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(60, 420, 181, 71))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #022162;\n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_9.setObjectName("label_9")
        self.login_usrname = QtWidgets.QLineEdit(self.frame)
        self.login_usrname.setGeometry(QtCore.QRect(42, 310, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.login_usrname.setFont(font)
        self.login_usrname.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.login_usrname.setObjectName("login_usrname")
        self.login_password = QtWidgets.QLineEdit(self.frame)
        self.login_password.setGeometry(QtCore.QRect(40, 500, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.login_password.setFont(font)
        self.login_password.setStyleSheet("border: 2px solid #022162; \n"
"border-radius: 25px; \n"
"padding: 5px;\n"
"font-family: \"Verdana\", sans-serif; ")
        self.login_password.setObjectName("login_password")
        self.pushButton_LOGIN = QtWidgets.QPushButton(self.frame)
        self.pushButton_LOGIN.setGeometry(QtCore.QRect(42, 680, 851, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(87)
        self.pushButton_LOGIN.setFont(font)
        self.pushButton_LOGIN.setStyleSheet("border: 2px solid #374550; \n"
"border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: #374550; \n"
"color: white;")
        self.pushButton_LOGIN.setObjectName("pushButton_LOGIN")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(280, 740, 401, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: #022162;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_10.setObjectName("label_10")
        self.pushButton_forgotPass_login_page = QtWidgets.QPushButton(self.frame)
        self.pushButton_forgotPass_login_page.setGeometry(QtCore.QRect(360, 840, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(87)
        self.pushButton_forgotPass_login_page.setFont(font)
        self.pushButton_forgotPass_login_page.setStyleSheet("border-radius: 25px; \n"
"padding: 5px; \n"
"font-weight: 700;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background-color: transparent; \n"
"color: #022162;")
        self.pushButton_forgotPass_login_page.setObjectName("pushButton_forgotPass_login_page")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(390, 790, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: #022162;\n"
"font-family: \"Verdana\", sans-serif; \n"
"background: transparent;")
        self.label_12.setObjectName("label_12")
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
        LOGIN.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LOGIN)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1925, 26))
        self.menubar.setObjectName("menubar")
        LOGIN.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LOGIN)
        self.statusbar.setObjectName("statusbar")
        LOGIN.setStatusBar(self.statusbar)

        self.retranslateUi(LOGIN)
        QtCore.QMetaObject.connectSlotsByName(LOGIN)

    def retranslateUi(self, LOGIN):
        _translate = QtCore.QCoreApplication.translate
        LOGIN.setWindowTitle(_translate("LOGIN", "Inventory and Sales Management System"))
        self.checkBox_rememberme.setText(_translate("LOGIN", "Remember me"))
        self.pushButton_xtolanding.setText(_translate("LOGIN", "x"))
        self.label_2.setText(_translate("LOGIN", "Login"))
        self.label_3.setText(_translate("LOGIN", "Username"))
        self.label_9.setText(_translate("LOGIN", "Password"))
        self.login_usrname.setPlaceholderText(_translate("LOGIN", "Enter your username"))
        self.login_password.setPlaceholderText(_translate("LOGIN", "Enter your password"))
        self.pushButton_LOGIN.setText(_translate("LOGIN", "Login"))
        self.label_10.setText(_translate("LOGIN", "Forgot password? Only available for"))
        self.pushButton_forgotPass_login_page.setText(_translate("LOGIN", "Reset Password"))
        self.label_12.setText(_translate("LOGIN", " Shop Owners"))
        self.label_18.setText(_translate("LOGIN", "J & J Roofsteel and Gutter Supply"))
        self.label_6.setText(_translate("LOGIN", "Moalboal Branch"))
        self.label_11.setText(_translate("LOGIN", "Supply       |         Install       |         Repair    "))
import resources.jj_owner_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LOGIN = QtWidgets.QMainWindow()
    ui = Ui_LOGIN()
    ui.setupUi(LOGIN)
    LOGIN.show()
    sys.exit(app.exec_())