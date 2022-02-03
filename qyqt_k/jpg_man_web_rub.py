import sys
import Jpg_manager_web
from PyQt5.QtWidgets import QApplication, QDialog
import requests
from bs4 import BeautifulSoup


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Jpg_manager_web.Ui_Dialog()
        self.ui.setupUi(self)

    def load_url(self):
        url_s = self.ui.lineEdit.text()
        r = requests.get(url_s)
        self.ui.webView.load(url_s)


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainWindow()
    myDlg.show()
    sys.exit(myapp.exec_())
