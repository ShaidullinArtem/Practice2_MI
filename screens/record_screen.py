import sys
from datetime import datetime
from typing import List

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QStackedWidget

from database import Database
from models import ServiceModel, ClientServiceModel
from models.service import ServiceToClientService
from screens.catalog_screen import CatalogScreen
from ui.records_ui import Ui_Records_MainWindow
from ui.widgets import records_widget


class RecordScreen(QMainWindow):
    def __init__(self):
        super(RecordScreen, self).__init__()
        self.ui = Ui_Records_MainWindow()
        self.ui.setupUi(self)
        self.ui.scrollArea.horizontalScrollBar().setEnabled(False)
        self.setWindowTitle(f'Каталог | Ближайшие записи')

        self.service_db = Database(
            table_name='Service',
            model=ServiceModel
        )

        self.client_service_db = Database(
            table_name='ClientService',
            model=ClientServiceModel
        )

        self.records: List[ClientServiceModel] = self.client_service_db.get_all_records(datetime(2019, 4, 27), datetime(2019, 9, 10))
        self.service_cards: List[ServiceToClientService] = []

        for record in self.records:
            service: List[ServiceModel] | None = self.service_db.get_by_query(f'ID = {record.service_id}')
            if service:
                self.service_cards.append(
                    ServiceToClientService(
                        service=service[0],
                        record=record
                    )
                )

        card_layout = QVBoxLayout(self)
        self.Stack = QStackedWidget()
        self.cards_widget = records_widget.Records(record_list=self.service_cards)
        self.Stack.addWidget(self.cards_widget)

        card_layout.addWidget(self.Stack)

        self.ui.recored_scroll_container.setLayout(card_layout)

        self.ui.nav_to_catalog_button.clicked.connect(self.on_nav_to_catalog_button_click)
        self.show()

    def on_nav_to_catalog_button_click(self):
        self.catalog_screen = CatalogScreen()
        self.catalog_screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RecordScreen()
    sys.exit(app.exec_())
