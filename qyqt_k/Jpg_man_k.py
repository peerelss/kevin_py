import sys
import Jpg_manager
from PyQt5.QtWidgets import QApplication, QDialog
import requests


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Jpg_manager.Ui_Dialog()
        self.ui.setupUi(self)

    def get_re_images(self):
        url_s = self.ui.lineEdit.text()
        r = requests.get(url_s)
        if r.status_code == 200:
            self.ui.textEdit.setText(r.text)
        else:
            self.ui.textEdit.setText("error")


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainWindow()
    myDlg.show()
    sys.exit(myapp.exec_())
