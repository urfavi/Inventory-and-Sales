from controllers.login_controller import Login
from gui_classes.ui_landing import Ui_JJ_LANDING  # Correct path
from gui_classes.ui_login import Ui_LOGIN  # Correct path for UI class
from controllers.login_controller import Login  # Adjust the import path as needed
from controllers.owner_controller import OwnerInterface  # Adjust the import path as needed
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QDate, QTimer, QTime, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class LandingPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_JJ_LANDING()
        self.ui.setupUi(self)
        
        self.ui.pushButton_cont_2Login.clicked.connect(self.open_login)

    def open_login(self):#Open login page and close current window
        self.owner_login = Login()
        self.owner_login.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LandingPage()  # import gikan sa controller
    window.show()
    sys.exit(app.exec_())
