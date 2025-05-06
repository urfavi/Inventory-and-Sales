from PyQt5 import QtCore, QtGui, QtWidgets
import resources.jj_owner_resources_rc

# OWNER INTERFACE----------------------------------------------------------------------------------------------------
class Ui_OWNER(object):   # THIS PART CORRESPONDS TO class OwnerInterface(QMainWindow) in main_app.py
    def setupUi(self, OWNER):
        OWNER.setObjectName("OWNER")
        OWNER.resize(1921, 1005)
        self.Owner_centralwidget = QtWidgets.QWidget(OWNER)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Owner_centralwidget.setFont(font)
        self.Owner_centralwidget.setObjectName("Owner_centralwidget")
        self.LeftMenuBar = QtWidgets.QFrame(self.Owner_centralwidget)
        self.LeftMenuBar.setGeometry(QtCore.QRect(-1, -1, 301, 981))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LeftMenuBar.setFont(font)
        self.LeftMenuBar.setStyleSheet("\n"
"background-color:#374550;\n"
"")
        self.LeftMenuBar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LeftMenuBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftMenuBar.setObjectName("LeftMenuBar")
        self.JJelevate_text = QtWidgets.QLabel(self.LeftMenuBar)
        self.JJelevate_text.setGeometry(QtCore.QRect(30, 240, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.JJelevate_text.setFont(font)
        self.JJelevate_text.setStyleSheet("color: #f6f3ee; ")
        self.JJelevate_text.setScaledContents(True)
        self.JJelevate_text.setObjectName("JJelevate_text")
        self.Logo = QtWidgets.QLabel(self.LeftMenuBar)
        self.Logo.setGeometry(QtCore.QRect(30, 50, 241, 171))
        self.Logo.setText("")
        self.Logo.setPixmap(QtGui.QPixmap(":/JJimages/JJLOGO.png"))
        self.Logo.setScaledContents(True)
        self.Logo.setAlignment(QtCore.Qt.AlignCenter)
        self.Logo.setObjectName("Logo")
        self.pushButton_Dashboard = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_Dashboard.setGeometry(QtCore.QRect(30, 310, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Dashboard.setFont(font)
        self.pushButton_Dashboard.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/JJimages/dashboard_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Dashboard.setIcon(icon)
        self.pushButton_Dashboard.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_Dashboard.setObjectName("pushButton_Dashboard")
        self.pushButton_Inventory = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_Inventory.setGeometry(QtCore.QRect(30, 390, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Inventory.setFont(font)
        self.pushButton_Inventory.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/JJimages/inventory_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Inventory.setIcon(icon1)
        self.pushButton_Inventory.setIconSize(QtCore.QSize(55, 50))
        self.pushButton_Inventory.setObjectName("pushButton_Inventory")
        self.pushButton_Orders = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_Orders.setGeometry(QtCore.QRect(30, 470, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Orders.setFont(font)
        self.pushButton_Orders.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/JJimages/orders_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Orders.setIcon(icon2)
        self.pushButton_Orders.setIconSize(QtCore.QSize(51, 48))
        self.pushButton_Orders.setObjectName("pushButton_Orders")
        self.pushButton_Sales = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_Sales.setGeometry(QtCore.QRect(30, 550, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Sales.setFont(font)
        self.pushButton_Sales.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/JJimages/sales_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Sales.setIcon(icon3)
        self.pushButton_Sales.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_Sales.setObjectName("pushButton_Sales")
        self.pushButton_Account = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_Account.setGeometry(QtCore.QRect(30, 630, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Account.setFont(font)
        self.pushButton_Account.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/JJimages/account_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Account.setIcon(icon4)
        self.pushButton_Account.setIconSize(QtCore.QSize(52, 50))
        self.pushButton_Account.setObjectName("pushButton_Account")
        self.pushButton_LogOut = QtWidgets.QPushButton(self.LeftMenuBar)
        self.pushButton_LogOut.setGeometry(QtCore.QRect(30, 890, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_LogOut.setFont(font)
        self.pushButton_LogOut.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: white;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-size: 14;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: left;\n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#8d2721;\n"
"color:white;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #8d2721;\n"
"    color: white;\n"
"font-weight: 500;\n"
"}\n"
"")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/JJimages/logout_icon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LogOut.setIcon(icon5)
        self.pushButton_LogOut.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_LogOut.setObjectName("pushButton_LogOut")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Owner_centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(300, 0, 1621, 1033))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Dashboard_page = QtWidgets.QWidget()
        self.Dashboard_page.setObjectName("Dashboard_page")
        self.dashboard_inview = QtWidgets.QWidget(self.Dashboard_page)
        self.dashboard_inview.setGeometry(QtCore.QRect(0, -6, 1925, 1005))
        self.dashboard_inview.setStyleSheet("background-color:#ffffff;")
        self.dashboard_inview.setObjectName("dashboard_inview")
        self.dashboard_bestsellers_box = QtWidgets.QFrame(self.dashboard_inview)
        self.dashboard_bestsellers_box.setGeometry(QtCore.QRect(40, 410, 741, 561))
        self.dashboard_bestsellers_box.setStyleSheet("#chartd\n"
"{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.dashboard_bestsellers_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dashboard_bestsellers_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dashboard_bestsellers_box.setObjectName("dashboard_bestsellers_box")
        self.frameBestSellersChart = QtWidgets.QFrame(self.dashboard_bestsellers_box)
        self.frameBestSellersChart.setGeometry(QtCore.QRect(20, 80, 691, 431))
        self.frameBestSellersChart.setStyleSheet("background-color: white;\n"
"border: none;\n"
"")
        self.frameBestSellersChart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBestSellersChart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBestSellersChart.setObjectName("frameBestSellersChart")
        self.bestsellersbox = QtWidgets.QLabel(self.dashboard_bestsellers_box)
        self.bestsellersbox.setGeometry(QtCore.QRect(0, 0, 741, 561))
        self.bestsellersbox.setStyleSheet("\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 15;\n"
"    padding: 10px;\n"
"\n"
"")
        self.bestsellersbox.setText("")
        self.bestsellersbox.setObjectName("bestsellersbox")
        self.label_10 = QtWidgets.QLabel(self.dashboard_bestsellers_box)
        self.label_10.setGeometry(QtCore.QRect(210, 10, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background: transparent;")
        self.label_10.setObjectName("label_10")
        self.btnViewSalesReport = QtWidgets.QPushButton(self.dashboard_bestsellers_box)
        self.btnViewSalesReport.setGeometry(QtCore.QRect(220, 520, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setUnderline(True)
        self.btnViewSalesReport.setFont(font)
        self.btnViewSalesReport.setStyleSheet("QPushButton{color: blue;\n"
"font-family: \'Poppins\', Medium;\n"
"text-decoration: underline;\n"
"border: none;\n"
"background: transparent;}\n"
"QPushButton:hover {\n"
"color:#8d2721;\n"
"}\n"
"")
        self.btnViewSalesReport.setObjectName("btnViewSalesReport")
        self.bestsellersbox.raise_()
        self.frameBestSellersChart.raise_()
        self.label_10.raise_()
        self.btnViewSalesReport.raise_()
        self.calendaricon = QtWidgets.QLabel(self.dashboard_inview)
        self.calendaricon.setGeometry(QtCore.QRect(30, 40, 191, 121))
        self.calendaricon.setText("")
        self.calendaricon.setPixmap(QtGui.QPixmap(":/JJimages/dashboardcalendar.png"))
        self.calendaricon.setScaledContents(True)
        self.calendaricon.setObjectName("calendaricon")
        self.Todays_Sales_box = QtWidgets.QFrame(self.dashboard_inview)
        self.Todays_Sales_box.setGeometry(QtCore.QRect(40, 220, 511, 171))
        self.Todays_Sales_box.setStyleSheet("#salesbox\n"
"{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"    background-color: white;\n"
"    border: 2px solid black;\n"
"    padding: 10px;\n"
"}")
        self.Todays_Sales_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Todays_Sales_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Todays_Sales_box.setObjectName("Todays_Sales_box")
        self.salesbox = QtWidgets.QLabel(self.Todays_Sales_box)
        self.salesbox.setGeometry(QtCore.QRect(4, 5, 501, 161))
        self.salesbox.setStyleSheet("\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 15;\n"
"    padding: 10px;\n"
"\n"
"")
        self.salesbox.setText("")
        self.salesbox.setObjectName("salesbox")
        self.sales_hand_icon = QtWidgets.QLabel(self.Todays_Sales_box)
        self.sales_hand_icon.setGeometry(QtCore.QRect(10, 30, 101, 71))
        self.sales_hand_icon.setStyleSheet("background: transparent;")
        self.sales_hand_icon.setText("")
        self.sales_hand_icon.setPixmap(QtGui.QPixmap(":/JJimages/moneyhand_icon.svg"))
        self.sales_hand_icon.setScaledContents(True)
        self.sales_hand_icon.setObjectName("sales_hand_icon")
        self.up_sales = QtWidgets.QLabel(self.Todays_Sales_box)
        self.up_sales.setGeometry(QtCore.QRect(420, 50, 71, 51))
        self.up_sales.setStyleSheet("background: transparent;")
        self.up_sales.setText("")
        self.up_sales.setPixmap(QtGui.QPixmap(":/JJimages/up.png"))
        self.up_sales.setScaledContents(True)
        self.up_sales.setObjectName("up_sales")
        self.value_Tod_sales = QtWidgets.QLabel(self.Todays_Sales_box)
        self.value_Tod_sales.setGeometry(QtCore.QRect(100, 20, 321, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.value_Tod_sales.setFont(font)
        self.value_Tod_sales.setStyleSheet("color:#c9cc7f;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;\n"
"background: transparent;\n"
"")
        self.value_Tod_sales.setAlignment(QtCore.Qt.AlignCenter)
        self.value_Tod_sales.setObjectName("value_Tod_sales")
        self.label_4 = QtWidgets.QLabel(self.Todays_Sales_box)
        self.label_4.setGeometry(QtCore.QRect(160, 120, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #004aad;\n"
"font-family: \'Poppins\', Medium;\n"
"background: transparent;")
        self.label_4.setObjectName("label_4")
        self.low_inventory = QtWidgets.QFrame(self.dashboard_inview)
        self.low_inventory.setGeometry(QtCore.QRect(830, 410, 741, 561))
        self.low_inventory.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.low_inventory.setFrameShadow(QtWidgets.QFrame.Raised)
        self.low_inventory.setObjectName("low_inventory")
        self.lowstockbox = QtWidgets.QLabel(self.low_inventory)
        self.lowstockbox.setGeometry(QtCore.QRect(0, 0, 741, 561))
        self.lowstockbox.setStyleSheet("\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 15;\n"
"    padding: 10px;\n"
"\n"
"")
        self.lowstockbox.setText("")
        self.lowstockbox.setObjectName("lowstockbox")
        self.dotline_4 = QtWidgets.QLabel(self.low_inventory)
        self.dotline_4.setGeometry(QtCore.QRect(0, 470, 741, 151))
        self.dotline_4.setStyleSheet("background: transparent;")
        self.dotline_4.setText("")
        self.dotline_4.setPixmap(QtGui.QPixmap(":/JJimages/dottedline.png"))
        self.dotline_4.setScaledContents(True)
        self.dotline_4.setObjectName("dotline_4")
        self.dotline_3 = QtWidgets.QLabel(self.low_inventory)
        self.dotline_3.setGeometry(QtCore.QRect(0, 390, 741, 171))
        self.dotline_3.setStyleSheet("background: transparent;")
        self.dotline_3.setText("")
        self.dotline_3.setPixmap(QtGui.QPixmap(":/JJimages/dottedline.png"))
        self.dotline_3.setScaledContents(True)
        self.dotline_3.setObjectName("dotline_3")
        self.dotline_2 = QtWidgets.QLabel(self.low_inventory)
        self.dotline_2.setGeometry(QtCore.QRect(0, 310, 741, 191))
        self.dotline_2.setStyleSheet("background: transparent;")
        self.dotline_2.setText("")
        self.dotline_2.setPixmap(QtGui.QPixmap(":/JJimages/dottedline.png"))
        self.dotline_2.setScaledContents(True)
        self.dotline_2.setObjectName("dotline_2")
        self.dotline_1 = QtWidgets.QLabel(self.low_inventory)
        self.dotline_1.setGeometry(QtCore.QRect(0, 230, 741, 211))
        self.dotline_1.setStyleSheet("background: transparent;")
        self.dotline_1.setText("")
        self.dotline_1.setPixmap(QtGui.QPixmap(":/JJimages/dottedline.png"))
        self.dotline_1.setScaledContents(True)
        self.dotline_1.setObjectName("dotline_1")
        self.label_11 = QtWidgets.QLabel(self.low_inventory)
        self.label_11.setGeometry(QtCore.QRect(270, 10, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background: transparent;")
        self.label_11.setObjectName("label_11")
        self.btnViewMore_Inventory = QtWidgets.QPushButton(self.low_inventory)
        self.btnViewMore_Inventory.setGeometry(QtCore.QRect(210, 520, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(16)
        font.setUnderline(True)
        self.btnViewMore_Inventory.setFont(font)
        self.btnViewMore_Inventory.setStyleSheet("QPushButton{color: blue;\n"
"font-family: \'Poppins\', Medium;\n"
"text-decoration: underline;\n"
"border: none;\n"
"background: transparent;}\n"
"QPushButton:hover {\n"
"color:#8d2721;\n"
"}\n"
"")
        self.btnViewMore_Inventory.setObjectName("btnViewMore_Inventory")
        self.dashb_lowinstock_value = QtWidgets.QLabel(self.low_inventory)
        self.dashb_lowinstock_value.setGeometry(QtCore.QRect(580, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dashb_lowinstock_value.setFont(font)
        self.dashb_lowinstock_value.setStyleSheet("color: #d75413;\n"
"background: transparent;")
        self.dashb_lowinstock_value.setObjectName("dashb_lowinstock_value")
        self.label_12 = QtWidgets.QLabel(self.low_inventory)
        self.label_12.setGeometry(QtCore.QRect(50, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(19)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.low_inventory)
        self.label_13.setGeometry(QtCore.QRect(30, 130, 691, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #fff2bd; \n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.top1LOWEST_STOCK_PRODUCT = QtWidgets.QLabel(self.low_inventory)
        self.top1LOWEST_STOCK_PRODUCT.setGeometry(QtCore.QRect(60, 450, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top1LOWEST_STOCK_PRODUCT.setFont(font)
        self.top1LOWEST_STOCK_PRODUCT.setStyleSheet("color: #000000;\n"
"background: transparent;")
        self.top1LOWEST_STOCK_PRODUCT.setObjectName("top1LOWEST_STOCK_PRODUCT")
        self.top2LOWSTOCK_PRODUCT = QtWidgets.QLabel(self.low_inventory)
        self.top2LOWSTOCK_PRODUCT.setGeometry(QtCore.QRect(60, 380, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top2LOWSTOCK_PRODUCT.setFont(font)
        self.top2LOWSTOCK_PRODUCT.setStyleSheet("color: #000000;\n"
"background: transparent;")
        self.top2LOWSTOCK_PRODUCT.setObjectName("top2LOWSTOCK_PRODUCT")
        self.top3LOWSTOCK_PRODUCT = QtWidgets.QLabel(self.low_inventory)
        self.top3LOWSTOCK_PRODUCT.setGeometry(QtCore.QRect(60, 310, 261, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top3LOWSTOCK_PRODUCT.setFont(font)
        self.top3LOWSTOCK_PRODUCT.setStyleSheet("color: #000000;\n"
"background: transparent;")
        self.top3LOWSTOCK_PRODUCT.setObjectName("top3LOWSTOCK_PRODUCT")
        self.top4LOWSTOCK_PRODUCT = QtWidgets.QLabel(self.low_inventory)
        self.top4LOWSTOCK_PRODUCT.setGeometry(QtCore.QRect(60, 230, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top4LOWSTOCK_PRODUCT.setFont(font)
        self.top4LOWSTOCK_PRODUCT.setStyleSheet("color: #000000;\n"
"background: transparent;")
        self.top4LOWSTOCK_PRODUCT.setObjectName("top4LOWSTOCK_PRODUCT")
        self.top4LOWSTOCK_PROD_QTY = QtWidgets.QLabel(self.low_inventory)
        self.top4LOWSTOCK_PROD_QTY.setGeometry(QtCore.QRect(480, 230, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top4LOWSTOCK_PROD_QTY.setFont(font)
        self.top4LOWSTOCK_PROD_QTY.setStyleSheet("color: #b2423c;\n"
"background: transparent;")
        self.top4LOWSTOCK_PROD_QTY.setObjectName("top4LOWSTOCK_PROD_QTY")
        self.top3LOWSTOCK_PROD_QTY = QtWidgets.QLabel(self.low_inventory)
        self.top3LOWSTOCK_PROD_QTY.setGeometry(QtCore.QRect(480, 300, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top3LOWSTOCK_PROD_QTY.setFont(font)
        self.top3LOWSTOCK_PROD_QTY.setStyleSheet("color: #b2423c;\n"
"background: transparent;")
        self.top3LOWSTOCK_PROD_QTY.setObjectName("top3LOWSTOCK_PROD_QTY")
        self.top2LOWSTOCK_PROD_QTY = QtWidgets.QLabel(self.low_inventory)
        self.top2LOWSTOCK_PROD_QTY.setGeometry(QtCore.QRect(480, 370, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top2LOWSTOCK_PROD_QTY.setFont(font)
        self.top2LOWSTOCK_PROD_QTY.setStyleSheet("color: #b2423c;\n"
"background: transparent;")
        self.top2LOWSTOCK_PROD_QTY.setObjectName("top2LOWSTOCK_PROD_QTY")
        self.top1LOWEST_STOCK_PROD_QTY = QtWidgets.QLabel(self.low_inventory)
        self.top1LOWEST_STOCK_PROD_QTY.setGeometry(QtCore.QRect(480, 450, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(21)
        self.top1LOWEST_STOCK_PROD_QTY.setFont(font)
        self.top1LOWEST_STOCK_PROD_QTY.setStyleSheet("color: #b2423c;\n"
"background: transparent;")
        self.top1LOWEST_STOCK_PROD_QTY.setObjectName("top1LOWEST_STOCK_PROD_QTY")
        self.Todays_total_orders_box = QtWidgets.QFrame(self.dashboard_inview)
        self.Todays_total_orders_box.setGeometry(QtCore.QRect(580, 220, 441, 171))
        self.Todays_total_orders_box.setStyleSheet("#ordersbox\n"
"{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.Todays_total_orders_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Todays_total_orders_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Todays_total_orders_box.setObjectName("Todays_total_orders_box")
        self.ordersbox = QtWidgets.QLabel(self.Todays_total_orders_box)
        self.ordersbox.setGeometry(QtCore.QRect(10, 0, 431, 171))
        self.ordersbox.setStyleSheet("\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 15;\n"
"    padding: 10px;\n"
"\n"
"")
        self.ordersbox.setText("")
        self.ordersbox.setObjectName("ordersbox")
        self.orders_hand_icon = QtWidgets.QLabel(self.Todays_total_orders_box)
        self.orders_hand_icon.setGeometry(QtCore.QRect(20, 30, 101, 71))
        self.orders_hand_icon.setStyleSheet("background: transparent;")
        self.orders_hand_icon.setText("")
        self.orders_hand_icon.setPixmap(QtGui.QPixmap(":/JJimages/moneyhand_icon.svg"))
        self.orders_hand_icon.setScaledContents(True)
        self.orders_hand_icon.setObjectName("orders_hand_icon")
        self.up_orders = QtWidgets.QLabel(self.Todays_total_orders_box)
        self.up_orders.setGeometry(QtCore.QRect(350, 40, 71, 51))
        self.up_orders.setStyleSheet("background: transparent;")
        self.up_orders.setText("")
        self.up_orders.setPixmap(QtGui.QPixmap(":/JJimages/up.png"))
        self.up_orders.setScaledContents(True)
        self.up_orders.setObjectName("up_orders")
        self.value_Tod_orders = QtWidgets.QLabel(self.Todays_total_orders_box)
        self.value_Tod_orders.setGeometry(QtCore.QRect(100, 20, 261, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.value_Tod_orders.setFont(font)
        self.value_Tod_orders.setStyleSheet("color:#c9cc7f;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;\n"
"background: transparent;\n"
"")
        self.value_Tod_orders.setAlignment(QtCore.Qt.AlignCenter)
        self.value_Tod_orders.setObjectName("value_Tod_orders")
        self.label_8 = QtWidgets.QLabel(self.Todays_total_orders_box)
        self.label_8.setGeometry(QtCore.QRect(80, 120, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(17)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: #004aad;\n"
"font-family: \'Poppins\', Medium;\n"
"background: transparent;")
        self.label_8.setObjectName("label_8")
        self.Todays_revenue_box = QtWidgets.QFrame(self.dashboard_inview)
        self.Todays_revenue_box.setGeometry(QtCore.QRect(1060, 220, 511, 171))
        self.Todays_revenue_box.setStyleSheet("#revenue\n"
"{\n"
"border: 1px solid black;\n"
"border-radius: 10px;\n"
"}")
        self.Todays_revenue_box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Todays_revenue_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Todays_revenue_box.setObjectName("Todays_revenue_box")
        self.revenuebox = QtWidgets.QLabel(self.Todays_revenue_box)
        self.revenuebox.setGeometry(QtCore.QRect(4, 5, 501, 161))
        self.revenuebox.setStyleSheet("\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    border-radius: 15;\n"
"    padding: 10px;\n"
"\n"
"")
        self.revenuebox.setText("")
        self.revenuebox.setObjectName("revenuebox")
        self.revenue_hand_icon = QtWidgets.QLabel(self.Todays_revenue_box)
        self.revenue_hand_icon.setGeometry(QtCore.QRect(10, 40, 101, 71))
        self.revenue_hand_icon.setStyleSheet("background: transparent;")
        self.revenue_hand_icon.setText("")
        self.revenue_hand_icon.setPixmap(QtGui.QPixmap(":/JJimages/moneyhand_icon.svg"))
        self.revenue_hand_icon.setScaledContents(True)
        self.revenue_hand_icon.setObjectName("revenue_hand_icon")
        self.up_revenue = QtWidgets.QLabel(self.Todays_revenue_box)
        self.up_revenue.setGeometry(QtCore.QRect(420, 50, 71, 51))
        self.up_revenue.setStyleSheet("background: transparent;")
        self.up_revenue.setText("")
        self.up_revenue.setPixmap(QtGui.QPixmap(":/JJimages/up.png"))
        self.up_revenue.setScaledContents(True)
        self.up_revenue.setObjectName("up_revenue")
        self.value_Tod_revenue = QtWidgets.QLabel(self.Todays_revenue_box)
        self.value_Tod_revenue.setGeometry(QtCore.QRect(90, 30, 341, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.value_Tod_revenue.setFont(font)
        self.value_Tod_revenue.setStyleSheet("color:#c9cc7f;\n"
"font-family: \"MS Shell Dlg 2\", sans-serif;\n"
"background: transparent;\n"
"")
        self.value_Tod_revenue.setAlignment(QtCore.Qt.AlignCenter)
        self.value_Tod_revenue.setObjectName("value_Tod_revenue")
        self.label_9 = QtWidgets.QLabel(self.Todays_revenue_box)
        self.label_9.setGeometry(QtCore.QRect(140, 120, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(17)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #004aad;\n"
"font-family: \'Poppins\', Medium;\n"
"background: transparent;")
        self.label_9.setObjectName("label_9")
        self.dateLabel = QtWidgets.QLabel(self.dashboard_inview)
        self.dateLabel.setGeometry(QtCore.QRect(0, 10, 951, 191))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel.setFont(font)
        self.dateLabel.setStyleSheet("QLabel {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"background: transparent;\n"
"}\n"
"")
        self.dateLabel.setTextFormat(QtCore.Qt.RichText)
        self.dateLabel.setObjectName("dateLabel")
        self.timeLabel = QtWidgets.QLabel(self.dashboard_inview)
        self.timeLabel.setGeometry(QtCore.QRect(950, 10, 671, 191))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 1px solid black;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"}\n"
"")
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setObjectName("timeLabel")
        self.stackedWidget.addWidget(self.Dashboard_page)
        self.Inventory_page = QtWidgets.QWidget()
        self.Inventory_page.setObjectName("Inventory_page")
        self.inventory_inview = QtWidgets.QWidget(self.Inventory_page)
        self.inventory_inview.setGeometry(QtCore.QRect(0, 0, 1631, 1005))
        self.inventory_inview.setStyleSheet("background-color:#ffffff;\n"
"padding: 10;\n"
"")
        self.inventory_inview.setObjectName("inventory_inview")
        self.frame_3 = QtWidgets.QFrame(self.inventory_inview)
        self.frame_3.setGeometry(QtCore.QRect(40, 90, 771, 71))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_Inventory_ALL_ITEMS_table = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Inventory_ALL_ITEMS_table.setGeometry(QtCore.QRect(0, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.pushButton_Inventory_ALL_ITEMS_table.setFont(font)
        self.pushButton_Inventory_ALL_ITEMS_table.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border: 1px solid #000000; \n"
"    padding: 10px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"    /* Only top corners curved */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"    /* Keep the same corner radius for active button */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.pushButton_Inventory_ALL_ITEMS_table.setObjectName("pushButton_Inventory_ALL_ITEMS_table")
        self.pushButton_Inventory_ROOF_table = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Inventory_ROOF_table.setGeometry(QtCore.QRect(220, 10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.pushButton_Inventory_ROOF_table.setFont(font)
        self.pushButton_Inventory_ROOF_table.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border: 1px solid #000000; \n"
"    padding: 10px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"    /* Only top corners curved */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"    /* Keep the same corner radius for active button */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.pushButton_Inventory_ROOF_table.setObjectName("pushButton_Inventory_ROOF_table")
        self.pushButton_Inventory_SPANDREL_table = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Inventory_SPANDREL_table.setGeometry(QtCore.QRect(370, 10, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.pushButton_Inventory_SPANDREL_table.setFont(font)
        self.pushButton_Inventory_SPANDREL_table.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border: 1px solid #000000; \n"
"    padding: 10px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"    /* Only top corners curved */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"    /* Keep the same corner radius for active button */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.pushButton_Inventory_SPANDREL_table.setObjectName("pushButton_Inventory_SPANDREL_table")
        self.pushButton_Inventory_GUTTER_table = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Inventory_GUTTER_table.setGeometry(QtCore.QRect(580, 10, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        self.pushButton_Inventory_GUTTER_table.setFont(font)
        self.pushButton_Inventory_GUTTER_table.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border: 1px solid #000000; \n"
"    padding: 10px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"    /* Only top corners curved */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"\n"
"    /* Keep the same corner radius for active button */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"}\n"
"")
        self.pushButton_Inventory_GUTTER_table.setObjectName("pushButton_Inventory_GUTTER_table")
        self.frame_4 = QtWidgets.QFrame(self.inventory_inview)
        self.frame_4.setGeometry(QtCore.QRect(20, 30, 801, 41))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_OWNER_QuickSearch_Inventory = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_OWNER_QuickSearch_Inventory.setGeometry(QtCore.QRect(20, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        self.lineEdit_OWNER_QuickSearch_Inventory.setFont(font)
        self.lineEdit_OWNER_QuickSearch_Inventory.setStyleSheet("\n"
"    background-color: #ffffff;\n"
"border-radius: 11;\n"
"    color: black;\n"
"    border: 1px solid #000000; \n"
"    padding: 3px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"\n"
"\n"
"")
        self.lineEdit_OWNER_QuickSearch_Inventory.setClearButtonEnabled(False)
        self.lineEdit_OWNER_QuickSearch_Inventory.setObjectName("lineEdit_OWNER_QuickSearch_Inventory")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(330, 0, 51, 31))
        self.label_14.setStyleSheet("background: transparent;\n"
"padding: 5;\n"
"")
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(":/JJimages/search.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.frame_5 = QtWidgets.QFrame(self.inventory_inview)
        self.frame_5.setGeometry(QtCore.QRect(1040, 50, 551, 81))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_OWNER_Add_Inventory = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_OWNER_Add_Inventory.setGeometry(QtCore.QRect(20, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_OWNER_Add_Inventory.setFont(font)
        self.pushButton_OWNER_Add_Inventory.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ebe0cc;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 10px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#d7a613;\n"
"color:black;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #d7a613;\n"
"    color: black;\n"
"}\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/JJimages/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_OWNER_Add_Inventory.setIcon(icon6)
        self.pushButton_OWNER_Add_Inventory.setIconSize(QtCore.QSize(26, 26))
        self.pushButton_OWNER_Add_Inventory.setObjectName("pushButton_OWNER_Add_Inventory")
        self.pushButton_OWNER_Edit_Inventory = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_OWNER_Edit_Inventory.setGeometry(QtCore.QRect(190, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_OWNER_Edit_Inventory.setFont(font)
        self.pushButton_OWNER_Edit_Inventory.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ebe0cc;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 10px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#d7a613;\n"
"color:black;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #d7a613;\n"
"    color: black;\n"
"}\n"
"")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/JJimages/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_OWNER_Edit_Inventory.setIcon(icon7)
        self.pushButton_OWNER_Edit_Inventory.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_OWNER_Edit_Inventory.setObjectName("pushButton_OWNER_Edit_Inventory")
        self.pushButton_OWNER_Delete_Inventory = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_OWNER_Delete_Inventory.setGeometry(QtCore.QRect(350, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_OWNER_Delete_Inventory.setFont(font)
        self.pushButton_OWNER_Delete_Inventory.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #ebe0cc;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 10px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#d7a613;\n"
"color:black;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #d7a613;\n"
"    color: black;\n"
"}\n"
"")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/JJimages/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_OWNER_Delete_Inventory.setIcon(icon8)
        self.pushButton_OWNER_Delete_Inventory.setIconSize(QtCore.QSize(27, 27))
        self.pushButton_OWNER_Delete_Inventory.setObjectName("pushButton_OWNER_Delete_Inventory")
        self.textBrowser_inv_ROOF_lowstk_warning = QtWidgets.QTextBrowser(self.inventory_inview)
        self.textBrowser_inv_ROOF_lowstk_warning.setGeometry(QtCore.QRect(40, 870, 1521, 91))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.textBrowser_inv_ROOF_lowstk_warning.setFont(font)
        self.textBrowser_inv_ROOF_lowstk_warning.setStyleSheet("\n"
"    background-color: #ffffff;\n"
"border-radius: 11;\n"
"    color: #d75413;\n"
"    border: 1px solid #d75413; \n"
"    padding: 3px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"\n"
"\n"
"")
        self.textBrowser_inv_ROOF_lowstk_warning.setObjectName("textBrowser_inv_ROOF_lowstk_warning")
        self.INVENTORY_afterBUTTONSclick = QtWidgets.QStackedWidget(self.inventory_inview)
        self.INVENTORY_afterBUTTONSclick.setGeometry(QtCore.QRect(-10, 150, 1631, 711))
        self.INVENTORY_afterBUTTONSclick.setStyleSheet("background: transparent;")
        self.INVENTORY_afterBUTTONSclick.setObjectName("INVENTORY_afterBUTTONSclick")
        self.page_INV_ALL_ITEMS = QtWidgets.QWidget()
        self.page_INV_ALL_ITEMS.setObjectName("page_INV_ALL_ITEMS")
        self.tableWidget_ALL_ITEMS = QtWidgets.QTableWidget(self.page_INV_ALL_ITEMS)
        self.tableWidget_ALL_ITEMS.setGeometry(QtCore.QRect(40, 0, 1521, 691))
        self.tableWidget_ALL_ITEMS.setStyleSheet("padding: 1;")
        self.tableWidget_ALL_ITEMS.setObjectName("tableWidget_ALL_ITEMS")
        self.tableWidget_ALL_ITEMS.setColumnCount(6)
        self.tableWidget_ALL_ITEMS.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ALL_ITEMS.setHorizontalHeaderItem(5, item)
        self.tableWidget_ALL_ITEMS.horizontalHeader().setDefaultSectionSize(265)
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_ALL_ITEMS)
        self.page_INV_ROOF = QtWidgets.QWidget()
        self.page_INV_ROOF.setObjectName("page_INV_ROOF")
        self.tableWidget_ROOF = QtWidgets.QTableWidget(self.page_INV_ROOF)
        self.tableWidget_ROOF.setGeometry(QtCore.QRect(40, 0, 1521, 691))
        self.tableWidget_ROOF.setStyleSheet("padding: 1;")
        self.tableWidget_ROOF.setObjectName("tableWidget_ROOF")
        self.tableWidget_ROOF.setColumnCount(12)
        self.tableWidget_ROOF.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ROOF.setHorizontalHeaderItem(11, item)
        self.tableWidget_ROOF.horizontalHeader().setDefaultSectionSize(265)
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_ROOF)
        self.page_INV_SPANDREL = QtWidgets.QWidget()
        self.page_INV_SPANDREL.setObjectName("page_INV_SPANDREL")
        self.tableWidget_SPANDREL = QtWidgets.QTableWidget(self.page_INV_SPANDREL)
        self.tableWidget_SPANDREL.setGeometry(QtCore.QRect(40, 0, 1521, 691))
        self.tableWidget_SPANDREL.setStyleSheet("padding: 1;")
        self.tableWidget_SPANDREL.setObjectName("tableWidget_SPANDREL")
        self.tableWidget_SPANDREL.setColumnCount(12)
        self.tableWidget_SPANDREL.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SPANDREL.setHorizontalHeaderItem(11, item)
        self.tableWidget_SPANDREL.horizontalHeader().setDefaultSectionSize(265)
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_SPANDREL)
        self.page_INV_GUTTER = QtWidgets.QWidget()
        self.page_INV_GUTTER.setObjectName("page_INV_GUTTER")
        self.tableWidget_GUTTER = QtWidgets.QTableWidget(self.page_INV_GUTTER)
        self.tableWidget_GUTTER.setGeometry(QtCore.QRect(40, 0, 1521, 691))
        self.tableWidget_GUTTER.setStyleSheet("padding: 1;")
        self.tableWidget_GUTTER.setObjectName("tableWidget_GUTTER")
        self.tableWidget_GUTTER.setColumnCount(12)
        self.tableWidget_GUTTER.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_GUTTER.setHorizontalHeaderItem(11, item)
        self.tableWidget_GUTTER.horizontalHeader().setDefaultSectionSize(265)
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_GUTTER)
        self.page_INV_ADD_STOCK = QtWidgets.QWidget()
        self.page_INV_ADD_STOCK.setObjectName("page_INV_ADD_STOCK")
        self.frame_6 = QtWidgets.QFrame(self.page_INV_ADD_STOCK)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 1621, 691))
        self.frame_6.setStyleSheet("background: #ebe0cc;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_15 = QtWidgets.QLabel(self.frame_6)
        self.label_15.setGeometry(QtCore.QRect(80, 30, 1451, 631))
        self.label_15.setStyleSheet("    background-color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; ")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.addStocklabel = QtWidgets.QLabel(self.frame_6)
        self.addStocklabel.setGeometry(QtCore.QRect(120, 30, 1371, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.addStocklabel.setFont(font)
        self.addStocklabel.setStyleSheet("    background-color: transparent;\n"
"")
        self.addStocklabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addStocklabel.setObjectName("addStocklabel")
        self.Add_Select_Prod_Type = QtWidgets.QStackedWidget(self.frame_6)
        self.Add_Select_Prod_Type.setGeometry(QtCore.QRect(100, 120, 1411, 521))
        self.Add_Select_Prod_Type.setStyleSheet("background: #f6f3ee;")
        self.Add_Select_Prod_Type.setObjectName("Add_Select_Prod_Type")
        self.ADD_blank = QtWidgets.QWidget()
        self.ADD_blank.setObjectName("ADD_blank")
        self.label_22 = QtWidgets.QLabel(self.ADD_blank)
        self.label_22.setGeometry(QtCore.QRect(0, -10, 1321, 361))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background: transparent;\n"
"color: #a6a6a6;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.Add_Select_Prod_Type.addWidget(self.ADD_blank)
        self.ADD_ROOF = QtWidgets.QWidget()
        self.ADD_ROOF.setObjectName("ADD_ROOF")
        self.frame_9 = QtWidgets.QFrame(self.ADD_ROOF)
        self.frame_9.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_9.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.pushButton_Confirm_ROOFadd = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_Confirm_ROOFadd.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_ROOFadd.setFont(font)
        self.pushButton_Confirm_ROOFadd.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_ROOFadd.setObjectName("pushButton_Confirm_ROOFadd")
        self.pushButton_Close_ROOFadd = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_Close_ROOFadd.setGeometry(QtCore.QRect(740, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_ROOFadd.setFont(font)
        self.pushButton_Close_ROOFadd.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_ROOFadd.setObjectName("pushButton_Close_ROOFadd")
        self.frame_addroof = QtWidgets.QFrame(self.ADD_ROOF)
        self.frame_addroof.setGeometry(QtCore.QRect(-11, -1, 1411, 421))
        self.frame_addroof.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_addroof.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addroof.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addroof.setObjectName("frame_addroof")
        self.label_23 = QtWidgets.QLabel(self.frame_addroof)
        self.label_23.setGeometry(QtCore.QRect(30, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_addroof)
        self.label_24.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_addroof)
        self.label_25.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_25.setObjectName("label_25")
        self.label_32 = QtWidgets.QLabel(self.frame_addroof)
        self.label_32.setGeometry(QtCore.QRect(30, 60, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_32.setObjectName("label_32")
        self.lineEdit_AddROOF_prodCode = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_prodCode.setFont(font)
        self.lineEdit_AddROOF_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_prodCode.setObjectName("lineEdit_AddROOF_prodCode")
        self.lineEdit_AddROOF_Name = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Name.setFont(font)
        self.lineEdit_AddROOF_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Name.setObjectName("lineEdit_AddROOF_Name")
        self.lineEdit_AddROOF_Weight = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Weight.setFont(font)
        self.lineEdit_AddROOF_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Weight.setObjectName("lineEdit_AddROOF_Weight")
        self.comboBox_AddROOF_Type = QtWidgets.QComboBox(self.frame_addroof)
        self.comboBox_AddROOF_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_AddROOF_Type.setFont(font)
        self.comboBox_AddROOF_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_AddROOF_Type.setObjectName("comboBox_AddROOF_Type")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.comboBox_AddROOF_Type.addItem("")
        self.label_105 = QtWidgets.QLabel(self.frame_addroof)
        self.label_105.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_105.setObjectName("label_105")
        self.lineEdit_AddROOF_Qty = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Qty.setFont(font)
        self.lineEdit_AddROOF_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Qty.setObjectName("lineEdit_AddROOF_Qty")
        self.label_107 = QtWidgets.QLabel(self.frame_addroof)
        self.label_107.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_107.setFont(font)
        self.label_107.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_107.setObjectName("label_107")
        self.label_31 = QtWidgets.QLabel(self.frame_addroof)
        self.label_31.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_31.setObjectName("label_31")
        self.lineEdit_AddROOF_Color = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Color.setFont(font)
        self.lineEdit_AddROOF_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Color.setObjectName("lineEdit_AddROOF_Color")
        self.label_30 = QtWidgets.QLabel(self.frame_addroof)
        self.label_30.setGeometry(QtCore.QRect(820, 340, 291, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_30.setObjectName("label_30")
        self.lineEdit_AddROOF_Width = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Width.setFont(font)
        self.lineEdit_AddROOF_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Width.setObjectName("lineEdit_AddROOF_Width")
        self.label_29 = QtWidgets.QLabel(self.frame_addroof)
        self.label_29.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_29.setObjectName("label_29")
        self.lineEdit_AddROOF_Length = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Length.setFont(font)
        self.lineEdit_AddROOF_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Length.setObjectName("lineEdit_AddROOF_Length")
        self.label_27 = QtWidgets.QLabel(self.frame_addroof)
        self.label_27.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_27.setObjectName("label_27")
        self.lineEdit_AddROOF_Price = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Price.setFont(font)
        self.lineEdit_AddROOF_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Price.setObjectName("lineEdit_AddROOF_Price")
        self.lineEdit_AddROOF_Desc = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Desc.setFont(font)
        self.lineEdit_AddROOF_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Desc.setObjectName("lineEdit_AddROOF_Desc")
        self.label_117 = QtWidgets.QLabel(self.frame_addroof)
        self.label_117.setGeometry(QtCore.QRect(820, 130, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_117.setFont(font)
        self.label_117.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_117.setObjectName("label_117")
        self.lineEdit_AddROOF_Thickness = QtWidgets.QLineEdit(self.frame_addroof)
        self.lineEdit_AddROOF_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddROOF_Thickness.setFont(font)
        self.lineEdit_AddROOF_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddROOF_Thickness.setObjectName("lineEdit_AddROOF_Thickness")
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_32.raise_()
        self.lineEdit_AddROOF_prodCode.raise_()
        self.lineEdit_AddROOF_Name.raise_()
        self.lineEdit_AddROOF_Weight.raise_()
        self.comboBox_AddROOF_Type.raise_()
        self.lineEdit_AddROOF_Qty.raise_()
        self.label_107.raise_()
        self.label_31.raise_()
        self.lineEdit_AddROOF_Color.raise_()
        self.label_30.raise_()
        self.lineEdit_AddROOF_Width.raise_()
        self.label_29.raise_()
        self.lineEdit_AddROOF_Length.raise_()
        self.label_105.raise_()
        self.label_27.raise_()
        self.lineEdit_AddROOF_Price.raise_()
        self.lineEdit_AddROOF_Desc.raise_()
        self.label_117.raise_()
        self.lineEdit_AddROOF_Thickness.raise_()
        self.Add_Select_Prod_Type.addWidget(self.ADD_ROOF)
        self.ADD_SPANDREL = QtWidgets.QWidget()
        self.ADD_SPANDREL.setObjectName("ADD_SPANDREL")
        self.frame_10 = QtWidgets.QFrame(self.ADD_SPANDREL)
        self.frame_10.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_10.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.pushButton_Confirm_SPANDRELadd = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_Confirm_SPANDRELadd.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_SPANDRELadd.setFont(font)
        self.pushButton_Confirm_SPANDRELadd.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_SPANDRELadd.setObjectName("pushButton_Confirm_SPANDRELadd")
        self.pushButton_Close_SPANDRELadd = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_Close_SPANDRELadd.setGeometry(QtCore.QRect(740, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_SPANDRELadd.setFont(font)
        self.pushButton_Close_SPANDRELadd.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_SPANDRELadd.setObjectName("pushButton_Close_SPANDRELadd")
        self.frame_addspandrel = QtWidgets.QFrame(self.ADD_SPANDREL)
        self.frame_addspandrel.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_addspandrel.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_addspandrel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addspandrel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addspandrel.setObjectName("frame_addspandrel")
        self.label_26 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_26.setGeometry(QtCore.QRect(30, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_28.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_28.setObjectName("label_28")
        self.label_108 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_108.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_108.setFont(font)
        self.label_108.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_108.setObjectName("label_108")
        self.label_109 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_109.setGeometry(QtCore.QRect(30, 60, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_109.setFont(font)
        self.label_109.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_109.setObjectName("label_109")
        self.lineEdit_AddSPANDREL_prodCode = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_prodCode.setFont(font)
        self.lineEdit_AddSPANDREL_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_prodCode.setObjectName("lineEdit_AddSPANDREL_prodCode")
        self.lineEdit_AddSPANDREL_Name = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Name.setFont(font)
        self.lineEdit_AddSPANDREL_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Name.setObjectName("lineEdit_AddSPANDREL_Name")
        self.lineEdit_AddSPANDREL_Weight = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Weight.setFont(font)
        self.lineEdit_AddSPANDREL_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Weight.setObjectName("lineEdit_AddSPANDREL_Weight")
        self.label_110 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_110.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_110.setFont(font)
        self.label_110.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_110.setObjectName("label_110")
        self.lineEdit_AddSPANDREL_Qty = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Qty.setFont(font)
        self.lineEdit_AddSPANDREL_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Qty.setObjectName("lineEdit_AddSPANDREL_Qty")
        self.label_112 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_112.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_112.setFont(font)
        self.label_112.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_112.setObjectName("label_112")
        self.lineEdit_AddSPANDREL_Thickness = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Thickness.setFont(font)
        self.lineEdit_AddSPANDREL_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Thickness.setObjectName("lineEdit_AddSPANDREL_Thickness")
        self.label_113 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_113.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_113.setFont(font)
        self.label_113.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_113.setObjectName("label_113")
        self.lineEdit_AddSPANDREL_Color = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Color.setFont(font)
        self.lineEdit_AddSPANDREL_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Color.setObjectName("lineEdit_AddSPANDREL_Color")
        self.label_115 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_115.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_115.setFont(font)
        self.label_115.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_115.setObjectName("label_115")
        self.lineEdit_AddSPANDREL_Length = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Length.setFont(font)
        self.lineEdit_AddSPANDREL_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Length.setObjectName("lineEdit_AddSPANDREL_Length")
        self.label_116 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_116.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_116.setFont(font)
        self.label_116.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_116.setObjectName("label_116")
        self.lineEdit_AddSPANDREL_Price = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Price.setFont(font)
        self.lineEdit_AddSPANDREL_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Price.setObjectName("lineEdit_AddSPANDREL_Price")
        self.lineEdit_AddSPANDREL_Desc = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Desc.setFont(font)
        self.lineEdit_AddSPANDREL_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Desc.setObjectName("lineEdit_AddSPANDREL_Desc")
        self.comboBox_AddSPANDREL_Type = QtWidgets.QComboBox(self.frame_addspandrel)
        self.comboBox_AddSPANDREL_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_AddSPANDREL_Type.setFont(font)
        self.comboBox_AddSPANDREL_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_AddSPANDREL_Type.setObjectName("comboBox_AddSPANDREL_Type")
        self.comboBox_AddSPANDREL_Type.addItem("")
        self.comboBox_AddSPANDREL_Type.addItem("")
        self.comboBox_AddSPANDREL_Type.addItem("")
        self.label_118 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_118.setGeometry(QtCore.QRect(820, 130, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_118.setFont(font)
        self.label_118.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_118.setObjectName("label_118")
        self.lineEdit_AddSPANDREL_Width = QtWidgets.QLineEdit(self.frame_addspandrel)
        self.lineEdit_AddSPANDREL_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddSPANDREL_Width.setFont(font)
        self.lineEdit_AddSPANDREL_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddSPANDREL_Width.setObjectName("lineEdit_AddSPANDREL_Width")
        self.label_119 = QtWidgets.QLabel(self.frame_addspandrel)
        self.label_119.setGeometry(QtCore.QRect(820, 340, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_119.setFont(font)
        self.label_119.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_119.setObjectName("label_119")
        self.Add_Select_Prod_Type.addWidget(self.ADD_SPANDREL)
        self.ADD_GUTTER = QtWidgets.QWidget()
        self.ADD_GUTTER.setObjectName("ADD_GUTTER")
        self.frame_11 = QtWidgets.QFrame(self.ADD_GUTTER)
        self.frame_11.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_11.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.pushButton_Confirm_GUTTERadd = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_Confirm_GUTTERadd.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_GUTTERadd.setFont(font)
        self.pushButton_Confirm_GUTTERadd.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_GUTTERadd.setObjectName("pushButton_Confirm_GUTTERadd")
        self.pushButton_Close_GUTTERadd = QtWidgets.QPushButton(self.frame_11)
        self.pushButton_Close_GUTTERadd.setGeometry(QtCore.QRect(740, 20, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_GUTTERadd.setFont(font)
        self.pushButton_Close_GUTTERadd.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_GUTTERadd.setObjectName("pushButton_Close_GUTTERadd")
        self.frame_addgutter = QtWidgets.QFrame(self.ADD_GUTTER)
        self.frame_addgutter.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_addgutter.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_addgutter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addgutter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addgutter.setObjectName("frame_addgutter")
        self.label_33 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_33.setGeometry(QtCore.QRect(30, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_34.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_34.setObjectName("label_34")
        self.label_129 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_129.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_129.setFont(font)
        self.label_129.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_129.setObjectName("label_129")
        self.lineEdit_AddGUTTER_prodCode = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_prodCode.setFont(font)
        self.lineEdit_AddGUTTER_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_prodCode.setObjectName("lineEdit_AddGUTTER_prodCode")
        self.lineEdit_AddGUTTER_Name = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Name.setFont(font)
        self.lineEdit_AddGUTTER_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Name.setObjectName("lineEdit_AddGUTTER_Name")
        self.lineEdit_AddGUTTER_Weight = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Weight.setFont(font)
        self.lineEdit_AddGUTTER_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Weight.setObjectName("lineEdit_AddGUTTER_Weight")
        self.label_131 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_131.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_131.setFont(font)
        self.label_131.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_131.setObjectName("label_131")
        self.lineEdit_AddGUTTER_Qty = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Qty.setFont(font)
        self.lineEdit_AddGUTTER_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Qty.setObjectName("lineEdit_AddGUTTER_Qty")
        self.label_133 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_133.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_133.setFont(font)
        self.label_133.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_133.setObjectName("label_133")
        self.lineEdit_AddGUTTER_Thickness = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Thickness.setFont(font)
        self.lineEdit_AddGUTTER_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Thickness.setObjectName("lineEdit_AddGUTTER_Thickness")
        self.label_134 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_134.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_134.setFont(font)
        self.label_134.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_134.setObjectName("label_134")
        self.lineEdit_AddGUTTER_Color = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Color.setFont(font)
        self.lineEdit_AddGUTTER_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Color.setObjectName("lineEdit_AddGUTTER_Color")
        self.label_136 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_136.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_136.setFont(font)
        self.label_136.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_136.setObjectName("label_136")
        self.lineEdit_AddGUTTER_Length = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Length.setFont(font)
        self.lineEdit_AddGUTTER_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Length.setObjectName("lineEdit_AddGUTTER_Length")
        self.label_137 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_137.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_137.setFont(font)
        self.label_137.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_137.setObjectName("label_137")
        self.lineEdit_AddGUTTER_Price = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Price.setFont(font)
        self.lineEdit_AddGUTTER_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Price.setObjectName("lineEdit_AddGUTTER_Price")
        self.lineEdit_AddGUTTER_Desc = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Desc.setFont(font)
        self.lineEdit_AddGUTTER_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Desc.setObjectName("lineEdit_AddGUTTER_Desc")
        self.comboBox_AddGUTTER_Type = QtWidgets.QComboBox(self.frame_addgutter)
        self.comboBox_AddGUTTER_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_AddGUTTER_Type.setFont(font)
        self.comboBox_AddGUTTER_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_AddGUTTER_Type.setObjectName("comboBox_AddGUTTER_Type")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.comboBox_AddGUTTER_Type.addItem("")
        self.label_159 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_159.setGeometry(QtCore.QRect(820, 140, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_159.setFont(font)
        self.label_159.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_159.setObjectName("label_159")
        self.label_160 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_160.setGeometry(QtCore.QRect(820, 340, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_160.setFont(font)
        self.label_160.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_160.setObjectName("label_160")
        self.lineEdit_AddGUTTER_Width = QtWidgets.QLineEdit(self.frame_addgutter)
        self.lineEdit_AddGUTTER_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_AddGUTTER_Width.setFont(font)
        self.lineEdit_AddGUTTER_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_AddGUTTER_Width.setObjectName("lineEdit_AddGUTTER_Width")
        self.label_132 = QtWidgets.QLabel(self.frame_addgutter)
        self.label_132.setGeometry(QtCore.QRect(30, 50, 191, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_132.setFont(font)
        self.label_132.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_132.setObjectName("label_132")
        self.Add_Select_Prod_Type.addWidget(self.ADD_GUTTER)
        self.comboBox_Select_Prod_Type_toAdd = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_Select_Prod_Type_toAdd.setGeometry(QtCore.QRect(1220, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_Select_Prod_Type_toAdd.setFont(font)
        self.comboBox_Select_Prod_Type_toAdd.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_Select_Prod_Type_toAdd.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_Select_Prod_Type_toAdd.setObjectName("comboBox_Select_Prod_Type_toAdd")
        self.comboBox_Select_Prod_Type_toAdd.addItem("")
        self.comboBox_Select_Prod_Type_toAdd.addItem("")
        self.comboBox_Select_Prod_Type_toAdd.addItem("")
        self.comboBox_Select_Prod_Type_toAdd.addItem("")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(360, 80, 881, 81))
        self.label_16.setStyleSheet("background: transparent;")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/JJimages/straightline.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_15.raise_()
        self.Add_Select_Prod_Type.raise_()
        self.addStocklabel.raise_()
        self.comboBox_Select_Prod_Type_toAdd.raise_()
        self.label_16.raise_()
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_ADD_STOCK)
        self.page_INV_EDIT_STOCK = QtWidgets.QWidget()
        self.page_INV_EDIT_STOCK.setObjectName("page_INV_EDIT_STOCK")
        self.frame_7 = QtWidgets.QFrame(self.page_INV_EDIT_STOCK)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 1621, 691))
        self.frame_7.setStyleSheet("background: #ebe0cc;")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_21 = QtWidgets.QLabel(self.frame_7)
        self.label_21.setGeometry(QtCore.QRect(80, 30, 1451, 631))
        self.label_21.setStyleSheet("    background-color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; ")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.editStocklabel = QtWidgets.QLabel(self.frame_7)
        self.editStocklabel.setGeometry(QtCore.QRect(120, 30, 1371, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.editStocklabel.setFont(font)
        self.editStocklabel.setStyleSheet("    background-color: transparent;\n"
"")
        self.editStocklabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editStocklabel.setObjectName("editStocklabel")
        self.Edit_Select_Prod_Type = QtWidgets.QStackedWidget(self.frame_7)
        self.Edit_Select_Prod_Type.setGeometry(QtCore.QRect(100, 120, 1411, 521))
        self.Edit_Select_Prod_Type.setStyleSheet("background: #f6f3ee;")
        self.Edit_Select_Prod_Type.setObjectName("Edit_Select_Prod_Type")
        self.EDIT_blank = QtWidgets.QWidget()
        self.EDIT_blank.setObjectName("EDIT_blank")
        self.label_54 = QtWidgets.QLabel(self.EDIT_blank)
        self.label_54.setGeometry(QtCore.QRect(0, -10, 1321, 361))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("background: transparent;\n"
"color: #a6a6a6;")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.Edit_Select_Prod_Type.addWidget(self.EDIT_blank)
        self.EDIT_ROOF = QtWidgets.QWidget()
        self.EDIT_ROOF.setObjectName("EDIT_ROOF")
        self.frame_15 = QtWidgets.QFrame(self.EDIT_ROOF)
        self.frame_15.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_15.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.pushButton_Save_ROOFedit = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_Save_ROOFedit.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Save_ROOFedit.setFont(font)
        self.pushButton_Save_ROOFedit.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Save_ROOFedit.setObjectName("pushButton_Save_ROOFedit")
        self.pushButton_Discard_ROOFedit = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_Discard_ROOFedit.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Discard_ROOFedit.setFont(font)
        self.pushButton_Discard_ROOFedit.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Discard_ROOFedit.setObjectName("pushButton_Discard_ROOFedit")
        self.frame_editroof = QtWidgets.QFrame(self.EDIT_ROOF)
        self.frame_editroof.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_editroof.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_editroof.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_editroof.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_editroof.setObjectName("frame_editroof")
        self.label_35 = QtWidgets.QLabel(self.frame_editroof)
        self.label_35.setGeometry(QtCore.QRect(30, -10, 211, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame_editroof)
        self.label_36.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame_editroof)
        self.label_37.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame_editroof)
        self.label_38.setGeometry(QtCore.QRect(30, 80, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_38.setObjectName("label_38")
        self.lineEdit_EditROOF_prodCode = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_prodCode.setFont(font)
        self.lineEdit_EditROOF_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_prodCode.setObjectName("lineEdit_EditROOF_prodCode")
        self.lineEdit_EditROOF_Name = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Name.setFont(font)
        self.lineEdit_EditROOF_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Name.setObjectName("lineEdit_EditROOF_Name")
        self.lineEdit_EditROOF_Weight = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Weight.setFont(font)
        self.lineEdit_EditROOF_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Weight.setObjectName("lineEdit_EditROOF_Weight")
        self.comboBox_EditROOF_Type = QtWidgets.QComboBox(self.frame_editroof)
        self.comboBox_EditROOF_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_EditROOF_Type.setFont(font)
        self.comboBox_EditROOF_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_EditROOF_Type.setObjectName("comboBox_EditROOF_Type")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.comboBox_EditROOF_Type.addItem("")
        self.label_138 = QtWidgets.QLabel(self.frame_editroof)
        self.label_138.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_138.setFont(font)
        self.label_138.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_138.setObjectName("label_138")
        self.lineEdit_EditROOF_Qty = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Qty.setFont(font)
        self.lineEdit_EditROOF_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Qty.setObjectName("lineEdit_EditROOF_Qty")
        self.label_140 = QtWidgets.QLabel(self.frame_editroof)
        self.label_140.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_140.setFont(font)
        self.label_140.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_140.setObjectName("label_140")
        self.lineEdit_EditROOF_Thickness = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Thickness.setFont(font)
        self.lineEdit_EditROOF_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Thickness.setObjectName("lineEdit_EditROOF_Thickness")
        self.label_39 = QtWidgets.QLabel(self.frame_editroof)
        self.label_39.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_39.setObjectName("label_39")
        self.lineEdit_EditROOF_Color = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Color.setFont(font)
        self.lineEdit_EditROOF_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Color.setObjectName("lineEdit_EditROOF_Color")
        self.label_40 = QtWidgets.QLabel(self.frame_editroof)
        self.label_40.setGeometry(QtCore.QRect(820, 340, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.frame_editroof)
        self.label_41.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_41.setObjectName("label_41")
        self.lineEdit_EditROOF_Length = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Length.setFont(font)
        self.lineEdit_EditROOF_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Length.setObjectName("lineEdit_EditROOF_Length")
        self.label_42 = QtWidgets.QLabel(self.frame_editroof)
        self.label_42.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_42.setObjectName("label_42")
        self.lineEdit_EditROOF_Price = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Price.setFont(font)
        self.lineEdit_EditROOF_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Price.setObjectName("lineEdit_EditROOF_Price")
        self.lineEdit_EditROOF_Desc = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Desc.setFont(font)
        self.lineEdit_EditROOF_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Desc.setObjectName("lineEdit_EditROOF_Desc")
        self.label_156 = QtWidgets.QLabel(self.frame_editroof)
        self.label_156.setGeometry(QtCore.QRect(820, 120, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_156.setFont(font)
        self.label_156.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_156.setObjectName("label_156")
        self.lineEdit_EditROOF_Width = QtWidgets.QLineEdit(self.frame_editroof)
        self.lineEdit_EditROOF_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditROOF_Width.setFont(font)
        self.lineEdit_EditROOF_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditROOF_Width.setObjectName("lineEdit_EditROOF_Width")
        self.Edit_Select_Prod_Type.addWidget(self.EDIT_ROOF)
        self.EDIT_SPANDREL = QtWidgets.QWidget()
        self.EDIT_SPANDREL.setObjectName("EDIT_SPANDREL")
        self.frame_17 = QtWidgets.QFrame(self.EDIT_SPANDREL)
        self.frame_17.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_17.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.pushButton_Save_SPANDRELedit = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_Save_SPANDRELedit.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Save_SPANDRELedit.setFont(font)
        self.pushButton_Save_SPANDRELedit.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Save_SPANDRELedit.setObjectName("pushButton_Save_SPANDRELedit")
        self.pushButton_Discard_SPANDRELedit = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_Discard_SPANDRELedit.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Discard_SPANDRELedit.setFont(font)
        self.pushButton_Discard_SPANDRELedit.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Discard_SPANDRELedit.setObjectName("pushButton_Discard_SPANDRELedit")
        self.frame_editspandrel = QtWidgets.QFrame(self.EDIT_SPANDREL)
        self.frame_editspandrel.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_editspandrel.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_editspandrel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_editspandrel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_editspandrel.setObjectName("frame_editspandrel")
        self.label_43 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_43.setGeometry(QtCore.QRect(30, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_44.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_44.setObjectName("label_44")
        self.label_141 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_141.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_141.setFont(font)
        self.label_141.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_141.setObjectName("label_141")
        self.label_142 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_142.setGeometry(QtCore.QRect(30, 50, 171, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_142.setFont(font)
        self.label_142.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_142.setObjectName("label_142")
        self.lineEdit_EditSPANDREL_prodCode = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_prodCode.setFont(font)
        self.lineEdit_EditSPANDREL_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_prodCode.setObjectName("lineEdit_EditSPANDREL_prodCode")
        self.lineEdit_EditSPANDREL_Name = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Name.setFont(font)
        self.lineEdit_EditSPANDREL_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Name.setObjectName("lineEdit_EditSPANDREL_Name")
        self.lineEdit_EditSPANDREL_Weight = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Weight.setFont(font)
        self.lineEdit_EditSPANDREL_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Weight.setObjectName("lineEdit_EditSPANDREL_Weight")
        self.label_143 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_143.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_143.setFont(font)
        self.label_143.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_143.setObjectName("label_143")
        self.lineEdit_EditSPANDREL_Qty = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Qty.setFont(font)
        self.lineEdit_EditSPANDREL_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Qty.setObjectName("lineEdit_EditSPANDREL_Qty")
        self.label_144 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_144.setGeometry(QtCore.QRect(820, 130, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_144.setFont(font)
        self.label_144.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_144.setObjectName("label_144")
        self.label_145 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_145.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_145.setFont(font)
        self.label_145.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_145.setObjectName("label_145")
        self.lineEdit_EditSPANDREL_Thickness = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Thickness.setFont(font)
        self.lineEdit_EditSPANDREL_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Thickness.setObjectName("lineEdit_EditSPANDREL_Thickness")
        self.label_146 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_146.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_146.setFont(font)
        self.label_146.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_146.setObjectName("label_146")
        self.lineEdit_EditSPANDREL_Color = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Color.setFont(font)
        self.lineEdit_EditSPANDREL_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Color.setObjectName("lineEdit_EditSPANDREL_Color")
        self.label_148 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_148.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_148.setFont(font)
        self.label_148.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_148.setObjectName("label_148")
        self.lineEdit_EditSPANDREL_Length = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Length.setFont(font)
        self.lineEdit_EditSPANDREL_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Length.setObjectName("lineEdit_EditSPANDREL_Length")
        self.label_149 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_149.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_149.setFont(font)
        self.label_149.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_149.setObjectName("label_149")
        self.lineEdit_EditSPANDREL_Price = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Price.setFont(font)
        self.lineEdit_EditSPANDREL_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Price.setObjectName("lineEdit_EditSPANDREL_Price")
        self.lineEdit_EditSPANDREL_Desc = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Desc.setFont(font)
        self.lineEdit_EditSPANDREL_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Desc.setObjectName("lineEdit_EditSPANDREL_Desc")
        self.comboBox_EditSPANDREL_Type = QtWidgets.QComboBox(self.frame_editspandrel)
        self.comboBox_EditSPANDREL_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_EditSPANDREL_Type.setFont(font)
        self.comboBox_EditSPANDREL_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_EditSPANDREL_Type.setObjectName("comboBox_EditSPANDREL_Type")
        self.comboBox_EditSPANDREL_Type.addItem("")
        self.comboBox_EditSPANDREL_Type.addItem("")
        self.comboBox_EditSPANDREL_Type.addItem("")
        self.label_162 = QtWidgets.QLabel(self.frame_editspandrel)
        self.label_162.setGeometry(QtCore.QRect(820, 340, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_162.setFont(font)
        self.label_162.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_162.setObjectName("label_162")
        self.lineEdit_EditSPANDREL_Width = QtWidgets.QLineEdit(self.frame_editspandrel)
        self.lineEdit_EditSPANDREL_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditSPANDREL_Width.setFont(font)
        self.lineEdit_EditSPANDREL_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditSPANDREL_Width.setObjectName("lineEdit_EditSPANDREL_Width")
        self.Edit_Select_Prod_Type.addWidget(self.EDIT_SPANDREL)
        self.EDIT_GUTTER = QtWidgets.QWidget()
        self.EDIT_GUTTER.setObjectName("EDIT_GUTTER")
        self.frame_19 = QtWidgets.QFrame(self.EDIT_GUTTER)
        self.frame_19.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_19.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.pushButton_Save_GUTTERedit = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_Save_GUTTERedit.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Save_GUTTERedit.setFont(font)
        self.pushButton_Save_GUTTERedit.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Save_GUTTERedit.setObjectName("pushButton_Save_GUTTERedit")
        self.pushButton_Discard_GUTTERedit = QtWidgets.QPushButton(self.frame_19)
        self.pushButton_Discard_GUTTERedit.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Discard_GUTTERedit.setFont(font)
        self.pushButton_Discard_GUTTERedit.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Discard_GUTTERedit.setObjectName("pushButton_Discard_GUTTERedit")
        self.frame_editgutter = QtWidgets.QFrame(self.EDIT_GUTTER)
        self.frame_editgutter.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_editgutter.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_editgutter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_editgutter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_editgutter.setObjectName("frame_editgutter")
        self.label_45 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_45.setGeometry(QtCore.QRect(30, 0, 211, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_46.setGeometry(QtCore.QRect(30, 140, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_46.setObjectName("label_46")
        self.label_150 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_150.setGeometry(QtCore.QRect(30, 260, 161, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_150.setFont(font)
        self.label_150.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_150.setObjectName("label_150")
        self.label_151 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_151.setGeometry(QtCore.QRect(30, 60, 171, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_151.setFont(font)
        self.label_151.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_151.setObjectName("label_151")
        self.lineEdit_EditGUTTER_prodCode = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_prodCode.setGeometry(QtCore.QRect(240, 10, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_prodCode.setFont(font)
        self.lineEdit_EditGUTTER_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_prodCode.setObjectName("lineEdit_EditGUTTER_prodCode")
        self.lineEdit_EditGUTTER_Name = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Name.setGeometry(QtCore.QRect(240, 150, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Name.setFont(font)
        self.lineEdit_EditGUTTER_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Name.setObjectName("lineEdit_EditGUTTER_Name")
        self.lineEdit_EditGUTTER_Weight = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Weight.setGeometry(QtCore.QRect(1100, 290, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Weight.setFont(font)
        self.lineEdit_EditGUTTER_Weight.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Weight.setObjectName("lineEdit_EditGUTTER_Weight")
        self.label_152 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_152.setGeometry(QtCore.QRect(820, -50, 271, 171))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_152.setFont(font)
        self.label_152.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_152.setObjectName("label_152")
        self.lineEdit_EditGUTTER_Qty = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Qty.setGeometry(QtCore.QRect(1100, 10, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Qty.setFont(font)
        self.lineEdit_EditGUTTER_Qty.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Qty.setObjectName("lineEdit_EditGUTTER_Qty")
        self.label_153 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_153.setGeometry(QtCore.QRect(820, 130, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_153.setFont(font)
        self.label_153.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_153.setObjectName("label_153")
        self.label_154 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_154.setGeometry(QtCore.QRect(820, 270, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_154.setFont(font)
        self.label_154.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_154.setObjectName("label_154")
        self.lineEdit_EditGUTTER_Thickness = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Thickness.setGeometry(QtCore.QRect(1100, 150, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Thickness.setFont(font)
        self.lineEdit_EditGUTTER_Thickness.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Thickness.setObjectName("lineEdit_EditGUTTER_Thickness")
        self.label_155 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_155.setGeometry(QtCore.QRect(820, 200, 271, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_155.setFont(font)
        self.label_155.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_155.setObjectName("label_155")
        self.lineEdit_EditGUTTER_Color = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Color.setGeometry(QtCore.QRect(1100, 220, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Color.setFont(font)
        self.lineEdit_EditGUTTER_Color.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Color.setObjectName("lineEdit_EditGUTTER_Color")
        self.label_157 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_157.setGeometry(QtCore.QRect(820, 50, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_157.setFont(font)
        self.label_157.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_157.setObjectName("label_157")
        self.lineEdit_EditGUTTER_Length = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Length.setGeometry(QtCore.QRect(1100, 80, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Length.setFont(font)
        self.lineEdit_EditGUTTER_Length.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Length.setObjectName("lineEdit_EditGUTTER_Length")
        self.label_158 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_158.setGeometry(QtCore.QRect(30, 170, 181, 151))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_158.setFont(font)
        self.label_158.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_158.setObjectName("label_158")
        self.lineEdit_EditGUTTER_Price = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Price.setGeometry(QtCore.QRect(240, 220, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Price.setFont(font)
        self.lineEdit_EditGUTTER_Price.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Price.setObjectName("lineEdit_EditGUTTER_Price")
        self.lineEdit_EditGUTTER_Desc = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Desc.setGeometry(QtCore.QRect(240, 290, 561, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Desc.setFont(font)
        self.lineEdit_EditGUTTER_Desc.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Desc.setObjectName("lineEdit_EditGUTTER_Desc")
        self.comboBox_EditGUTTER_Type = QtWidgets.QComboBox(self.frame_editgutter)
        self.comboBox_EditGUTTER_Type.setGeometry(QtCore.QRect(240, 80, 561, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_EditGUTTER_Type.setFont(font)
        self.comboBox_EditGUTTER_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_EditGUTTER_Type.setObjectName("comboBox_EditGUTTER_Type")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.comboBox_EditGUTTER_Type.addItem("")
        self.label_161 = QtWidgets.QLabel(self.frame_editgutter)
        self.label_161.setGeometry(QtCore.QRect(820, 340, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_161.setFont(font)
        self.label_161.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_161.setObjectName("label_161")
        self.lineEdit_EditGUTTER_Width = QtWidgets.QLineEdit(self.frame_editgutter)
        self.lineEdit_EditGUTTER_Width.setGeometry(QtCore.QRect(1100, 360, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_EditGUTTER_Width.setFont(font)
        self.lineEdit_EditGUTTER_Width.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_EditGUTTER_Width.setObjectName("lineEdit_EditGUTTER_Width")
        self.Edit_Select_Prod_Type.addWidget(self.EDIT_GUTTER)
        self.comboBox_Select_Prod_Type_toEdit = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_Select_Prod_Type_toEdit.setGeometry(QtCore.QRect(1220, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_Select_Prod_Type_toEdit.setFont(font)
        self.comboBox_Select_Prod_Type_toEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_Select_Prod_Type_toEdit.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_Select_Prod_Type_toEdit.setObjectName("comboBox_Select_Prod_Type_toEdit")
        self.comboBox_Select_Prod_Type_toEdit.addItem("")
        self.comboBox_Select_Prod_Type_toEdit.addItem("")
        self.comboBox_Select_Prod_Type_toEdit.addItem("")
        self.comboBox_Select_Prod_Type_toEdit.addItem("")
        self.label_88 = QtWidgets.QLabel(self.frame_7)
        self.label_88.setGeometry(QtCore.QRect(360, 80, 881, 81))
        self.label_88.setStyleSheet("background: transparent;")
        self.label_88.setText("")
        self.label_88.setPixmap(QtGui.QPixmap(":/JJimages/straightline.png"))
        self.label_88.setScaledContents(True)
        self.label_88.setObjectName("label_88")
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_EDIT_STOCK)
        self.page_INV_DELETE_STOCK = QtWidgets.QWidget()
        self.page_INV_DELETE_STOCK.setObjectName("page_INV_DELETE_STOCK")
        self.frame_8 = QtWidgets.QFrame(self.page_INV_DELETE_STOCK)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1621, 691))
        self.frame_8.setStyleSheet("background: #ebe0cc;")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.frame_21 = QtWidgets.QFrame(self.frame_8)
        self.frame_21.setGeometry(QtCore.QRect(0, 0, 1621, 691))
        self.frame_21.setStyleSheet("background: #ebe0cc;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.label_89 = QtWidgets.QLabel(self.frame_21)
        self.label_89.setGeometry(QtCore.QRect(80, 30, 1451, 631))
        self.label_89.setStyleSheet("    background-color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; ")
        self.label_89.setText("")
        self.label_89.setObjectName("label_89")
        self.deleteStocklabel = QtWidgets.QLabel(self.frame_21)
        self.deleteStocklabel.setGeometry(QtCore.QRect(120, 30, 1371, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.deleteStocklabel.setFont(font)
        self.deleteStocklabel.setStyleSheet("    background-color: transparent;\n"
"")
        self.deleteStocklabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deleteStocklabel.setObjectName("deleteStocklabel")
        self.Delete_Select_Prod_Type = QtWidgets.QStackedWidget(self.frame_21)
        self.Delete_Select_Prod_Type.setGeometry(QtCore.QRect(100, 120, 1411, 521))
        self.Delete_Select_Prod_Type.setStyleSheet("background: #f6f3ee;")
        self.Delete_Select_Prod_Type.setObjectName("Delete_Select_Prod_Type")
        self.DELETE_blank = QtWidgets.QWidget()
        self.DELETE_blank.setObjectName("DELETE_blank")
        self.label_90 = QtWidgets.QLabel(self.DELETE_blank)
        self.label_90.setGeometry(QtCore.QRect(0, -10, 1321, 361))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_90.setFont(font)
        self.label_90.setStyleSheet("background: transparent;\n"
"color: #a6a6a6;")
        self.label_90.setAlignment(QtCore.Qt.AlignCenter)
        self.label_90.setObjectName("label_90")
        self.Delete_Select_Prod_Type.addWidget(self.DELETE_blank)
        self.DELETE_ROOF = QtWidgets.QWidget()
        self.DELETE_ROOF.setObjectName("DELETE_ROOF")
        self.frame_22 = QtWidgets.QFrame(self.DELETE_ROOF)
        self.frame_22.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_22.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.pushButton_Confirm_ROOFdelete = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_Confirm_ROOFdelete.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_ROOFdelete.setFont(font)
        self.pushButton_Confirm_ROOFdelete.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_ROOFdelete.setObjectName("pushButton_Confirm_ROOFdelete")
        self.pushButton_Close_ROOFdelete = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_Close_ROOFdelete.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_ROOFdelete.setFont(font)
        self.pushButton_Close_ROOFdelete.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_ROOFdelete.setObjectName("pushButton_Close_ROOFdelete")
        self.frame_deleteroof = QtWidgets.QFrame(self.DELETE_ROOF)
        self.frame_deleteroof.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_deleteroof.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_deleteroof.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_deleteroof.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_deleteroof.setObjectName("frame_deleteroof")
        self.label_97 = QtWidgets.QLabel(self.frame_deleteroof)
        self.label_97.setGeometry(QtCore.QRect(230, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_97.setObjectName("label_97")
        self.lineEdit_DeleteROOF_prodCode = QtWidgets.QLineEdit(self.frame_deleteroof)
        self.lineEdit_DeleteROOF_prodCode.setGeometry(QtCore.QRect(530, 30, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteROOF_prodCode.setFont(font)
        self.lineEdit_DeleteROOF_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteROOF_prodCode.setObjectName("lineEdit_DeleteROOF_prodCode")
        self.label_114 = QtWidgets.QLabel(self.frame_deleteroof)
        self.label_114.setGeometry(QtCore.QRect(230, 110, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_114.setFont(font)
        self.label_114.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_114.setObjectName("label_114")
        self.label_120 = QtWidgets.QLabel(self.frame_deleteroof)
        self.label_120.setGeometry(QtCore.QRect(230, 180, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_120.setFont(font)
        self.label_120.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_120.setObjectName("label_120")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.frame_deleteroof)
        self.lineEdit_28.setGeometry(QtCore.QRect(1030, 460, 371, 51))
        self.lineEdit_28.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_DeleteROOF_Name = QtWidgets.QLineEdit(self.frame_deleteroof)
        self.lineEdit_DeleteROOF_Name.setGeometry(QtCore.QRect(530, 110, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteROOF_Name.setFont(font)
        self.lineEdit_DeleteROOF_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteROOF_Name.setObjectName("lineEdit_DeleteROOF_Name")
        self.label_48 = QtWidgets.QLabel(self.frame_deleteroof)
        self.label_48.setGeometry(QtCore.QRect(0, 265, 1411, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("    background-color: transparent;\n"
"color: #d75413;\n"
"")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.comboBox_DeleteROOF_Type = QtWidgets.QComboBox(self.frame_deleteroof)
        self.comboBox_DeleteROOF_Type.setGeometry(QtCore.QRect(530, 190, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_DeleteROOF_Type.setFont(font)
        self.comboBox_DeleteROOF_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_DeleteROOF_Type.setObjectName("comboBox_DeleteROOF_Type")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.comboBox_DeleteROOF_Type.addItem("")
        self.Delete_Select_Prod_Type.addWidget(self.DELETE_ROOF)
        self.DELETE_SPANDREL = QtWidgets.QWidget()
        self.DELETE_SPANDREL.setObjectName("DELETE_SPANDREL")
        self.frame_24 = QtWidgets.QFrame(self.DELETE_SPANDREL)
        self.frame_24.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_24.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.pushButton_Confirm_SPANDRELdelete = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_Confirm_SPANDRELdelete.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_SPANDRELdelete.setFont(font)
        self.pushButton_Confirm_SPANDRELdelete.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_SPANDRELdelete.setObjectName("pushButton_Confirm_SPANDRELdelete")
        self.pushButton_Close_SPANDRELdelete = QtWidgets.QPushButton(self.frame_24)
        self.pushButton_Close_SPANDRELdelete.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_SPANDRELdelete.setFont(font)
        self.pushButton_Close_SPANDRELdelete.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_SPANDRELdelete.setObjectName("pushButton_Close_SPANDRELdelete")
        self.frame_deletespandrel = QtWidgets.QFrame(self.DELETE_SPANDREL)
        self.frame_deletespandrel.setGeometry(QtCore.QRect(-10, 0, 1411, 411))
        self.frame_deletespandrel.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_deletespandrel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_deletespandrel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_deletespandrel.setObjectName("frame_deletespandrel")
        self.label_93 = QtWidgets.QLabel(self.frame_deletespandrel)
        self.label_93.setGeometry(QtCore.QRect(230, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_93.setFont(font)
        self.label_93.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_93.setObjectName("label_93")
        self.lineEdit_DeleteSPANDREL_prodCode = QtWidgets.QLineEdit(self.frame_deletespandrel)
        self.lineEdit_DeleteSPANDREL_prodCode.setGeometry(QtCore.QRect(530, 30, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteSPANDREL_prodCode.setFont(font)
        self.lineEdit_DeleteSPANDREL_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteSPANDREL_prodCode.setObjectName("lineEdit_DeleteSPANDREL_prodCode")
        self.label_94 = QtWidgets.QLabel(self.frame_deletespandrel)
        self.label_94.setGeometry(QtCore.QRect(230, 110, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_94.setObjectName("label_94")
        self.label_102 = QtWidgets.QLabel(self.frame_deletespandrel)
        self.label_102.setGeometry(QtCore.QRect(230, 180, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_102.setFont(font)
        self.label_102.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_102.setObjectName("label_102")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.frame_deletespandrel)
        self.lineEdit_25.setGeometry(QtCore.QRect(1030, 460, 371, 51))
        self.lineEdit_25.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_DeleteSPANDREL_Name = QtWidgets.QLineEdit(self.frame_deletespandrel)
        self.lineEdit_DeleteSPANDREL_Name.setGeometry(QtCore.QRect(530, 110, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteSPANDREL_Name.setFont(font)
        self.lineEdit_DeleteSPANDREL_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteSPANDREL_Name.setObjectName("lineEdit_DeleteSPANDREL_Name")
        self.label_20 = QtWidgets.QLabel(self.frame_deletespandrel)
        self.label_20.setGeometry(QtCore.QRect(0, 265, 1411, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("    background-color: transparent;\n"
"color: #d75413;\n"
"")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.comboBox_DeleteSPANDREL_Type = QtWidgets.QComboBox(self.frame_deletespandrel)
        self.comboBox_DeleteSPANDREL_Type.setGeometry(QtCore.QRect(530, 190, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_DeleteSPANDREL_Type.setFont(font)
        self.comboBox_DeleteSPANDREL_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_DeleteSPANDREL_Type.setObjectName("comboBox_DeleteSPANDREL_Type")
        self.comboBox_DeleteSPANDREL_Type.addItem("")
        self.comboBox_DeleteSPANDREL_Type.addItem("")
        self.comboBox_DeleteSPANDREL_Type.addItem("")
        self.Delete_Select_Prod_Type.addWidget(self.DELETE_SPANDREL)
        self.DELETE_GUTTER = QtWidgets.QWidget()
        self.DELETE_GUTTER.setObjectName("DELETE_GUTTER")
        self.frame_26 = QtWidgets.QFrame(self.DELETE_GUTTER)
        self.frame_26.setGeometry(QtCore.QRect(-10, 419, 1331, 91))
        self.frame_26.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.pushButton_Confirm_GUTTERdelete = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_Confirm_GUTTERdelete.setGeometry(QtCore.QRect(360, 20, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Confirm_GUTTERdelete.setFont(font)
        self.pushButton_Confirm_GUTTERdelete.setStyleSheet("    background-color: #b2423c;\n"
"    color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.pushButton_Confirm_GUTTERdelete.setObjectName("pushButton_Confirm_GUTTERdelete")
        self.pushButton_Close_GUTTERdelete = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_Close_GUTTERdelete.setGeometry(QtCore.QRect(740, 20, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.pushButton_Close_GUTTERdelete.setFont(font)
        self.pushButton_Close_GUTTERdelete.setStyleSheet("\n"
"/* Default Inactive Button */\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #a6a6a6;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_Close_GUTTERdelete.setObjectName("pushButton_Close_GUTTERdelete")
        self.frame_deletegutter = QtWidgets.QFrame(self.DELETE_GUTTER)
        self.frame_deletegutter.setGeometry(QtCore.QRect(-10, 0, 1411, 421))
        self.frame_deletegutter.setStyleSheet("    background-color: transparent;\n"
"")
        self.frame_deletegutter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_deletegutter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_deletegutter.setObjectName("frame_deletegutter")
        self.label_96 = QtWidgets.QLabel(self.frame_deletegutter)
        self.label_96.setGeometry(QtCore.QRect(230, 20, 321, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_96.setObjectName("label_96")
        self.lineEdit_DeleteGUTTER_prodCode = QtWidgets.QLineEdit(self.frame_deletegutter)
        self.lineEdit_DeleteGUTTER_prodCode.setGeometry(QtCore.QRect(530, 30, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteGUTTER_prodCode.setFont(font)
        self.lineEdit_DeleteGUTTER_prodCode.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteGUTTER_prodCode.setObjectName("lineEdit_DeleteGUTTER_prodCode")
        self.label_106 = QtWidgets.QLabel(self.frame_deletegutter)
        self.label_106.setGeometry(QtCore.QRect(230, 110, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_106.setFont(font)
        self.label_106.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_106.setObjectName("label_106")
        self.label_111 = QtWidgets.QLabel(self.frame_deletegutter)
        self.label_111.setGeometry(QtCore.QRect(230, 180, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("    background-color: transparent;\n"
"")
        self.label_111.setObjectName("label_111")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.frame_deletegutter)
        self.lineEdit_27.setGeometry(QtCore.QRect(1030, 460, 371, 51))
        self.lineEdit_27.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_DeleteGUTTER_Name = QtWidgets.QLineEdit(self.frame_deletegutter)
        self.lineEdit_DeleteGUTTER_Name.setGeometry(QtCore.QRect(530, 110, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_DeleteGUTTER_Name.setFont(font)
        self.lineEdit_DeleteGUTTER_Name.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.lineEdit_DeleteGUTTER_Name.setObjectName("lineEdit_DeleteGUTTER_Name")
        self.label_47 = QtWidgets.QLabel(self.frame_deletegutter)
        self.label_47.setGeometry(QtCore.QRect(0, 265, 1411, 131))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("    background-color: transparent;\n"
"color: #d75413;\n"
"")
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.comboBox_DeleteGUTTER_Type = QtWidgets.QComboBox(self.frame_deletegutter)
        self.comboBox_DeleteGUTTER_Type.setGeometry(QtCore.QRect(530, 190, 641, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox_DeleteGUTTER_Type.setFont(font)
        self.comboBox_DeleteGUTTER_Type.setStyleSheet("    background-color: #ffffff;\n"
"    color: black;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"")
        self.comboBox_DeleteGUTTER_Type.setObjectName("comboBox_DeleteGUTTER_Type")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.comboBox_DeleteGUTTER_Type.addItem("")
        self.Delete_Select_Prod_Type.addWidget(self.DELETE_GUTTER)
        self.comboBox_Select_Prod_Type_toDelete = QtWidgets.QComboBox(self.frame_21)
        self.comboBox_Select_Prod_Type_toDelete.setGeometry(QtCore.QRect(1220, 50, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_Select_Prod_Type_toDelete.setFont(font)
        self.comboBox_Select_Prod_Type_toDelete.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_Select_Prod_Type_toDelete.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_Select_Prod_Type_toDelete.setObjectName("comboBox_Select_Prod_Type_toDelete")
        self.comboBox_Select_Prod_Type_toDelete.addItem("")
        self.comboBox_Select_Prod_Type_toDelete.addItem("")
        self.comboBox_Select_Prod_Type_toDelete.addItem("")
        self.comboBox_Select_Prod_Type_toDelete.addItem("")
        self.label_124 = QtWidgets.QLabel(self.frame_21)
        self.label_124.setGeometry(QtCore.QRect(360, 80, 881, 81))
        self.label_124.setStyleSheet("background: transparent;")
        self.label_124.setText("")
        self.label_124.setPixmap(QtGui.QPixmap(":/JJimages/straightline.png"))
        self.label_124.setScaledContents(True)
        self.label_124.setObjectName("label_124")
        self.INVENTORY_afterBUTTONSclick.addWidget(self.page_INV_DELETE_STOCK)
        self.textBrowser_inv_ROOF_lowstk_warning.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.INVENTORY_afterBUTTONSclick.raise_()
        self.frame_3.raise_()
        self.stackedWidget.addWidget(self.Inventory_page)
        self.Orders_page = QtWidgets.QWidget()
        self.Orders_page.setObjectName("Orders_page")
        self.orders_inview = QtWidgets.QWidget(self.Orders_page)
        self.orders_inview.setGeometry(QtCore.QRect(0, 0, 1631, 1005))
        self.orders_inview.setStyleSheet("background-color:#ffffff;")
        self.orders_inview.setObjectName("orders_inview")
        self.frame_29 = QtWidgets.QFrame(self.orders_inview)
        self.frame_29.setGeometry(QtCore.QRect(40, 30, 461, 71))
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.label_5 = QtWidgets.QLabel(self.frame_29)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(87)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("\n"
"    background-color: #903929;\n"
"    color: white;\n"
"    font-weight: 700;\n"
"    border: 1px solid #000000; \n"
"    padding: 10px;\n"
"    font-family: \"Verdana\", sans-serif; \n"
"    text-align: center;\n"
"\n"
"    /* Only top corners curved */\n"
"    border-top-left-radius: 15px;\n"
"    border-top-right-radius: 15px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tableWidget_ORDERS = QtWidgets.QTableWidget(self.orders_inview)
        self.tableWidget_ORDERS.setGeometry(QtCore.QRect(40, 100, 1521, 861))
        self.tableWidget_ORDERS.setStyleSheet("padding: 1;")
        self.tableWidget_ORDERS.setObjectName("tableWidget_ORDERS")
        self.tableWidget_ORDERS.setColumnCount(12)
        self.tableWidget_ORDERS.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_ORDERS.setHorizontalHeaderItem(11, item)
        self.tableWidget_ORDERS.horizontalHeader().setDefaultSectionSize(265)
        self.comboBox_SortORDERS_high_low = QtWidgets.QComboBox(self.orders_inview)
        self.comboBox_SortORDERS_high_low.setGeometry(QtCore.QRect(1100, 30, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_SortORDERS_high_low.setFont(font)
        self.comboBox_SortORDERS_high_low.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_SortORDERS_high_low.setObjectName("comboBox_SortORDERS_high_low")
        self.comboBox_SortORDERS_high_low.addItem("")
        self.comboBox_SortORDERS_high_low.addItem("")
        self.comboBox_SortORDERS_high_low.addItem("")
        self.frame_29.raise_()
        self.comboBox_SortORDERS_high_low.raise_()
        self.tableWidget_ORDERS.raise_()
        self.stackedWidget.addWidget(self.Orders_page)
        self.Sales_page = QtWidgets.QWidget()
        self.Sales_page.setStyleSheet("background-color:#ffffff;")
        self.Sales_page.setObjectName("Sales_page")
        self.sales_inview = QtWidgets.QWidget(self.Sales_page)
        self.sales_inview.setGeometry(QtCore.QRect(-6, 0, 1931, 1005))
        self.sales_inview.setObjectName("sales_inview")
        self.frame_30 = QtWidgets.QFrame(self.sales_inview)
        self.frame_30.setGeometry(QtCore.QRect(550, 50, 1011, 71))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.comboBox_SR_all_items = QtWidgets.QComboBox(self.frame_30)
        self.comboBox_SR_all_items.setGeometry(QtCore.QRect(60, 10, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_SR_all_items.setFont(font)
        self.comboBox_SR_all_items.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_SR_all_items.setObjectName("comboBox_SR_all_items")
        self.comboBox_SR_all_items.addItem("")
        self.comboBox_SR_all_items.addItem("")
        self.comboBox_SR_all_items.addItem("")
        self.comboBox_SR_all_items.addItem("")
        self.label_17 = QtWidgets.QLabel(self.frame_30)
        self.label_17.setGeometry(QtCore.QRect(480, 20, 51, 31))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/JJimages/moneyhand_icon.svg"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.comboBox_SR_prodType = QtWidgets.QComboBox(self.frame_30)
        self.comboBox_SR_prodType.setGeometry(QtCore.QRect(550, 10, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_SR_prodType.setFont(font)
        self.comboBox_SR_prodType.setStyleSheet("    background-color: #ebe0cc;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; \n"
"text-align: center;")
        self.comboBox_SR_prodType.setObjectName("comboBox_SR_prodType")
        self.comboBox_SR_prodType.addItem("")
        self.comboBox_SR_prodType.addItem("")
        self.comboBox_SR_prodType.addItem("")
        self.comboBox_SR_prodType.addItem("")
        self.stackedWidget_choose_SALES_REPORT = QtWidgets.QStackedWidget(self.sales_inview)
        self.stackedWidget_choose_SALES_REPORT.setGeometry(QtCore.QRect(80, 130, 1461, 801))
        self.stackedWidget_choose_SALES_REPORT.setStyleSheet("background: #f6f3ee;")
        self.stackedWidget_choose_SALES_REPORT.setObjectName("stackedWidget_choose_SALES_REPORT")
        self.page_blank = QtWidgets.QWidget()
        self.page_blank.setObjectName("page_blank")
        self.label_55 = QtWidgets.QLabel(self.page_blank)
        self.label_55.setGeometry(QtCore.QRect(0, 40, 1461, 161))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("background: transparent;\n"
"color: #a6a6a6;")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_blank)
        self.page_DAILY = QtWidgets.QWidget()
        self.page_DAILY.setObjectName("page_DAILY")
        self.tableWidget_SR_DAILY = QtWidgets.QTableWidget(self.page_DAILY)
        self.tableWidget_SR_DAILY.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_DAILY.setStyleSheet("padding: 1;")
        self.tableWidget_SR_DAILY.setObjectName("tableWidget_SR_DAILY")
        self.tableWidget_SR_DAILY.setColumnCount(6)
        self.tableWidget_SR_DAILY.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_DAILY.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_DAILY.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_DAILY)
        self.page_WEEKLY = QtWidgets.QWidget()
        self.page_WEEKLY.setObjectName("page_WEEKLY")
        self.tableWidget_SR_WEEKLY = QtWidgets.QTableWidget(self.page_WEEKLY)
        self.tableWidget_SR_WEEKLY.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_WEEKLY.setStyleSheet("padding: 1;")
        self.tableWidget_SR_WEEKLY.setObjectName("tableWidget_SR_WEEKLY")
        self.tableWidget_SR_WEEKLY.setColumnCount(6)
        self.tableWidget_SR_WEEKLY.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_WEEKLY.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_WEEKLY.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_WEEKLY)
        self.page_MONTHLY = QtWidgets.QWidget()
        self.page_MONTHLY.setObjectName("page_MONTHLY")
        self.tableWidget_SR_MONTHLY = QtWidgets.QTableWidget(self.page_MONTHLY)
        self.tableWidget_SR_MONTHLY.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_MONTHLY.setStyleSheet("padding: 1;")
        self.tableWidget_SR_MONTHLY.setObjectName("tableWidget_SR_MONTHLY")
        self.tableWidget_SR_MONTHLY.setColumnCount(6)
        self.tableWidget_SR_MONTHLY.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_MONTHLY.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_MONTHLY.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_MONTHLY)
        self.page_ROOF = QtWidgets.QWidget()
        self.page_ROOF.setObjectName("page_ROOF")
        self.tableWidget_SR_ROOF = QtWidgets.QTableWidget(self.page_ROOF)
        self.tableWidget_SR_ROOF.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_ROOF.setStyleSheet("padding: 1;")
        self.tableWidget_SR_ROOF.setObjectName("tableWidget_SR_ROOF")
        self.tableWidget_SR_ROOF.setColumnCount(6)
        self.tableWidget_SR_ROOF.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_ROOF.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_ROOF.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_ROOF)
        self.page_SPANDREL = QtWidgets.QWidget()
        self.page_SPANDREL.setObjectName("page_SPANDREL")
        self.tableWidget_SR_SPANDREL = QtWidgets.QTableWidget(self.page_SPANDREL)
        self.tableWidget_SR_SPANDREL.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_SPANDREL.setStyleSheet("padding: 1;")
        self.tableWidget_SR_SPANDREL.setObjectName("tableWidget_SR_SPANDREL")
        self.tableWidget_SR_SPANDREL.setColumnCount(6)
        self.tableWidget_SR_SPANDREL.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_SPANDREL.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_SPANDREL.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_SPANDREL)
        self.page_GUTTER = QtWidgets.QWidget()
        self.page_GUTTER.setObjectName("page_GUTTER")
        self.tableWidget_SR_GUTTER = QtWidgets.QTableWidget(self.page_GUTTER)
        self.tableWidget_SR_GUTTER.setGeometry(QtCore.QRect(0, 0, 1461, 801))
        self.tableWidget_SR_GUTTER.setStyleSheet("padding: 1;")
        self.tableWidget_SR_GUTTER.setObjectName("tableWidget_SR_GUTTER")
        self.tableWidget_SR_GUTTER.setColumnCount(6)
        self.tableWidget_SR_GUTTER.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget_SR_GUTTER.setHorizontalHeaderItem(5, item)
        self.tableWidget_SR_GUTTER.horizontalHeader().setDefaultSectionSize(265)
        self.stackedWidget_choose_SALES_REPORT.addWidget(self.page_GUTTER)
        self.label_91 = QtWidgets.QLabel(self.sales_inview)
        self.label_91.setGeometry(QtCore.QRect(50, 30, 1521, 931))
        self.label_91.setStyleSheet("    background-color: white;\n"
"    border-radius: 15px;\n"
"border: 1px solid #000000; ")
        self.label_91.setText("")
        self.label_91.setObjectName("label_91")
        self.label_6 = QtWidgets.QLabel(self.sales_inview)
        self.label_6.setGeometry(QtCore.QRect(60, 80, 571, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/JJimages/straightline.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.SALES_label = QtWidgets.QLabel(self.sales_inview)
        self.SALES_label.setGeometry(QtCore.QRect(90, 50, 511, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(21)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.SALES_label.setFont(font)
        self.SALES_label.setStyleSheet("    background-color: transparent;\n"
"")
        self.SALES_label.setAlignment(QtCore.Qt.AlignCenter)
        self.SALES_label.setObjectName("SALES_label")
        self.label_91.raise_()
        self.label_6.raise_()
        self.SALES_label.raise_()
        self.stackedWidget_choose_SALES_REPORT.raise_()
        self.frame_30.raise_()
        self.stackedWidget.addWidget(self.Sales_page)
        self.Account_page = QtWidgets.QWidget()
        self.Account_page.setObjectName("Account_page")
        self.widget = QtWidgets.QWidget(self.Account_page)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1661, 1005))
        self.widget.setObjectName("widget")
        self.account_inview = QtWidgets.QWidget(self.widget)
        self.account_inview.setGeometry(QtCore.QRect(0, 0, 1661, 1005))
        self.account_inview.setStyleSheet("background-color:#ffffff;")
        self.account_inview.setObjectName("account_inview")
        self.calendaricon_2 = QtWidgets.QLabel(self.account_inview)
        self.calendaricon_2.setGeometry(QtCore.QRect(30, 40, 191, 121))
        self.calendaricon_2.setText("")
        self.calendaricon_2.setPixmap(QtGui.QPixmap(":/JJimages/dashboardcalendar.png"))
        self.calendaricon_2.setScaledContents(True)
        self.calendaricon_2.setObjectName("calendaricon_2")
        self.stackedWidget_AccountBtns = QtWidgets.QStackedWidget(self.account_inview)
        self.stackedWidget_AccountBtns.setGeometry(QtCore.QRect(0, 260, 1621, 661))
        self.stackedWidget_AccountBtns.setObjectName("stackedWidget_AccountBtns")
        self.VIEW_MY_ACCOUNT = QtWidgets.QWidget()
        self.VIEW_MY_ACCOUNT.setObjectName("VIEW_MY_ACCOUNT")
        self.frame_14 = QtWidgets.QFrame(self.VIEW_MY_ACCOUNT)
        self.frame_14.setGeometry(QtCore.QRect(0, -1, 1621, 671))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_13 = QtWidgets.QFrame(self.frame_14)
        self.frame_13.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_uploadUSER_profile_pic = QtWidgets.QLabel(self.frame_13)
        self.label_uploadUSER_profile_pic.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_uploadUSER_profile_pic.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_uploadUSER_profile_pic.setText("")
        self.label_uploadUSER_profile_pic.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_uploadUSER_profile_pic.setScaledContents(True)
        self.label_uploadUSER_profile_pic.setObjectName("label_uploadUSER_profile_pic")
        self.pushButton_EditAccount = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_EditAccount.setGeometry(QtCore.QRect(70, 480, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.pushButton_EditAccount.setFont(font)
        self.pushButton_EditAccount.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#12245c;\n"
"color:white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #12245c;\n"
"    color: white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"")
        self.pushButton_EditAccount.setObjectName("pushButton_EditAccount")
        self.label_getUSERNAME = QtWidgets.QLabel(self.frame_13)
        self.label_getUSERNAME.setGeometry(QtCore.QRect(0, 430, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_getUSERNAME.setFont(font)
        self.label_getUSERNAME.setStyleSheet("color: #12245c;")
        self.label_getUSERNAME.setAlignment(QtCore.Qt.AlignCenter)
        self.label_getUSERNAME.setObjectName("label_getUSERNAME")
        self.pushButton_ChangePassword = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_ChangePassword.setGeometry(QtCore.QRect(70, 540, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.pushButton_ChangePassword.setFont(font)
        self.pushButton_ChangePassword.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#12245c;\n"
"color:white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #12245c;\n"
"    color: white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"")
        self.pushButton_ChangePassword.setObjectName("pushButton_ChangePassword")
        self.frame_12 = QtWidgets.QFrame(self.frame_14)
        self.frame_12.setGeometry(QtCore.QRect(610, 60, 911, 551))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_12.setFont(font)
        self.frame_12.setStyleSheet("background: transparent;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_2 = QtWidgets.QLabel(self.frame_12)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.frame_12)
        self.label_18.setGeometry(QtCore.QRect(50, 80, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_12)
        self.label_19.setGeometry(QtCore.QRect(50, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_49 = QtWidgets.QLabel(self.frame_12)
        self.label_49.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.frame_12)
        self.label_50.setGeometry(QtCore.QRect(50, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.frame_12)
        self.label_51.setGeometry(QtCore.QRect(50, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.frame_12)
        self.label_52.setGeometry(QtCore.QRect(50, 370, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.frame_12)
        self.label_53.setGeometry(QtCore.QRect(50, 410, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_56 = QtWidgets.QLabel(self.frame_12)
        self.label_56.setGeometry(QtCore.QRect(50, 460, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_storeAccount_ID = QtWidgets.QLabel(self.frame_12)
        self.label_storeAccount_ID.setGeometry(QtCore.QRect(410, 20, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeAccount_ID.setFont(font)
        self.label_storeAccount_ID.setObjectName("label_storeAccount_ID")
        self.label_storeAccount_Role = QtWidgets.QLabel(self.frame_12)
        self.label_storeAccount_Role.setGeometry(QtCore.QRect(410, 80, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeAccount_Role.setFont(font)
        self.label_storeAccount_Role.setObjectName("label_storeAccount_Role")
        self.label_storeFirst_Name = QtWidgets.QLabel(self.frame_12)
        self.label_storeFirst_Name.setGeometry(QtCore.QRect(410, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeFirst_Name.setFont(font)
        self.label_storeFirst_Name.setObjectName("label_storeFirst_Name")
        self.label_storeLast_Name = QtWidgets.QLabel(self.frame_12)
        self.label_storeLast_Name.setGeometry(QtCore.QRect(410, 200, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeLast_Name.setFont(font)
        self.label_storeLast_Name.setObjectName("label_storeLast_Name")
        self.label_storeMiddle_Initial = QtWidgets.QLabel(self.frame_12)
        self.label_storeMiddle_Initial.setGeometry(QtCore.QRect(410, 250, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeMiddle_Initial.setFont(font)
        self.label_storeMiddle_Initial.setObjectName("label_storeMiddle_Initial")
        self.label_storeDate_of_Birth = QtWidgets.QLabel(self.frame_12)
        self.label_storeDate_of_Birth.setGeometry(QtCore.QRect(410, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeDate_of_Birth.setFont(font)
        self.label_storeDate_of_Birth.setObjectName("label_storeDate_of_Birth")
        self.label_storeGender = QtWidgets.QLabel(self.frame_12)
        self.label_storeGender.setGeometry(QtCore.QRect(410, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeGender.setFont(font)
        self.label_storeGender.setObjectName("label_storeGender")
        self.label_storeHome_Address = QtWidgets.QLabel(self.frame_12)
        self.label_storeHome_Address.setGeometry(QtCore.QRect(410, 410, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeHome_Address.setFont(font)
        self.label_storeHome_Address.setObjectName("label_storeHome_Address")
        self.label_storeContact_Num = QtWidgets.QLabel(self.frame_12)
        self.label_storeContact_Num.setGeometry(QtCore.QRect(410, 460, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeContact_Num.setFont(font)
        self.label_storeContact_Num.setObjectName("label_storeContact_Num")
        self.stackedWidget_AccountBtns.addWidget(self.VIEW_MY_ACCOUNT)
        self.Edit_Account = QtWidgets.QWidget()
        self.Edit_Account.setObjectName("Edit_Account")
        self.frame_16 = QtWidgets.QFrame(self.Edit_Account)
        self.frame_16.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.frame_18 = QtWidgets.QFrame(self.frame_16)
        self.frame_18.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_editUSER_profile_pic = QtWidgets.QLabel(self.frame_18)
        self.label_editUSER_profile_pic.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_editUSER_profile_pic.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_editUSER_profile_pic.setText("")
        self.label_editUSER_profile_pic.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_editUSER_profile_pic.setScaledContents(True)
        self.label_editUSER_profile_pic.setObjectName("label_editUSER_profile_pic")
        self.lineEdit_editUSERNAME = QtWidgets.QLineEdit(self.frame_18)
        self.lineEdit_editUSERNAME.setGeometry(QtCore.QRect(10, 430, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editUSERNAME.setFont(font)
        self.lineEdit_editUSERNAME.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editUSERNAME.setText("")
        self.lineEdit_editUSERNAME.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_editUSERNAME.setObjectName("lineEdit_editUSERNAME")
        self.frame_20 = QtWidgets.QFrame(self.frame_16)
        self.frame_20.setGeometry(QtCore.QRect(610, -60, 961, 531))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_20.setFont(font)
        self.frame_20.setStyleSheet("background: transparent;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_59 = QtWidgets.QLabel(self.frame_20)
        self.label_59.setGeometry(QtCore.QRect(50, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.label_60 = QtWidgets.QLabel(self.frame_20)
        self.label_60.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.label_61 = QtWidgets.QLabel(self.frame_20)
        self.label_61.setGeometry(QtCore.QRect(50, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.label_62 = QtWidgets.QLabel(self.frame_20)
        self.label_62.setGeometry(QtCore.QRect(50, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.label_63 = QtWidgets.QLabel(self.frame_20)
        self.label_63.setGeometry(QtCore.QRect(50, 370, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.label_64 = QtWidgets.QLabel(self.frame_20)
        self.label_64.setGeometry(QtCore.QRect(50, 410, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.label_65 = QtWidgets.QLabel(self.frame_20)
        self.label_65.setGeometry(QtCore.QRect(50, 460, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.lineEdit_editFname = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editFname.setGeometry(QtCore.QRect(410, 120, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editFname.setFont(font)
        self.lineEdit_editFname.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editFname.setText("")
        self.lineEdit_editFname.setObjectName("lineEdit_editFname")
        self.lineEdit_editLname = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editLname.setGeometry(QtCore.QRect(410, 180, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editLname.setFont(font)
        self.lineEdit_editLname.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editLname.setText("")
        self.lineEdit_editLname.setObjectName("lineEdit_editLname")
        self.lineEdit_editMidInitial = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editMidInitial.setGeometry(QtCore.QRect(410, 240, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editMidInitial.setFont(font)
        self.lineEdit_editMidInitial.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editMidInitial.setText("")
        self.lineEdit_editMidInitial.setObjectName("lineEdit_editMidInitial")
        self.lineEdit_editDOB = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editDOB.setGeometry(QtCore.QRect(410, 300, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editDOB.setFont(font)
        self.lineEdit_editDOB.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editDOB.setText("")
        self.lineEdit_editDOB.setObjectName("lineEdit_editDOB")
        self.lineEdit_editGender = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editGender.setGeometry(QtCore.QRect(410, 360, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editGender.setFont(font)
        self.lineEdit_editGender.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editGender.setText("")
        self.lineEdit_editGender.setObjectName("lineEdit_editGender")
        self.lineEdit_editHomeAddress = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editHomeAddress.setGeometry(QtCore.QRect(410, 420, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editHomeAddress.setFont(font)
        self.lineEdit_editHomeAddress.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editHomeAddress.setText("")
        self.lineEdit_editHomeAddress.setObjectName("lineEdit_editHomeAddress")
        self.lineEdit_editContactNum = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_editContactNum.setGeometry(QtCore.QRect(410, 480, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editContactNum.setFont(font)
        self.lineEdit_editContactNum.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editContactNum.setText("")
        self.lineEdit_editContactNum.setObjectName("lineEdit_editContactNum")
        self.pushButton_saveEditaccount = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_saveEditaccount.setGeometry(QtCore.QRect(1020, 520, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_saveEditaccount.setFont(font)
        self.pushButton_saveEditaccount.setStyleSheet("\n"
"color: #ffffff;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #b2423c; \n"
"font-weight: 500;\n"
"")
        self.pushButton_saveEditaccount.setObjectName("pushButton_saveEditaccount")
        self.pushButton_cancelEditaccount = QtWidgets.QPushButton(self.frame_16)
        self.pushButton_cancelEditaccount.setGeometry(QtCore.QRect(660, 520, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.pushButton_cancelEditaccount.setFont(font)
        self.pushButton_cancelEditaccount.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#dbdcd8;\n"
"color:black;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #dbdcd8;\n"
"    color: black;\n"
"font-weight: 500;\n"
"}\n"
"")
        self.pushButton_cancelEditaccount.setObjectName("pushButton_cancelEditaccount")
        self.stackedWidget_AccountBtns.addWidget(self.Edit_Account)
        self.Change_Password = QtWidgets.QWidget()
        self.Change_Password.setObjectName("Change_Password")
        self.frame_23 = QtWidgets.QFrame(self.Change_Password)
        self.frame_23.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.label_editUSER_profile_pic_2 = QtWidgets.QLabel(self.frame_25)
        self.label_editUSER_profile_pic_2.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_editUSER_profile_pic_2.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_editUSER_profile_pic_2.setText("")
        self.label_editUSER_profile_pic_2.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_editUSER_profile_pic_2.setScaledContents(True)
        self.label_editUSER_profile_pic_2.setObjectName("label_editUSER_profile_pic_2")
        self.frame_27 = QtWidgets.QFrame(self.frame_23)
        self.frame_27.setGeometry(QtCore.QRect(610, 40, 961, 431))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_27.setFont(font)
        self.frame_27.setStyleSheet("background: transparent;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.label_68 = QtWidgets.QLabel(self.frame_27)
        self.label_68.setGeometry(QtCore.QRect(50, 70, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_68.setFont(font)
        self.label_68.setAlignment(QtCore.Qt.AlignCenter)
        self.label_68.setObjectName("label_68")
        self.label_69 = QtWidgets.QLabel(self.frame_27)
        self.label_69.setGeometry(QtCore.QRect(60, 190, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_69.setFont(font)
        self.label_69.setAlignment(QtCore.Qt.AlignCenter)
        self.label_69.setObjectName("label_69")
        self.label_70 = QtWidgets.QLabel(self.frame_27)
        self.label_70.setGeometry(QtCore.QRect(50, 300, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_70.setFont(font)
        self.label_70.setAlignment(QtCore.Qt.AlignCenter)
        self.label_70.setObjectName("label_70")
        self.lineEdit_enterpass = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_enterpass.setGeometry(QtCore.QRect(50, 120, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_enterpass.setFont(font)
        self.lineEdit_enterpass.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_enterpass.setText("")
        self.lineEdit_enterpass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_enterpass.setObjectName("lineEdit_enterpass")
        self.lineEdit_enterNEWpass = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_enterNEWpass.setGeometry(QtCore.QRect(50, 240, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_enterNEWpass.setFont(font)
        self.lineEdit_enterNEWpass.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_enterNEWpass.setText("")
        self.lineEdit_enterNEWpass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_enterNEWpass.setObjectName("lineEdit_enterNEWpass")
        self.lineEdit_confirmNEWpass = QtWidgets.QLineEdit(self.frame_27)
        self.lineEdit_confirmNEWpass.setGeometry(QtCore.QRect(50, 360, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_confirmNEWpass.setFont(font)
        self.lineEdit_confirmNEWpass.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_confirmNEWpass.setText("")
        self.lineEdit_confirmNEWpass.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_confirmNEWpass.setObjectName("lineEdit_confirmNEWpass")
        self.pushButton_saveNEWpassword = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_saveNEWpassword.setGeometry(QtCore.QRect(700, 510, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_saveNEWpassword.setFont(font)
        self.pushButton_saveNEWpassword.setStyleSheet("\n"
"color: #ffffff;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #b2423c; \n"
"font-weight: 500;\n"
"")
        self.pushButton_saveNEWpassword.setObjectName("pushButton_saveNEWpassword")
        self.pushButton_cancelNEWpassword = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_cancelNEWpassword.setGeometry(QtCore.QRect(1000, 510, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.pushButton_cancelNEWpassword.setFont(font)
        self.pushButton_cancelNEWpassword.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#dbdcd8;\n"
"color:black;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #dbdcd8;\n"
"    color: black;\n"
"font-weight: 500;\n"
"}\n"
"")
        self.pushButton_cancelNEWpassword.setObjectName("pushButton_cancelNEWpassword")
        self.stackedWidget_AccountBtns.addWidget(self.Change_Password)
        self.VIEW_CASHIER_ACCOUNT = QtWidgets.QWidget()
        self.VIEW_CASHIER_ACCOUNT.setObjectName("VIEW_CASHIER_ACCOUNT")
        self.frame_28 = QtWidgets.QFrame(self.VIEW_CASHIER_ACCOUNT)
        self.frame_28.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.frame_31 = QtWidgets.QFrame(self.frame_28)
        self.frame_31.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.label_uploadUSER_profile_pic_cashier = QtWidgets.QLabel(self.frame_31)
        self.label_uploadUSER_profile_pic_cashier.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_uploadUSER_profile_pic_cashier.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_uploadUSER_profile_pic_cashier.setText("")
        self.label_uploadUSER_profile_pic_cashier.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_uploadUSER_profile_pic_cashier.setScaledContents(True)
        self.label_uploadUSER_profile_pic_cashier.setObjectName("label_uploadUSER_profile_pic_cashier")
        self.pushButton_EditAccount_cashier = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_EditAccount_cashier.setGeometry(QtCore.QRect(70, 480, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.pushButton_EditAccount_cashier.setFont(font)
        self.pushButton_EditAccount_cashier.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#12245c;\n"
"color:white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #12245c;\n"
"    color: white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"")
        self.pushButton_EditAccount_cashier.setObjectName("pushButton_EditAccount_cashier")
        self.label_getUSERNAME_cashier = QtWidgets.QLabel(self.frame_31)
        self.label_getUSERNAME_cashier.setGeometry(QtCore.QRect(0, 430, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_getUSERNAME_cashier.setFont(font)
        self.label_getUSERNAME_cashier.setStyleSheet("color: #12245c;")
        self.label_getUSERNAME_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.label_getUSERNAME_cashier.setObjectName("label_getUSERNAME_cashier")
        self.pushButton_ChangePassword_cashier = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_ChangePassword_cashier.setGeometry(QtCore.QRect(70, 540, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(12)
        self.pushButton_ChangePassword_cashier.setFont(font)
        self.pushButton_ChangePassword_cashier.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#12245c;\n"
"color:white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #12245c;\n"
"    color: white;\n"
"font-weight: 500;\n"
"border-radius: 9px; \n"
"}\n"
"")
        self.pushButton_ChangePassword_cashier.setObjectName("pushButton_ChangePassword_cashier")
        self.frame_32 = QtWidgets.QFrame(self.frame_28)
        self.frame_32.setGeometry(QtCore.QRect(610, 60, 911, 551))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_32.setFont(font)
        self.frame_32.setStyleSheet("background: transparent;")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.label_3 = QtWidgets.QLabel(self.frame_32)
        self.label_3.setGeometry(QtCore.QRect(50, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_66 = QtWidgets.QLabel(self.frame_32)
        self.label_66.setGeometry(QtCore.QRect(50, 80, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.label_67 = QtWidgets.QLabel(self.frame_32)
        self.label_67.setGeometry(QtCore.QRect(50, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.label_71 = QtWidgets.QLabel(self.frame_32)
        self.label_71.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.label_72 = QtWidgets.QLabel(self.frame_32)
        self.label_72.setGeometry(QtCore.QRect(50, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.frame_32)
        self.label_73.setGeometry(QtCore.QRect(50, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.label_74 = QtWidgets.QLabel(self.frame_32)
        self.label_74.setGeometry(QtCore.QRect(50, 370, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.frame_32)
        self.label_75.setGeometry(QtCore.QRect(50, 410, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.frame_32)
        self.label_76.setGeometry(QtCore.QRect(50, 460, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_storeAccount_ID_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeAccount_ID_cashier.setGeometry(QtCore.QRect(410, 20, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeAccount_ID_cashier.setFont(font)
        self.label_storeAccount_ID_cashier.setObjectName("label_storeAccount_ID_cashier")
        self.label_storeAccount_Role_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeAccount_Role_cashier.setGeometry(QtCore.QRect(410, 80, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeAccount_Role_cashier.setFont(font)
        self.label_storeAccount_Role_cashier.setObjectName("label_storeAccount_Role_cashier")
        self.label_storeFirst_Name_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeFirst_Name_cashier.setGeometry(QtCore.QRect(410, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeFirst_Name_cashier.setFont(font)
        self.label_storeFirst_Name_cashier.setObjectName("label_storeFirst_Name_cashier")
        self.label_storeLast_Name_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeLast_Name_cashier.setGeometry(QtCore.QRect(410, 200, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeLast_Name_cashier.setFont(font)
        self.label_storeLast_Name_cashier.setObjectName("label_storeLast_Name_cashier")
        self.label_storeMiddle_Initial_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeMiddle_Initial_cashier.setGeometry(QtCore.QRect(410, 250, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeMiddle_Initial_cashier.setFont(font)
        self.label_storeMiddle_Initial_cashier.setObjectName("label_storeMiddle_Initial_cashier")
        self.label_storeDate_of_Birth_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeDate_of_Birth_cashier.setGeometry(QtCore.QRect(410, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeDate_of_Birth_cashier.setFont(font)
        self.label_storeDate_of_Birth_cashier.setObjectName("label_storeDate_of_Birth_cashier")
        self.label_storeGender_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeGender_cashier.setGeometry(QtCore.QRect(410, 370, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeGender_cashier.setFont(font)
        self.label_storeGender_cashier.setObjectName("label_storeGender_cashier")
        self.label_storeHome_Address_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeHome_Address_cashier.setGeometry(QtCore.QRect(410, 410, 481, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeHome_Address_cashier.setFont(font)
        self.label_storeHome_Address_cashier.setObjectName("label_storeHome_Address_cashier")
        self.label_storeContact_Num_cashier = QtWidgets.QLabel(self.frame_32)
        self.label_storeContact_Num_cashier.setGeometry(QtCore.QRect(410, 460, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_storeContact_Num_cashier.setFont(font)
        self.label_storeContact_Num_cashier.setObjectName("label_storeContact_Num_cashier")
        self.stackedWidget_AccountBtns.addWidget(self.VIEW_CASHIER_ACCOUNT)
        self.Edit_Account_cashier = QtWidgets.QWidget()
        self.Edit_Account_cashier.setObjectName("Edit_Account_cashier")
        self.frame_33 = QtWidgets.QFrame(self.Edit_Account_cashier)
        self.frame_33.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.frame_34 = QtWidgets.QFrame(self.frame_33)
        self.frame_34.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.label_editUSER_profile_pic_cashier = QtWidgets.QLabel(self.frame_34)
        self.label_editUSER_profile_pic_cashier.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_editUSER_profile_pic_cashier.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_editUSER_profile_pic_cashier.setText("")
        self.label_editUSER_profile_pic_cashier.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_editUSER_profile_pic_cashier.setScaledContents(True)
        self.label_editUSER_profile_pic_cashier.setObjectName("label_editUSER_profile_pic_cashier")
        self.frame_35 = QtWidgets.QFrame(self.frame_33)
        self.frame_35.setGeometry(QtCore.QRect(610, -60, 961, 561))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_35.setFont(font)
        self.frame_35.setStyleSheet("background: transparent;")
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.label_79 = QtWidgets.QLabel(self.frame_35)
        self.label_79.setGeometry(QtCore.QRect(50, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.frame_35)
        self.label_80.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.label_81 = QtWidgets.QLabel(self.frame_35)
        self.label_81.setGeometry(QtCore.QRect(50, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.label_82 = QtWidgets.QLabel(self.frame_35)
        self.label_82.setGeometry(QtCore.QRect(50, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.label_83 = QtWidgets.QLabel(self.frame_35)
        self.label_83.setGeometry(QtCore.QRect(50, 370, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.frame_35)
        self.label_84.setGeometry(QtCore.QRect(50, 410, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.label_85 = QtWidgets.QLabel(self.frame_35)
        self.label_85.setGeometry(QtCore.QRect(50, 460, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.lineEdit_editFname_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editFname_cashier.setGeometry(QtCore.QRect(410, 120, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editFname_cashier.setFont(font)
        self.lineEdit_editFname_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editFname_cashier.setText("")
        self.lineEdit_editFname_cashier.setObjectName("lineEdit_editFname_cashier")
        self.lineEdit_editLname_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editLname_cashier.setGeometry(QtCore.QRect(410, 180, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editLname_cashier.setFont(font)
        self.lineEdit_editLname_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editLname_cashier.setText("")
        self.lineEdit_editLname_cashier.setObjectName("lineEdit_editLname_cashier")
        self.lineEdit_editMidInitial_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editMidInitial_cashier.setGeometry(QtCore.QRect(410, 240, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editMidInitial_cashier.setFont(font)
        self.lineEdit_editMidInitial_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editMidInitial_cashier.setText("")
        self.lineEdit_editMidInitial_cashier.setObjectName("lineEdit_editMidInitial_cashier")
        self.lineEdit_editDOB_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editDOB_cashier.setGeometry(QtCore.QRect(410, 300, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editDOB_cashier.setFont(font)
        self.lineEdit_editDOB_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editDOB_cashier.setText("")
        self.lineEdit_editDOB_cashier.setObjectName("lineEdit_editDOB_cashier")
        self.lineEdit_editGender_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editGender_cashier.setGeometry(QtCore.QRect(410, 360, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editGender_cashier.setFont(font)
        self.lineEdit_editGender_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editGender_cashier.setText("")
        self.lineEdit_editGender_cashier.setObjectName("lineEdit_editGender_cashier")
        self.lineEdit_editHomeAddress_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editHomeAddress_cashier.setGeometry(QtCore.QRect(410, 420, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editHomeAddress_cashier.setFont(font)
        self.lineEdit_editHomeAddress_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editHomeAddress_cashier.setText("")
        self.lineEdit_editHomeAddress_cashier.setObjectName("lineEdit_editHomeAddress_cashier")
        self.lineEdit_editContactNum_cashier = QtWidgets.QLineEdit(self.frame_35)
        self.lineEdit_editContactNum_cashier.setGeometry(QtCore.QRect(410, 480, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editContactNum_cashier.setFont(font)
        self.lineEdit_editContactNum_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editContactNum_cashier.setText("")
        self.lineEdit_editContactNum_cashier.setObjectName("lineEdit_editContactNum_cashier")
        self.lineEdit_editUSERNAME_cashier = QtWidgets.QLineEdit(self.frame_33)
        self.lineEdit_editUSERNAME_cashier.setGeometry(QtCore.QRect(90, 470, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_editUSERNAME_cashier.setFont(font)
        self.lineEdit_editUSERNAME_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_editUSERNAME_cashier.setText("")
        self.lineEdit_editUSERNAME_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_editUSERNAME_cashier.setObjectName("lineEdit_editUSERNAME_cashier")
        self.pushButton_saveEditaccount_cashier = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_saveEditaccount_cashier.setGeometry(QtCore.QRect(1020, 520, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_saveEditaccount_cashier.setFont(font)
        self.pushButton_saveEditaccount_cashier.setStyleSheet("\n"
"color: #ffffff;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #b2423c; \n"
"font-weight: 500;\n"
"")
        self.pushButton_saveEditaccount_cashier.setObjectName("pushButton_saveEditaccount_cashier")
        self.pushButton_cancelEditaccount_cashier = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_cancelEditaccount_cashier.setGeometry(QtCore.QRect(660, 520, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.pushButton_cancelEditaccount_cashier.setFont(font)
        self.pushButton_cancelEditaccount_cashier.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#dbdcd8;\n"
"color:black;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #dbdcd8;\n"
"    color: black;\n"
"font-weight: 500;\n"
"}\n"
"")
        self.pushButton_cancelEditaccount_cashier.setObjectName("pushButton_cancelEditaccount_cashier")
        self.stackedWidget_AccountBtns.addWidget(self.Edit_Account_cashier)
        self.Change_Password_cashier = QtWidgets.QWidget()
        self.Change_Password_cashier.setObjectName("Change_Password_cashier")
        self.frame_36 = QtWidgets.QFrame(self.Change_Password_cashier)
        self.frame_36.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.frame_37 = QtWidgets.QFrame(self.frame_36)
        self.frame_37.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.label_editUSER_profile_pic_4 = QtWidgets.QLabel(self.frame_37)
        self.label_editUSER_profile_pic_4.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_editUSER_profile_pic_4.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_editUSER_profile_pic_4.setText("")
        self.label_editUSER_profile_pic_4.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_editUSER_profile_pic_4.setScaledContents(True)
        self.label_editUSER_profile_pic_4.setObjectName("label_editUSER_profile_pic_4")
        self.frame_38 = QtWidgets.QFrame(self.frame_36)
        self.frame_38.setGeometry(QtCore.QRect(610, 40, 961, 421))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_38.setFont(font)
        self.frame_38.setStyleSheet("background: transparent;")
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.label_86 = QtWidgets.QLabel(self.frame_38)
        self.label_86.setGeometry(QtCore.QRect(50, 70, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_86.setFont(font)
        self.label_86.setAlignment(QtCore.Qt.AlignCenter)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.frame_38)
        self.label_87.setGeometry(QtCore.QRect(60, 190, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_87.setFont(font)
        self.label_87.setAlignment(QtCore.Qt.AlignCenter)
        self.label_87.setObjectName("label_87")
        self.label_92 = QtWidgets.QLabel(self.frame_38)
        self.label_92.setGeometry(QtCore.QRect(50, 300, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_92.setFont(font)
        self.label_92.setAlignment(QtCore.Qt.AlignCenter)
        self.label_92.setObjectName("label_92")
        self.lineEdit_enterpass_cashier = QtWidgets.QLineEdit(self.frame_38)
        self.lineEdit_enterpass_cashier.setGeometry(QtCore.QRect(50, 120, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_enterpass_cashier.setFont(font)
        self.lineEdit_enterpass_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_enterpass_cashier.setText("")
        self.lineEdit_enterpass_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_enterpass_cashier.setObjectName("lineEdit_enterpass_cashier")
        self.lineEdit_enterNEWpass_cashier = QtWidgets.QLineEdit(self.frame_38)
        self.lineEdit_enterNEWpass_cashier.setGeometry(QtCore.QRect(50, 240, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_enterNEWpass_cashier.setFont(font)
        self.lineEdit_enterNEWpass_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_enterNEWpass_cashier.setText("")
        self.lineEdit_enterNEWpass_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_enterNEWpass_cashier.setObjectName("lineEdit_enterNEWpass_cashier")
        self.lineEdit_confirmNEWpass_cashier = QtWidgets.QLineEdit(self.frame_38)
        self.lineEdit_confirmNEWpass_cashier.setGeometry(QtCore.QRect(50, 360, 571, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_confirmNEWpass_cashier.setFont(font)
        self.lineEdit_confirmNEWpass_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_confirmNEWpass_cashier.setText("")
        self.lineEdit_confirmNEWpass_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_confirmNEWpass_cashier.setObjectName("lineEdit_confirmNEWpass_cashier")
        self.pushButton_saveNEWpassword_cashier = QtWidgets.QPushButton(self.frame_36)
        self.pushButton_saveNEWpassword_cashier.setGeometry(QtCore.QRect(700, 510, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_saveNEWpassword_cashier.setFont(font)
        self.pushButton_saveNEWpassword_cashier.setStyleSheet("\n"
"color: #ffffff;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #b2423c; \n"
"font-weight: 500;\n"
"")
        self.pushButton_saveNEWpassword_cashier.setObjectName("pushButton_saveNEWpassword_cashier")
        self.pushButton_cancelNEWpassword_cashier = QtWidgets.QPushButton(self.frame_36)
        self.pushButton_cancelNEWpassword_cashier.setGeometry(QtCore.QRect(1000, 510, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.pushButton_cancelNEWpassword_cashier.setFont(font)
        self.pushButton_cancelNEWpassword_cashier.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#dbdcd8;\n"
"color:black;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #dbdcd8;\n"
"    color: black;\n"
"font-weight: 500;\n"
"}\n"
"")
        self.pushButton_cancelNEWpassword_cashier.setObjectName("pushButton_cancelNEWpassword_cashier")
        self.stackedWidget_AccountBtns.addWidget(self.Change_Password_cashier)
        self.CREATE_NEW_CASHIER_ACCOUNT = QtWidgets.QWidget()
        self.CREATE_NEW_CASHIER_ACCOUNT.setObjectName("CREATE_NEW_CASHIER_ACCOUNT")
        self.frame_39 = QtWidgets.QFrame(self.CREATE_NEW_CASHIER_ACCOUNT)
        self.frame_39.setGeometry(QtCore.QRect(0, 0, 1621, 671))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.frame_40 = QtWidgets.QFrame(self.frame_39)
        self.frame_40.setGeometry(QtCore.QRect(80, 40, 491, 621))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.label_createUSER_profile_pic_cashier = QtWidgets.QLabel(self.frame_40)
        self.label_createUSER_profile_pic_cashier.setGeometry(QtCore.QRect(40, 20, 400, 400))
        self.label_createUSER_profile_pic_cashier.setStyleSheet("border-radius: 200px;   /* half of 400 */\n"
"border: 2px solid #12245c;  /* optional: blue border */\n"
"")
        self.label_createUSER_profile_pic_cashier.setText("")
        self.label_createUSER_profile_pic_cashier.setPixmap(QtGui.QPixmap(":/JJimages/userProfilepicture.png"))
        self.label_createUSER_profile_pic_cashier.setScaledContents(True)
        self.label_createUSER_profile_pic_cashier.setObjectName("label_createUSER_profile_pic_cashier")
        self.lineEdit_createUSERNAME_cashier = QtWidgets.QLineEdit(self.frame_40)
        self.lineEdit_createUSERNAME_cashier.setGeometry(QtCore.QRect(10, 430, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_createUSERNAME_cashier.setFont(font)
        self.lineEdit_createUSERNAME_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_createUSERNAME_cashier.setText("")
        self.lineEdit_createUSERNAME_cashier.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_createUSERNAME_cashier.setObjectName("lineEdit_createUSERNAME_cashier")
        self.frame_41 = QtWidgets.QFrame(self.frame_39)
        self.frame_41.setGeometry(QtCore.QRect(610, -60, 961, 561))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.frame_41.setFont(font)
        self.frame_41.setStyleSheet("background: transparent;")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.label_100 = QtWidgets.QLabel(self.frame_41)
        self.label_100.setGeometry(QtCore.QRect(50, 140, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.label_101 = QtWidgets.QLabel(self.frame_41)
        self.label_101.setGeometry(QtCore.QRect(50, 200, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.label_103 = QtWidgets.QLabel(self.frame_41)
        self.label_103.setGeometry(QtCore.QRect(50, 250, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.label_104 = QtWidgets.QLabel(self.frame_41)
        self.label_104.setGeometry(QtCore.QRect(50, 310, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_104.setFont(font)
        self.label_104.setObjectName("label_104")
        self.label_121 = QtWidgets.QLabel(self.frame_41)
        self.label_121.setGeometry(QtCore.QRect(50, 370, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_121.setFont(font)
        self.label_121.setObjectName("label_121")
        self.label_122 = QtWidgets.QLabel(self.frame_41)
        self.label_122.setGeometry(QtCore.QRect(50, 410, 311, 71))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_122.setFont(font)
        self.label_122.setObjectName("label_122")
        self.label_123 = QtWidgets.QLabel(self.frame_41)
        self.label_123.setGeometry(QtCore.QRect(50, 460, 321, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(17)
        self.label_123.setFont(font)
        self.label_123.setObjectName("label_123")
        self.lineEdit__createFname_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createFname_cashier.setGeometry(QtCore.QRect(410, 120, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createFname_cashier.setFont(font)
        self.lineEdit__createFname_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createFname_cashier.setText("")
        self.lineEdit__createFname_cashier.setObjectName("lineEdit__createFname_cashier")
        self.lineEdit__createLname_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createLname_cashier.setGeometry(QtCore.QRect(410, 180, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createLname_cashier.setFont(font)
        self.lineEdit__createLname_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createLname_cashier.setText("")
        self.lineEdit__createLname_cashier.setObjectName("lineEdit__createLname_cashier")
        self.lineEdit__createMidInitial_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createMidInitial_cashier.setGeometry(QtCore.QRect(410, 240, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createMidInitial_cashier.setFont(font)
        self.lineEdit__createMidInitial_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createMidInitial_cashier.setText("")
        self.lineEdit__createMidInitial_cashier.setObjectName("lineEdit__createMidInitial_cashier")
        self.lineEdit__createDOB_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createDOB_cashier.setGeometry(QtCore.QRect(410, 300, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createDOB_cashier.setFont(font)
        self.lineEdit__createDOB_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createDOB_cashier.setText("")
        self.lineEdit__createDOB_cashier.setObjectName("lineEdit__createDOB_cashier")
        self.lineEdit__createGender_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createGender_cashier.setGeometry(QtCore.QRect(410, 360, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createGender_cashier.setFont(font)
        self.lineEdit__createGender_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createGender_cashier.setText("")
        self.lineEdit__createGender_cashier.setObjectName("lineEdit__createGender_cashier")
        self.lineEdit__createHomeAddress_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit__createHomeAddress_cashier.setGeometry(QtCore.QRect(410, 420, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit__createHomeAddress_cashier.setFont(font)
        self.lineEdit__createHomeAddress_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit__createHomeAddress_cashier.setText("")
        self.lineEdit__createHomeAddress_cashier.setObjectName("lineEdit__createHomeAddress_cashier")
        self.lineEdit_createContactNum_cashier = QtWidgets.QLineEdit(self.frame_41)
        self.lineEdit_createContactNum_cashier.setGeometry(QtCore.QRect(410, 480, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_createContactNum_cashier.setFont(font)
        self.lineEdit_createContactNum_cashier.setStyleSheet("border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 1px;")
        self.lineEdit_createContactNum_cashier.setText("")
        self.lineEdit_createContactNum_cashier.setObjectName("lineEdit_createContactNum_cashier")
        self.pushButton_CreateAccount_cashier = QtWidgets.QPushButton(self.frame_39)
        self.pushButton_CreateAccount_cashier.setGeometry(QtCore.QRect(1020, 530, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(62)
        self.pushButton_CreateAccount_cashier.setFont(font)
        self.pushButton_CreateAccount_cashier.setStyleSheet("\n"
"color: #ffffff;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #b2423c; \n"
"font-weight: 500;\n"
"")
        self.pushButton_CreateAccount_cashier.setObjectName("pushButton_CreateAccount_cashier")
        self.pushButton_cancelCreateAccount_cashier = QtWidgets.QPushButton(self.frame_39)
        self.pushButton_cancelCreateAccount_cashier.setGeometry(QtCore.QRect(660, 530, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.pushButton_cancelCreateAccount_cashier.setFont(font)
        self.pushButton_cancelCreateAccount_cashier.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"color: #000000;\n"
"border: 1px solid #000000; \n"
"border-radius: 9px; \n"
"padding: 3px; \n"
"background-color: #ffffff; \n"
"}\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#dbdcd8;\n"
"color:black;\n"
"font-weight: 500;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #dbdcd8;\n"
"    color: black;\n"
"font-weight: 500;\n"
"}\n"
"")
        self.pushButton_cancelCreateAccount_cashier.setObjectName("pushButton_cancelCreateAccount_cashier")
        self.stackedWidget_AccountBtns.addWidget(self.CREATE_NEW_CASHIER_ACCOUNT)
        self.frame = QtWidgets.QFrame(self.account_inview)
        self.frame.setGeometry(QtCore.QRect(0, 200, 1621, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_VIEW = QtWidgets.QPushButton(self.frame)
        self.pushButton_VIEW.setGeometry(QtCore.QRect(0, 0, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.pushButton_VIEW.setFont(font)
        self.pushButton_VIEW.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #f6f3ee;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#374550;\n"
"color:white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #374550;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_VIEW.setObjectName("pushButton_VIEW")
        self.pushButton_VIEW_C = QtWidgets.QPushButton(self.frame)
        self.pushButton_VIEW_C.setGeometry(QtCore.QRect(440, 0, 541, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.pushButton_VIEW_C.setFont(font)
        self.pushButton_VIEW_C.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #f6f3ee;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#374550;\n"
"color:white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #374550;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_VIEW_C.setObjectName("pushButton_VIEW_C")
        self.pushButton_CREATE_C = QtWidgets.QPushButton(self.frame)
        self.pushButton_CREATE_C.setGeometry(QtCore.QRect(980, 0, 651, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        self.pushButton_CREATE_C.setFont(font)
        self.pushButton_CREATE_C.setStyleSheet("/* Default Inactive Buttons */\n"
"QPushButton {\n"
"    background-color: #f6f3ee;\n"
"    color: black;\n"
"border: 1px solid #000000; \n"
"    padding: 9px;\n"
"font-family: \"Verdana\", sans-serif; \n"
"text-align: center;\n"
"}\n"
"\n"
"/* Hover Effect on Inactive Buttons */\n"
"QPushButton:hover {\n"
"    background-color:#374550;\n"
"color:white;\n"
"}\n"
"\n"
"/* Active Button (Current Page) */\n"
"QPushButton#activeButton {\n"
"    background-color: #374550;\n"
"    color: white;\n"
"}\n"
"")
        self.pushButton_CREATE_C.setObjectName("pushButton_CREATE_C")
        self.frame_2 = QtWidgets.QFrame(self.account_inview)
        self.frame_2.setGeometry(QtCore.QRect(0, 930, 1621, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.account_inview)
        self.label.setGeometry(QtCore.QRect(0, 930, 1631, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: #374550;\n"
"padding: 2px;\n"
"color: #ffffff;\n"
"text-align: center;\n"
"")
        self.label.setObjectName("label")
        self.dateLabel_inAccount = QtWidgets.QLabel(self.account_inview)
        self.dateLabel_inAccount.setGeometry(QtCore.QRect(0, 10, 951, 191))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.dateLabel_inAccount.setFont(font)
        self.dateLabel_inAccount.setStyleSheet("QLabel {\n"
"    background-color: white;\n"
"    border: 1px solid black;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"background: transparent;\n"
"}\n"
"")
        self.dateLabel_inAccount.setTextFormat(QtCore.Qt.RichText)
        self.dateLabel_inAccount.setObjectName("dateLabel_inAccount")
        self.timeLabel_inAccount = QtWidgets.QLabel(self.account_inview)
        self.timeLabel_inAccount.setGeometry(QtCore.QRect(950, 10, 671, 191))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.timeLabel_inAccount.setFont(font)
        self.timeLabel_inAccount.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: 1px solid black;\n"
"    padding: 10px;\n"
"    text-align: center;\n"
"}\n"
"")
        self.timeLabel_inAccount.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel_inAccount.setObjectName("timeLabel_inAccount")
        self.stackedWidget_AccountBtns.raise_()
        self.calendaricon_2.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.label.raise_()
        self.dateLabel_inAccount.raise_()
        self.timeLabel_inAccount.raise_()
        self.stackedWidget.addWidget(self.Account_page)
        self.stackedWidget.raise_()
        self.LeftMenuBar.raise_()
        OWNER.setCentralWidget(self.Owner_centralwidget)
        self.statusbar = QtWidgets.QStatusBar(OWNER)
        self.statusbar.setObjectName("statusbar")
        OWNER.setStatusBar(self.statusbar)

        self.retranslateUi(OWNER)
        self.stackedWidget.setCurrentIndex(1)
        self.INVENTORY_afterBUTTONSclick.setCurrentIndex(3)
        self.Add_Select_Prod_Type.setCurrentIndex(1)
        self.Edit_Select_Prod_Type.setCurrentIndex(3)
        self.Delete_Select_Prod_Type.setCurrentIndex(3)
        self.stackedWidget_choose_SALES_REPORT.setCurrentIndex(6)
        self.stackedWidget_AccountBtns.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(OWNER)

    def retranslateUi(self, OWNER):
        _translate = QtCore.QCoreApplication.translate
        OWNER.setWindowTitle(_translate("OWNER", "Inventory and Sales Management System"))
        self.JJelevate_text.setText(_translate("OWNER", "J & J ELEVATE"))
        self.pushButton_Dashboard.setText(_translate("OWNER", " Dashboard"))
        self.pushButton_Inventory.setText(_translate("OWNER", "Inventory"))
        self.pushButton_Orders.setText(_translate("OWNER", " Orders"))
        self.pushButton_Sales.setText(_translate("OWNER", "  Sales"))
        self.pushButton_Account.setText(_translate("OWNER", " Account"))
        self.pushButton_LogOut.setText(_translate("OWNER", "Log out"))
        self.label_10.setText(_translate("OWNER", "Best Sellers"))
        self.btnViewSalesReport.setText(_translate("OWNER", "View Sales Report"))
        self.value_Tod_sales.setText(_translate("OWNER", "800,000"))
        self.label_4.setText(_translate("OWNER", "Today’s Sales"))
        self.label_11.setText(_translate("OWNER", "Inventory"))
        self.btnViewMore_Inventory.setText(_translate("OWNER", "View More in Inventory"))
        self.dashb_lowinstock_value.setText(_translate("OWNER", "4 items"))
        self.label_12.setText(_translate("OWNER", "Low in Stock"))
        self.label_13.setText(_translate("OWNER", "Warning! These items are low of stock."))
        self.top1LOWEST_STOCK_PRODUCT.setText(_translate("OWNER", "Product Name"))
        self.top2LOWSTOCK_PRODUCT.setText(_translate("OWNER", "Product Name"))
        self.top3LOWSTOCK_PRODUCT.setText(_translate("OWNER", "Product Name"))
        self.top4LOWSTOCK_PRODUCT.setText(_translate("OWNER", "Product Name"))
        self.top4LOWSTOCK_PROD_QTY.setText(_translate("OWNER", "ONLY 5 LEFT"))
        self.top3LOWSTOCK_PROD_QTY.setText(_translate("OWNER", "ONLY 4 LEFT"))
        self.top2LOWSTOCK_PROD_QTY.setText(_translate("OWNER", "ONLY 2 LEFT"))
        self.top1LOWEST_STOCK_PROD_QTY.setText(_translate("OWNER", "ONLY 1 LEFT"))
        self.value_Tod_orders.setText(_translate("OWNER", "300"))
        self.label_8.setText(_translate("OWNER", "Today’s Total Orders"))
        self.value_Tod_revenue.setText(_translate("OWNER", "900,000"))
        self.label_9.setText(_translate("OWNER", "Today’s Revenue"))
        self.dateLabel.setText(_translate("OWNER", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt;\">March 31, 2025 </span><span style=\" font-size:48pt; color:#ffffff;\">.</span></p><p align=\"center\"><span style=\" font-size:20pt;\">Monday</span><span style=\" font-size:16pt; color:#ffffff;\">....................................</span></p></body></html>"))
        self.timeLabel.setText(_translate("OWNER", " 09 : 10 : 54 AM"))
        self.pushButton_Inventory_ALL_ITEMS_table.setText(_translate("OWNER", "ALL ITEMS"))
        self.pushButton_Inventory_ROOF_table.setText(_translate("OWNER", "ROOF"))
        self.pushButton_Inventory_SPANDREL_table.setText(_translate("OWNER", "SPANDREL"))
        self.pushButton_Inventory_GUTTER_table.setText(_translate("OWNER", "GUTTER"))
        self.lineEdit_OWNER_QuickSearch_Inventory.setPlaceholderText(_translate("OWNER", "      Quick Search"))
        self.pushButton_OWNER_Add_Inventory.setText(_translate("OWNER", "ADD"))
        self.pushButton_OWNER_Edit_Inventory.setText(_translate("OWNER", "EDIT"))
        self.pushButton_OWNER_Delete_Inventory.setText(_translate("OWNER", "DELETE"))
        self.textBrowser_inv_ROOF_lowstk_warning.setHtml(_translate("OWNER", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\',\'sans-serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "NAME"))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "DESCRIPTION"))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "PRICE"))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "STOCK QTY."))
        item = self.tableWidget_ALL_ITEMS.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "TYPE"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "NAME"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "DESCRIPTION"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "PRICE"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "STOCK QTY."))
        item = self.tableWidget_ROOF.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(6)
        item.setText(_translate("OWNER", "LENGTH"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(7)
        item.setText(_translate("OWNER", "WIDTH"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(8)
        item.setText(_translate("OWNER", "COLOR "))
        item = self.tableWidget_ROOF.horizontalHeaderItem(9)
        item.setText(_translate("OWNER", "WEIGHT"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(10)
        item.setText(_translate("OWNER", "THICKNESS"))
        item = self.tableWidget_ROOF.horizontalHeaderItem(11)
        item.setText(_translate("OWNER", "ROOF TYPE"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "NAME"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "DESCRIPTION"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "PRICE"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "STOCK QTY."))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(6)
        item.setText(_translate("OWNER", "LENGTH"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(7)
        item.setText(_translate("OWNER", "WIDTH"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(8)
        item.setText(_translate("OWNER", "COLOR "))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(9)
        item.setText(_translate("OWNER", "WEIGHT"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(10)
        item.setText(_translate("OWNER", "THICKNESS"))
        item = self.tableWidget_SPANDREL.horizontalHeaderItem(11)
        item.setText(_translate("OWNER", "SPANDREL TYPE"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "NAME"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "DESCRIPTION"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "PRICE"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "STOCK QTY"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(6)
        item.setText(_translate("OWNER", "LENGTH"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(7)
        item.setText(_translate("OWNER", "WIDTH"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(8)
        item.setText(_translate("OWNER", "COLOR "))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(9)
        item.setText(_translate("OWNER", "WEIGHT"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(10)
        item.setText(_translate("OWNER", "THICKNESS"))
        item = self.tableWidget_GUTTER.horizontalHeaderItem(11)
        item.setText(_translate("OWNER", "GUTTER TYPE"))
        self.addStocklabel.setText(_translate("OWNER", "ADD STOCK"))
        self.label_22.setText(_translate("OWNER", "SELECT A PRODUCT TYPE TO ADD FIRST"))
        self.pushButton_Confirm_ROOFadd.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_ROOFadd.setText(_translate("OWNER", "CLOSE"))
        self.label_23.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_24.setText(_translate("OWNER", "NAME            :"))
        self.label_25.setText(_translate("OWNER", "DESC.           :"))
        self.label_32.setText(_translate("OWNER", "TYPE              :"))
        self.lineEdit_AddROOF_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddROOF_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddROOF_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_AddROOF_Type.setItemText(0, _translate("OWNER", "Select Roof Type"))
        self.comboBox_AddROOF_Type.setItemText(1, _translate("OWNER", "Ribstar (Roof Type)"))
        self.comboBox_AddROOF_Type.setItemText(2, _translate("OWNER", "TileStar (Roof Type)"))
        self.comboBox_AddROOF_Type.setItemText(3, _translate("OWNER", "Corrugated (Roof Type)"))
        self.comboBox_AddROOF_Type.setItemText(4, _translate("OWNER", "Ridge Roll (Roof Bended Material)"))
        self.comboBox_AddROOF_Type.setItemText(5, _translate("OWNER", "Metal Fascia (Roof Bended Material)"))
        self.comboBox_AddROOF_Type.setItemText(6, _translate("OWNER", "Molding (Roof Bended Material)"))
        self.comboBox_AddROOF_Type.setItemText(7, _translate("OWNER", "Capping (Roof Bended Material)"))
        self.label_105.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_AddROOF_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_107.setText(_translate("OWNER", "WEIGHT                       :"))
        self.label_31.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_AddROOF_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_30.setText(_translate("OWNER", "WIDTH                         :"))
        self.lineEdit_AddROOF_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.label_29.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_AddROOF_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_27.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_AddROOF_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddROOF_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.label_117.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.lineEdit_AddROOF_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.pushButton_Confirm_SPANDRELadd.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_SPANDRELadd.setText(_translate("OWNER", "CLOSE"))
        self.label_26.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_28.setText(_translate("OWNER", "NAME            :"))
        self.label_108.setText(_translate("OWNER", "DESC.           :"))
        self.label_109.setText(_translate("OWNER", "TYPE              :"))
        self.lineEdit_AddSPANDREL_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddSPANDREL_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddSPANDREL_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.label_110.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_AddSPANDREL_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_112.setText(_translate("OWNER", "WEIGHT                       :"))
        self.lineEdit_AddSPANDREL_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.label_113.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_AddSPANDREL_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_115.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_AddSPANDREL_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_116.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_AddSPANDREL_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddSPANDREL_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_AddSPANDREL_Type.setItemText(0, _translate("OWNER", "Select Spandrel Type"))
        self.comboBox_AddSPANDREL_Type.setItemText(1, _translate("OWNER", "V Cut (Spandrel Type)"))
        self.comboBox_AddSPANDREL_Type.setItemText(2, _translate("OWNER", "Ceiling (Spandrel Type)"))
        self.label_118.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.lineEdit_AddSPANDREL_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.label_119.setText(_translate("OWNER", "WIDTH                         :"))
        self.pushButton_Confirm_GUTTERadd.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_GUTTERadd.setText(_translate("OWNER", "CLOSE"))
        self.label_33.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_34.setText(_translate("OWNER", "NAME            :"))
        self.label_129.setText(_translate("OWNER", "DESC.           :"))
        self.lineEdit_AddGUTTER_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddGUTTER_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddGUTTER_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.label_131.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_AddGUTTER_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_133.setText(_translate("OWNER", "WEIGHT                       :"))
        self.lineEdit_AddGUTTER_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.label_134.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_AddGUTTER_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_136.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_AddGUTTER_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_137.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_AddGUTTER_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_AddGUTTER_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_AddGUTTER_Type.setItemText(0, _translate("OWNER", "Select Gutter Type"))
        self.comboBox_AddGUTTER_Type.setItemText(1, _translate("OWNER", "Spanish Gutter (Gutter Type)"))
        self.comboBox_AddGUTTER_Type.setItemText(2, _translate("OWNER", "Box Gutter (Gutter Type)"))
        self.comboBox_AddGUTTER_Type.setItemText(3, _translate("OWNER", "Modified Gutter (Gutter Type)"))
        self.comboBox_AddGUTTER_Type.setItemText(4, _translate("OWNER", "JB Gutter (Gutter Type)"))
        self.comboBox_AddGUTTER_Type.setItemText(5, _translate("OWNER", "IV Gutter (Gutter Type)"))
        self.comboBox_AddGUTTER_Type.setItemText(6, _translate("OWNER", "Flashing Gutter (Gutter Bended Material)"))
        self.comboBox_AddGUTTER_Type.setItemText(7, _translate("OWNER", "Valley Gutter / Cover (Gutter Bended Material)"))
        self.comboBox_AddGUTTER_Type.setItemText(8, _translate("OWNER", "Wall Flashing (Gutter Bended Material)"))
        self.comboBox_AddGUTTER_Type.setItemText(9, _translate("OWNER", "End Flashing (Gutter Bended Material)"))
        self.comboBox_AddGUTTER_Type.setItemText(10, _translate("OWNER", "L-Flashings (Gutter Bended Material)"))
        self.label_159.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.label_160.setText(_translate("OWNER", "WIDTH                         :"))
        self.lineEdit_AddGUTTER_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.label_132.setText(_translate("OWNER", "TYPE              :"))
        self.comboBox_Select_Prod_Type_toAdd.setItemText(0, _translate("OWNER", "Select Product Type"))
        self.comboBox_Select_Prod_Type_toAdd.setItemText(1, _translate("OWNER", "ROOF"))
        self.comboBox_Select_Prod_Type_toAdd.setItemText(2, _translate("OWNER", "SPANDREL"))
        self.comboBox_Select_Prod_Type_toAdd.setItemText(3, _translate("OWNER", "GUTTER"))
        self.editStocklabel.setText(_translate("OWNER", "EDIT STOCK"))
        self.label_54.setText(_translate("OWNER", "SELECT A PRODUCT TYPE TO EDIT FIRST"))
        self.pushButton_Save_ROOFedit.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_Discard_ROOFedit.setText(_translate("OWNER", "DISCARD CHANGES"))
        self.label_35.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_36.setText(_translate("OWNER", "NAME            :"))
        self.label_37.setText(_translate("OWNER", "DESC.           :"))
        self.label_38.setText(_translate("OWNER", "TYPE              :"))
        self.lineEdit_EditROOF_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditROOF_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditROOF_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_EditROOF_Type.setItemText(0, _translate("OWNER", "Select Roof Type"))
        self.comboBox_EditROOF_Type.setItemText(1, _translate("OWNER", "Ribstar (Roof Type)"))
        self.comboBox_EditROOF_Type.setItemText(2, _translate("OWNER", "TileStar (Roof Type)"))
        self.comboBox_EditROOF_Type.setItemText(3, _translate("OWNER", "Corrugated (Roof Type)"))
        self.comboBox_EditROOF_Type.setItemText(4, _translate("OWNER", "Ridge Roll (Roof Bended Material)"))
        self.comboBox_EditROOF_Type.setItemText(5, _translate("OWNER", "Metal Fascia (Roof Bended Material)"))
        self.comboBox_EditROOF_Type.setItemText(6, _translate("OWNER", "Molding (Roof Bended Material)"))
        self.comboBox_EditROOF_Type.setItemText(7, _translate("OWNER", "Capping (Roof Bended Material)"))
        self.label_138.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_EditROOF_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_140.setText(_translate("OWNER", "WEIGHT                       :"))
        self.lineEdit_EditROOF_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.label_39.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_EditROOF_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_40.setText(_translate("OWNER", "WIDTH                         :"))
        self.label_41.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_EditROOF_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_42.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_EditROOF_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditROOF_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.label_156.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.lineEdit_EditROOF_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.pushButton_Save_SPANDRELedit.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_Discard_SPANDRELedit.setText(_translate("OWNER", "DISCARD CHANGES"))
        self.label_43.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_44.setText(_translate("OWNER", "NAME            :"))
        self.label_141.setText(_translate("OWNER", "DESC.           :"))
        self.label_142.setText(_translate("OWNER", "TYPE              :"))
        self.lineEdit_EditSPANDREL_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditSPANDREL_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditSPANDREL_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.label_143.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_EditSPANDREL_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_144.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.label_145.setText(_translate("OWNER", "WEIGHT                       :"))
        self.lineEdit_EditSPANDREL_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.label_146.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_EditSPANDREL_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_148.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_EditSPANDREL_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_149.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_EditSPANDREL_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditSPANDREL_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_EditSPANDREL_Type.setItemText(0, _translate("OWNER", "Select Spandrel Type"))
        self.comboBox_EditSPANDREL_Type.setItemText(1, _translate("OWNER", "V Cut (Spandrel Type)"))
        self.comboBox_EditSPANDREL_Type.setItemText(2, _translate("OWNER", "Ceiling (Spandrel Type)"))
        self.label_162.setText(_translate("OWNER", "WIDTH                         :"))
        self.lineEdit_EditSPANDREL_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.pushButton_Save_GUTTERedit.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_Discard_GUTTERedit.setText(_translate("OWNER", "DISCARD CHANGES"))
        self.label_45.setText(_translate("OWNER", "PRODUCT CODE            :"))
        self.label_46.setText(_translate("OWNER", "NAME            :"))
        self.label_150.setText(_translate("OWNER", "DESC.           :"))
        self.label_151.setText(_translate("OWNER", "TYPE              :"))
        self.lineEdit_EditGUTTER_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditGUTTER_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditGUTTER_Weight.setPlaceholderText(_translate("OWNER", "....."))
        self.label_152.setText(_translate("OWNER", "STK. QTY.                    :"))
        self.lineEdit_EditGUTTER_Qty.setPlaceholderText(_translate("OWNER", "....."))
        self.label_153.setText(_translate("OWNER", "THICKNESS (MM)     :"))
        self.label_154.setText(_translate("OWNER", "WEIGHT                       :"))
        self.lineEdit_EditGUTTER_Thickness.setPlaceholderText(_translate("OWNER", "....."))
        self.label_155.setText(_translate("OWNER", "COLOR                        :"))
        self.lineEdit_EditGUTTER_Color.setPlaceholderText(_translate("OWNER", "....."))
        self.label_157.setText(_translate("OWNER", "LENGTH                       :"))
        self.lineEdit_EditGUTTER_Length.setPlaceholderText(_translate("OWNER", "....."))
        self.label_158.setText(_translate("OWNER", "PRICE           :"))
        self.lineEdit_EditGUTTER_Price.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_EditGUTTER_Desc.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_EditGUTTER_Type.setItemText(0, _translate("OWNER", "Select Gutter Type"))
        self.comboBox_EditGUTTER_Type.setItemText(1, _translate("OWNER", "Spanish Gutter (Gutter Type)"))
        self.comboBox_EditGUTTER_Type.setItemText(2, _translate("OWNER", "Box Gutter (Gutter Type)"))
        self.comboBox_EditGUTTER_Type.setItemText(3, _translate("OWNER", "Modified Gutter (Gutter Type)"))
        self.comboBox_EditGUTTER_Type.setItemText(4, _translate("OWNER", "JB Gutter (Gutter Type)"))
        self.comboBox_EditGUTTER_Type.setItemText(5, _translate("OWNER", "IV Gutter (Gutter Type)"))
        self.comboBox_EditGUTTER_Type.setItemText(6, _translate("OWNER", "Flashing Gutter (Gutter Bended Material)"))
        self.comboBox_EditGUTTER_Type.setItemText(7, _translate("OWNER", "Valley Gutter / Cover (Gutter Bended Material)"))
        self.comboBox_EditGUTTER_Type.setItemText(8, _translate("OWNER", "Wall Flashing (Gutter Bended Material)"))
        self.comboBox_EditGUTTER_Type.setItemText(9, _translate("OWNER", "End Flashing (Gutter Bended Material)"))
        self.comboBox_EditGUTTER_Type.setItemText(10, _translate("OWNER", "L-Flashings (Gutter Bended Material)"))
        self.label_161.setText(_translate("OWNER", "WIDTH                         :"))
        self.lineEdit_EditGUTTER_Width.setPlaceholderText(_translate("OWNER", "....."))
        self.comboBox_Select_Prod_Type_toEdit.setItemText(0, _translate("OWNER", "Select Product Type"))
        self.comboBox_Select_Prod_Type_toEdit.setItemText(1, _translate("OWNER", "ROOF"))
        self.comboBox_Select_Prod_Type_toEdit.setItemText(2, _translate("OWNER", "SPANDREL"))
        self.comboBox_Select_Prod_Type_toEdit.setItemText(3, _translate("OWNER", "GUTTER"))
        self.deleteStocklabel.setText(_translate("OWNER", "DELETE STOCK"))
        self.label_90.setText(_translate("OWNER", "SELECT A PRODUCT TYPE TO DELETE FIRST"))
        self.pushButton_Confirm_ROOFdelete.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_ROOFdelete.setText(_translate("OWNER", "CLOSE"))
        self.label_97.setText(_translate("OWNER", "PRODUCT CODE           :"))
        self.lineEdit_DeleteROOF_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.label_114.setText(_translate("OWNER", "NAME                              :"))
        self.label_120.setText(_translate("OWNER", "TYPE                                :"))
        self.lineEdit_28.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_DeleteROOF_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.label_48.setText(_translate("OWNER", "WARNING! This action cannot be undone."))
        self.comboBox_DeleteROOF_Type.setItemText(0, _translate("OWNER", "Select Roof Type"))
        self.comboBox_DeleteROOF_Type.setItemText(1, _translate("OWNER", "Ribstar (Roof Type)"))
        self.comboBox_DeleteROOF_Type.setItemText(2, _translate("OWNER", "TileStar (Roof Type)"))
        self.comboBox_DeleteROOF_Type.setItemText(3, _translate("OWNER", "Corrugated (Roof Type)"))
        self.comboBox_DeleteROOF_Type.setItemText(4, _translate("OWNER", "Ridge Roll (Roof Bended Material)"))
        self.comboBox_DeleteROOF_Type.setItemText(5, _translate("OWNER", "Metal Fascia (Roof Bended Material"))
        self.comboBox_DeleteROOF_Type.setItemText(6, _translate("OWNER", "Molding (Roof Bended Material)"))
        self.comboBox_DeleteROOF_Type.setItemText(7, _translate("OWNER", "Capping (Roof Bended Material)"))
        self.pushButton_Confirm_SPANDRELdelete.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_SPANDRELdelete.setText(_translate("OWNER", "CLOSE"))
        self.label_93.setText(_translate("OWNER", "PRODUCT CODE           :"))
        self.lineEdit_DeleteSPANDREL_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.label_94.setText(_translate("OWNER", "NAME                              :"))
        self.label_102.setText(_translate("OWNER", "TYPE                                :"))
        self.lineEdit_25.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_DeleteSPANDREL_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.label_20.setText(_translate("OWNER", "WARNING! This action cannot be undone."))
        self.comboBox_DeleteSPANDREL_Type.setItemText(0, _translate("OWNER", "Select Spandrel Type"))
        self.comboBox_DeleteSPANDREL_Type.setItemText(1, _translate("OWNER", "V Cut (Spandrel Type)"))
        self.comboBox_DeleteSPANDREL_Type.setItemText(2, _translate("OWNER", "Ceiling (Spandrel Type)"))
        self.pushButton_Confirm_GUTTERdelete.setText(_translate("OWNER", "CONFIRM"))
        self.pushButton_Close_GUTTERdelete.setText(_translate("OWNER", "CLOSE"))
        self.label_96.setText(_translate("OWNER", "PRODUCT CODE           :"))
        self.lineEdit_DeleteGUTTER_prodCode.setPlaceholderText(_translate("OWNER", "....."))
        self.label_106.setText(_translate("OWNER", "NAME                              :"))
        self.label_111.setText(_translate("OWNER", "TYPE                                :"))
        self.lineEdit_27.setPlaceholderText(_translate("OWNER", "....."))
        self.lineEdit_DeleteGUTTER_Name.setPlaceholderText(_translate("OWNER", "....."))
        self.label_47.setText(_translate("OWNER", "WARNING! This action cannot be undone."))
        self.comboBox_DeleteGUTTER_Type.setItemText(0, _translate("OWNER", "Select Gutter Type"))
        self.comboBox_DeleteGUTTER_Type.setItemText(1, _translate("OWNER", "Spanish Gutter (Gutter Type)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(2, _translate("OWNER", "Box Gutter (Gutter Type)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(3, _translate("OWNER", "Modified Gutter (Gutter Type)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(4, _translate("OWNER", "JB Gutter (Gutter Type)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(5, _translate("OWNER", "IV Gutter (Gutter Type)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(6, _translate("OWNER", "Flashing Gutter (Gutter Bended Material)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(7, _translate("OWNER", "Valley Gutter / Cover (Gutter Bended Material)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(8, _translate("OWNER", "Wall Flashing (Gutter Bended Material)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(9, _translate("OWNER", "End Flashing (Gutter Bended Material)"))
        self.comboBox_DeleteGUTTER_Type.setItemText(10, _translate("OWNER", "L-Flashings (Gutter Bended Material)"))
        self.comboBox_Select_Prod_Type_toDelete.setItemText(0, _translate("OWNER", "Select Product Type"))
        self.comboBox_Select_Prod_Type_toDelete.setItemText(1, _translate("OWNER", "ROOF"))
        self.comboBox_Select_Prod_Type_toDelete.setItemText(2, _translate("OWNER", "SPANDREL"))
        self.comboBox_Select_Prod_Type_toDelete.setItemText(3, _translate("OWNER", "GUTTER"))
        self.label_5.setText(_translate("OWNER", "ORDERS"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "ORDER ID"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "DATE"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "CUSTOMER NAME"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "PRICE"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(6)
        item.setText(_translate("OWNER", "QUANTITY"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(7)
        item.setText(_translate("OWNER", "BULK DISCOUNT"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(8)
        item.setText(_translate("OWNER", "SERVICE ID"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(9)
        item.setText(_translate("OWNER", "TOTAL AMOUNT"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(10)
        item.setText(_translate("OWNER", "CUSTOMER ADDRESS"))
        item = self.tableWidget_ORDERS.horizontalHeaderItem(11)
        item.setText(_translate("OWNER", "CUSTOMER CONTACT"))
        self.comboBox_SortORDERS_high_low.setItemText(0, _translate("OWNER", "                        Sort Orders By"))
        self.comboBox_SortORDERS_high_low.setItemText(1, _translate("OWNER", "  TOTAL AMOUNT (HIGHEST TO LOWEST)"))
        self.comboBox_SortORDERS_high_low.setItemText(2, _translate("OWNER", "  TOTAL AMOUNT (LOWEST TO HIGHEST)"))
        self.comboBox_SR_all_items.setItemText(0, _translate("OWNER", "  Generate Sales Report for All Items"))
        self.comboBox_SR_all_items.setItemText(1, _translate("OWNER", "  DAILY"))
        self.comboBox_SR_all_items.setItemText(2, _translate("OWNER", "  WEEKLY"))
        self.comboBox_SR_all_items.setItemText(3, _translate("OWNER", "  MONTHLY"))
        self.comboBox_SR_prodType.setItemText(0, _translate("OWNER", "  Generate Sales Report for Product Type"))
        self.comboBox_SR_prodType.setItemText(1, _translate("OWNER", "  ROOF"))
        self.comboBox_SR_prodType.setItemText(2, _translate("OWNER", "  SPANDREL"))
        self.comboBox_SR_prodType.setItemText(3, _translate("OWNER", "  GUTTER"))
        self.label_55.setText(_translate("OWNER", "CHOOSE A FILTER TO DISPLAY SALES REPORT"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "DATE"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TOTAL ITEM"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        item = self.tableWidget_SR_DAILY.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "DISCOUNT APPLIED"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "DATE"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TOTAL ITEM"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        item = self.tableWidget_SR_WEEKLY.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "DISCOUNT APPLIED"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "DATE"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TOTAL ITEM"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        item = self.tableWidget_SR_MONTHLY.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "DISCOUNT APPLIED"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "QTY. SOLD"))
        item = self.tableWidget_SR_ROOF.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "QTY. SOLD"))
        item = self.tableWidget_SR_SPANDREL.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(0)
        item.setText(_translate("OWNER", "RECEIPT ID"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(1)
        item.setText(_translate("OWNER", "PRODUCT CODE"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(2)
        item.setText(_translate("OWNER", "PRODUCT TYPE"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(3)
        item.setText(_translate("OWNER", "TIME"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(4)
        item.setText(_translate("OWNER", "QTY. SOLD"))
        item = self.tableWidget_SR_GUTTER.horizontalHeaderItem(5)
        item.setText(_translate("OWNER", "TOTAL AMOUNT (₱)"))
        self.SALES_label.setText(_translate("OWNER", "SALES"))
        self.pushButton_EditAccount.setText(_translate("OWNER", "Edit My Account"))
        self.label_getUSERNAME.setText(_translate("OWNER", "username"))
        self.pushButton_ChangePassword.setText(_translate("OWNER", "Change Password"))
        self.label_2.setText(_translate("OWNER", "Account ID                    :"))
        self.label_18.setText(_translate("OWNER", "Account Role               :"))
        self.label_19.setText(_translate("OWNER", "First Name                    :"))
        self.label_49.setText(_translate("OWNER", "Last Name                    :"))
        self.label_50.setText(_translate("OWNER", "Middle Initial                :"))
        self.label_51.setText(_translate("OWNER", "Date of Birth                 :"))
        self.label_52.setText(_translate("OWNER", "Gender                          :"))
        self.label_53.setText(_translate("OWNER", "Home Address           :"))
        self.label_56.setText(_translate("OWNER", "Contact Number       :"))
        self.label_storeAccount_ID.setText(_translate("OWNER", ".................................."))
        self.label_storeAccount_Role.setText(_translate("OWNER", ".........................."))
        self.label_storeFirst_Name.setText(_translate("OWNER", "..............................................."))
        self.label_storeLast_Name.setText(_translate("OWNER", "..........................................."))
        self.label_storeMiddle_Initial.setText(_translate("OWNER", "..."))
        self.label_storeDate_of_Birth.setText(_translate("OWNER", "...................."))
        self.label_storeGender.setText(_translate("OWNER", "................."))
        self.label_storeHome_Address.setText(_translate("OWNER", "................................................................"))
        self.label_storeContact_Num.setText(_translate("OWNER", "............................................"))
        self.lineEdit_editUSERNAME.setPlaceholderText(_translate("OWNER", "change username"))
        self.label_59.setText(_translate("OWNER", "First Name                    :"))
        self.label_60.setText(_translate("OWNER", "Last Name                    :"))
        self.label_61.setText(_translate("OWNER", "Middle Initial                :"))
        self.label_62.setText(_translate("OWNER", "Date of Birth                 :"))
        self.label_63.setText(_translate("OWNER", "Gender                          :"))
        self.label_64.setText(_translate("OWNER", "Home Address           :"))
        self.label_65.setText(_translate("OWNER", "Contact Number       :"))
        self.lineEdit_editFname.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editLname.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editMidInitial.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editDOB.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editGender.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editHomeAddress.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editContactNum.setPlaceholderText(_translate("OWNER", "..."))
        self.pushButton_saveEditaccount.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_cancelEditaccount.setText(_translate("OWNER", "CANCEL"))
        self.label_68.setText(_translate("OWNER", "Password                    "))
        self.label_69.setText(_translate("OWNER", "New Password                    "))
        self.label_70.setText(_translate("OWNER", "Confirm New Password                    "))
        self.lineEdit_enterpass.setPlaceholderText(_translate("OWNER", "enter password"))
        self.lineEdit_enterNEWpass.setPlaceholderText(_translate("OWNER", "enter new password"))
        self.lineEdit_confirmNEWpass.setPlaceholderText(_translate("OWNER", "confirm new password"))
        self.pushButton_saveNEWpassword.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_cancelNEWpassword.setText(_translate("OWNER", "CANCEL"))
        self.pushButton_EditAccount_cashier.setText(_translate("OWNER", "Edit Cashier Account"))
        self.label_getUSERNAME_cashier.setText(_translate("OWNER", "username"))
        self.pushButton_ChangePassword_cashier.setText(_translate("OWNER", "Change Cashier Password"))
        self.label_3.setText(_translate("OWNER", "Account ID                    :"))
        self.label_66.setText(_translate("OWNER", "Account Role               :"))
        self.label_67.setText(_translate("OWNER", "First Name                    :"))
        self.label_71.setText(_translate("OWNER", "Last Name                    :"))
        self.label_72.setText(_translate("OWNER", "Middle Initial                :"))
        self.label_73.setText(_translate("OWNER", "Date of Birth                 :"))
        self.label_74.setText(_translate("OWNER", "Gender                          :"))
        self.label_75.setText(_translate("OWNER", "Home Address           :"))
        self.label_76.setText(_translate("OWNER", "Contact Number       :"))
        self.label_storeAccount_ID_cashier.setText(_translate("OWNER", ".................................."))
        self.label_storeAccount_Role_cashier.setText(_translate("OWNER", ".........................."))
        self.label_storeFirst_Name_cashier.setText(_translate("OWNER", "..............................................."))
        self.label_storeLast_Name_cashier.setText(_translate("OWNER", "..........................................."))
        self.label_storeMiddle_Initial_cashier.setText(_translate("OWNER", "..."))
        self.label_storeDate_of_Birth_cashier.setText(_translate("OWNER", "...................."))
        self.label_storeGender_cashier.setText(_translate("OWNER", "................."))
        self.label_storeHome_Address_cashier.setText(_translate("OWNER", "................................................................"))
        self.label_storeContact_Num_cashier.setText(_translate("OWNER", "............................................"))
        self.label_79.setText(_translate("OWNER", "First Name                    :"))
        self.label_80.setText(_translate("OWNER", "Last Name                    :"))
        self.label_81.setText(_translate("OWNER", "Middle Initial                :"))
        self.label_82.setText(_translate("OWNER", "Date of Birth                 :"))
        self.label_83.setText(_translate("OWNER", "Gender                          :"))
        self.label_84.setText(_translate("OWNER", "Home Address           :"))
        self.label_85.setText(_translate("OWNER", "Contact Number       :"))
        self.lineEdit_editFname_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editLname_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editMidInitial_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editDOB_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editGender_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editHomeAddress_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editContactNum_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_editUSERNAME_cashier.setPlaceholderText(_translate("OWNER", "change username"))
        self.pushButton_saveEditaccount_cashier.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_cancelEditaccount_cashier.setText(_translate("OWNER", "CANCEL"))
        self.label_86.setText(_translate("OWNER", "Password                    "))
        self.label_87.setText(_translate("OWNER", "New Password                    "))
        self.label_92.setText(_translate("OWNER", "Confirm New Password                    "))
        self.lineEdit_enterpass_cashier.setPlaceholderText(_translate("OWNER", "enter password"))
        self.lineEdit_enterNEWpass_cashier.setPlaceholderText(_translate("OWNER", "enter new password"))
        self.lineEdit_confirmNEWpass_cashier.setPlaceholderText(_translate("OWNER", "confirm new password"))
        self.pushButton_saveNEWpassword_cashier.setText(_translate("OWNER", "SAVE CHANGES"))
        self.pushButton_cancelNEWpassword_cashier.setText(_translate("OWNER", "CANCEL"))
        self.lineEdit_createUSERNAME_cashier.setPlaceholderText(_translate("OWNER", "create username"))
        self.label_100.setText(_translate("OWNER", "First Name                    :"))
        self.label_101.setText(_translate("OWNER", "Last Name                    :"))
        self.label_103.setText(_translate("OWNER", "Middle Initial                :"))
        self.label_104.setText(_translate("OWNER", "Date of Birth                 :"))
        self.label_121.setText(_translate("OWNER", "Gender                          :"))
        self.label_122.setText(_translate("OWNER", "Home Address           :"))
        self.label_123.setText(_translate("OWNER", "Contact Number       :"))
        self.lineEdit__createFname_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit__createLname_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit__createMidInitial_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit__createDOB_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit__createGender_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit__createHomeAddress_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.lineEdit_createContactNum_cashier.setPlaceholderText(_translate("OWNER", "..."))
        self.pushButton_CreateAccount_cashier.setText(_translate("OWNER", "CREATE ACCOUNT"))
        self.pushButton_cancelCreateAccount_cashier.setText(_translate("OWNER", "CANCEL"))
        self.pushButton_VIEW.setText(_translate("OWNER", "VIEW MY ACCOUNT"))
        self.pushButton_VIEW_C.setText(_translate("OWNER", "VIEW CASHIER ACCOUNT"))
        self.pushButton_CREATE_C.setText(_translate("OWNER", "CREATE NEW CASHIER ACCOUNT"))
        self.label.setText(_translate("OWNER", "                                                                           J  &  J  ROOFSTEEL  AND  GUTTER  SUPPLY  (MOALBOAL BRANCH)     "))
        self.dateLabel_inAccount.setText(_translate("OWNER", "<html><head/><body><p align=\"right\"><span style=\" font-size:48pt;\">March 31, 2025 </span><span style=\" font-size:48pt; color:#ffffff;\">.</span></p><p align=\"center\"><span style=\" font-size:20pt;\">Monday</span><span style=\" font-size:16pt; color:#ffffff;\">....................................</span></p></body></html>"))
        self.timeLabel_inAccount.setText(_translate("OWNER", " 09 : 10 : 54 AM"))
import resources.jj_owner_resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OWNER = QtWidgets.QMainWindow()
    ui = Ui_OWNER()
    ui.setupUi(OWNER)
    OWNER.show()
    sys.exit(app.exec_())