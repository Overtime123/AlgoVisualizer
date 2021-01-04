from PyQt5 import QtWidgets
import sys
from UI.MainWindow import Ui_MainWindow

types = ["Searching", "Sorting", "Arrays", "String", "Graphs and Trees"]

class UI(Ui_MainWindow):
    def populateTypeOfAlgo(self):
        pass

    def addItemToAlgoBox(self, items):
        self.AlgoBox.clear()
        items.sort()
        for item in items:
                self.AlgoBox.addItem(item)

    def populateAlgo(self, nameOfAlgo):
        if nameOfAlgo is "Searching":
            items = ["Linear Searching", "Binary Searching"]
            self.addItemToAlgoBox(items)

        if nameOfAlgo is "Sorting":
            items = ["Selection Sort", "Bubble Sort", "Merge Sort", "Quick Sort", "Heap Sort", "Insertion Sort"]
            self.addItemToAlgoBox(items)

        if nameOfAlgo is "Arrays":
            pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = UI()
ui.setupUi(MainWindow)
ui.populateAlgo("Searching")
MainWindow.show()
sys.exit(app.exec_())
