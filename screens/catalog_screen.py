import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QStackedWidget

from database import Database
from models import ServiceModel
from ui import Ui_MainWindow_Catalog
from ui.widgets import Cards


class CatalogScreen(QMainWindow):
    def __init__(self, *, is_admin=False):
        super(CatalogScreen, self).__init__()
        self.ui = Ui_MainWindow_Catalog()
        self.ui.setupUi(self)
        self.ui.scrollArea.horizontalScrollBar().setEnabled(False)

        self.is_admin = is_admin
        self.setWindowTitle(f'Каталог | {"Покупатель" if not self.is_admin else "Администратор"}')

        self.service_db = Database(
            table_name='Service',
            model=ServiceModel
        )

        self.services = self.service_db.list()

        card_layout = QVBoxLayout(self)
        self.Stack = QStackedWidget()
        self.cards_widget = Cards(card_list=self.services, is_admin=is_admin)
        self.Stack.addWidget(self.cards_widget)

        card_layout.addWidget(self.Stack)

        self.ui.scroll_content.setLayout(card_layout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CatalogScreen()
    sys.exit(app.exec_())
