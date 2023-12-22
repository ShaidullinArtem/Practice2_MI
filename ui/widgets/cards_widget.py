from typing import List

from PyQt5.QtWidgets import QWidget, QVBoxLayout

from models import ServiceModel
from ui.card_ui import Ui_Card


class Cards(QWidget):
    def __init__(self, *, card_list: List[ServiceModel], is_admin: bool, parent=None):
        QWidget.__init__(self, parent=parent)
        self.card_list = card_list
        self.is_admin = is_admin

        cards_layout = QVBoxLayout(self)
        for service in self.card_list:
            card = Ui_Card(self.is_admin, service)
            cards_layout.addWidget(card)
