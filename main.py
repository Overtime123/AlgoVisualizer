from PyQt5 import QtWidgets
import sys
from UI.MainWindow import Ui_MainWindow

types = ["Searching", "Sorting", "Arrays", "String", "Graphs and Trees"]

class UI(Ui_MainWindow):
    def populateTypeOfAlgo(self):
        pass

    def populateAlgo(self):
        pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UI()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
