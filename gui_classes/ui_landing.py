# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'views/JJ_LANDING_PAGE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JJ_LANDING(object):
    def setupUi(self, JJ_LANDING):
        JJ_LANDING.setObjectName("JJ_LANDING")
        JJ_LANDING.resize(1925, 1035)
        JJ_LANDING.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(JJ_LANDING)
        self.centralwidget.setObjectName("centralwidget")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(-10, 0, 1925, 982))
        self.BG.setText("")
        self.BG.setScaledContents(True)
        self.BG.setObjectName("BG")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(780, 130, 381, 251))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(870, 430, 501, 101))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #d75413; \n"
"font-size:120px;\n"
"font-family: \"Arial Black\", Arial, sans-serif; background: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 440, 311, 101))
        font = QtGui.QFont()
        font.setFamily("Rubik Mono One")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #ebe0cc; \n"
"font-size: 120px;\n"
"font-family: \"Rubik Mono One\", sans-serif; background: transparent;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(600, 550, 721, 51))
        font = QtGui.QFont()
        font.setFamily("Sora Semibold")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #f6f3ee; font-family: \"Sora Semibold\", sans-serif; background: transparent;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(670, 660, 581, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Extrabold")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #ebe0cc; \n"
"font-size:25px;\n"
"font-family: \"Poppins Extrabold\", sans-serif; \n"
"background: transparent;\n"
"")
        self.label_5.setObjectName("label_5")
        self.pushButton_cont_2Login = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cont_2Login.setGeometry(QtCore.QRect(820, 800, 281, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        self.pushButton_cont_2Login.setFont(font)
        self.pushButton_cont_2Login.setStyleSheet("QPushButton { background-color: #f6f3ee; border-radius: 15px; padding: 4px; border: none; color: #374550; font-family: \"MS Shell Dlg 2\", sans-serif; } QPushButton:hover { background-color:#b2423c; color:white; font-weight: 700; text-align: center; }")
        self.pushButton_cont_2Login.setObjectName("pushButton_cont_2Login")
        JJ_LANDING.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JJ_LANDING)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1925, 26))
        self.menubar.setObjectName("menubar")
        JJ_LANDING.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JJ_LANDING)
        self.statusbar.setObjectName("statusbar")
        JJ_LANDING.setStatusBar(self.statusbar)

        self.retranslateUi(JJ_LANDING)
        QtCore.QMetaObject.connectSlotsByName(JJ_LANDING)

    def retranslateUi(self, JJ_LANDING):
        _translate = QtCore.QCoreApplication.translate
        JJ_LANDING.setWindowTitle(_translate("JJ_LANDING", "Inventory and Sales Management System"))
        self.label_2.setText(_translate("JJ_LANDING", "Elevate"))
        self.label_3.setText(_translate("JJ_LANDING", "J&J"))
        self.label_4.setText(_translate("JJ_LANDING", "Elevate Your Space, One Roof at a Time"))
        self.label_5.setText(_translate("JJ_LANDING", "Supply                               Install                               Repair"))
        self.pushButton_cont_2Login.setText(_translate("JJ_LANDING", "Continue to Login"))
import resources.resources_rc
