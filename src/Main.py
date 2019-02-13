# coding: utf-8
import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from Tasks.VagrantFile import VagrantFile

from View.Ui_MainWindow import Ui_MainWindow

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.myPushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        dialog = QFileDialog()
        DirectoryPath = dialog.getExistingDirectory(None, "Select Folder")
        result = VagrantFile(DirectoryPath).showInUse()
        self.textBrowser.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
