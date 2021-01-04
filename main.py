from PyQt5 import QtWidgets
import sys
from UI.MainWindow import Ui_MainWindow

class UI(Ui_MainWindow):
    def populateTypeOfAlgo(self):
        pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UI()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
