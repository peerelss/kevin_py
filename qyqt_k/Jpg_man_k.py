import sys
import Jpg_manager
from PyQt5.QtWidgets import QApplication, QDialog
import requests
from bs4 import BeautifulSoup


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.ui = Jpg_manager.Ui_Dialog()
        self.ui.setupUi(self)

    def get_re_images(self):
        url_s = self.ui.lineEdit.text()
        r = requests.get(url_s)
        if r.status_code == 200:
            #self.ui.textEdit.setText(r.text)
            print("photo url :" + url_s)
            pic_soup = BeautifulSoup(requests.get(url_s).content, "lxml").find_all('img')
            str_s = ''
            for p in pic_soup:
                result_str = (str(p['src']).replace('small', 'xl'))
                str_s = str_s + '\n' + result_str
                self.ui.textEdit.setText(str_s)
                print(result_str)
                # f.write(result_str + '\n')


if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = MainWindow()
    myDlg.show()
    sys.exit(myapp.exec_())
