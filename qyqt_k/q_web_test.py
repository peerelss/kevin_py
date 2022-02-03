import sys

# 使用调色板等
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
# 导入QT,其中包含一些常量，例如颜色等
# 导入常用组件
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt5.QtWidgets import QMdiArea, QMdiSubWindow
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class DemoWin(QMainWindow):
    count = 0

    def __init__(self):
        super(DemoWin, self).__init__()
        self.initUI()

    def initUI(self):
        # 将窗口设置为动图大小
        self.resize(1000, 800)
        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://www.rubber-passion.com/MembersArea/category/updates/photo-galleries/'))
        self.setCentralWidget(self.browser)

        # 添加窗口标题
        self.setWindowTitle("WebEngineDemo")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("images/icon.ico"))
    # 创建一个主窗口
    mainWin = DemoWin()
    # 显示
    mainWin.show()
    # 主循环
    sys.exit(app.exec_())