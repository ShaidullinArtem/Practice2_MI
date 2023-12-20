import sys
from typing import List

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

from models import ServiceModel
from ui import Ui_MainWindow_Catalog


class Cards(QWidget):
    def __init__(self, *, card_list: List[ServiceModel], parent=None):
        QWidget.__init__(self, parent=parent)
        self.card_list = card_list

        lay = QVBoxLayout(self)
        for i in range(1):
            lay.addWidget(QPushButton("{}".format(i)))


class CatalogScreen(QMainWindow):
    def __init__(self, *, is_admin=False):
        super(CatalogScreen, self).__init__()
        self.ui = Ui_MainWindow_Catalog()
        self.ui.setupUi(self)

        self.is_admin = is_admin

        lay = QVBoxLayout(self)
        self.Stack = QStackedWidget()
        self.Stack.addWidget(Cards(card_list=[]))

        lay.addWidget(self.Stack)

        self.ui.container.setLayout(lay)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CatalogScreen()
    sys.exit(app.exec_())

