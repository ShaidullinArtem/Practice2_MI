import datetime
from typing import List
import decimal

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from models.service import ServiceToClientService
from ui.card_ui import Ui_Card


class Records(QWidget):
    def __init__(self, *, record_list: List[ServiceToClientService], parent=None):
        QWidget.__init__(self, parent=parent)
        self.setObjectName(u'records')
        self.record_list = record_list

        self.records_layout = QVBoxLayout(self)
        self.make_records(self.record_list)
        # self.records_layout.addWidget(self.records)

    def make_records(self, cards: List[ServiceToClientService]):
        now_time = datetime.datetime(2019, 9, 10, 13, 40)
        for i in reversed(range(self.records_layout.count())):
            item = self.records_layout.itemAt(i).widget()
            if isinstance(item, Ui_Card):
                item.setParent(None)

        for records in cards:
            time_label = QLabel(str(records.record.start_time))
            description_label = QLabel(
                str(records.record.comment) if records.record.comment else ''
            )
            card = Ui_Card(True, records.service)
            self.records_layout.addWidget(time_label)
            self.records_layout.addWidget(card)
            self.records_layout.addWidget(description_label)
            if records.record.start_time.hour <= now_time.hour - 2:
                card.title_label.setStyleSheet("""QLabel {color: red; font-size: 20px;}""")
