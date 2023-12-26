import decimal
from typing import List

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLineEdit, QLabel, QComboBox, QPushButton

from models import ServiceModel
from screens.record_screen import RecordScreen
from ui.card_ui import Ui_Card
from utlis.service_sort import services_price_sort


class Cards(QWidget):
    def __init__(self, *, card_list: List[ServiceModel], is_admin: bool, parent=None):
        QWidget.__init__(self, parent=parent)
        self.setObjectName(u'cards')
        self.card_list = card_list
        self.is_admin = is_admin

        self.cards_layout = QVBoxLayout(self)

        self.search = QFrame(self)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 40))
        self.search.setMaximumSize(QSize(700, 40))
        self.search.setFrameShape(QFrame.NoFrame)
        self.search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.search)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_lineEdit = QLineEdit(self.search)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
        self.search_lineEdit.setMinimumSize(QSize(300, 0))
        self.search_lineEdit.setMaximumSize(QSize(300, 16777215))
        self.search_lineEdit.setStyleSheet(u"QLineEdit {\n"
                                           "	padding: 10px 5px;\n"
                                           "	color: black;\n"
                                           "	font-size: 14px;\n"
                                           "	font-weight: bold;\n"
                                           "	border-radius: 5px;\n"
                                           "}\n"
                                           "\n"
                                           "QLineEdit:focus {\n"
                                           "	outline: none;\n"
                                           "    border: 2px solid #673ae7;\n"
                                           "}")

        self.horizontalLayout.addWidget(self.search_lineEdit)

        self.price_filter_farme = QFrame(self.search)
        self.price_filter_farme.setObjectName(u"price_filter_farme")
        self.price_filter_farme.setLayoutDirection(Qt.RightToLeft)
        self.price_filter_farme.setFrameShape(QFrame.NoFrame)
        self.price_filter_farme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.price_filter_farme)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.price_filter_comboBox = QComboBox(self.price_filter_farme)
        self.price_filter_comboBox.addItems([
            'Все',
            'По возрастнаию',
            'По убыванию'
        ])
        self.price_filter_comboBox.setObjectName(u"price_filter_listWidget")
        self.price_filter_comboBox.setMaximumSize(QSize(150, 16777215))
        self.price_filter_comboBox.setStyleSheet(u"QComboBox {\n"
                                                 "	border: 1px solid #53555e;\n"
                                                 "	border-radius: 5px;\n"
                                                 "	padding: 5px;\n"
                                                 "	background: white;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QComboBox:focus {\n"
                                                 "	outline: none;\n"
                                                 "    border: 2px solid #673ae7;\n"
                                                 "}")

        self.horizontalLayout_2.addWidget(self.price_filter_comboBox)

        self.price_filter_label = QLabel(self.price_filter_farme)
        self.price_filter_label.setObjectName(u"price_filter_label")
        self.price_filter_label.setStyleSheet(u"QLabel {\n"
                                              "	color:  #53555e;\n"
                                              "	font-size: 12px;\n"
                                              "	font-weight: 400;\n"
                                              "}\n"
                                              "")

        self.horizontalLayout_2.addWidget(self.price_filter_label)

        self.horizontalLayout.addWidget(self.price_filter_farme)

        self.discount_filter_farme = QFrame(self.search)
        self.discount_filter_farme.setObjectName(u"discount_filter_farme")
        self.discount_filter_farme.setLayoutDirection(Qt.RightToLeft)
        self.discount_filter_farme.setFrameShape(QFrame.NoFrame)
        self.discount_filter_farme.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.discount_filter_farme)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.discount_filter_comboBox = QComboBox(self.discount_filter_farme)
        self.discount_filter_comboBox.addItems([
            'Все',
            'от 0 % до 5 %',
            'от 5 % до 15 %',
            'от 15 % до 30 %',
            'от 30 % до 70 %',
            'от 70 % до 100 %',
        ])
        self.discount_filter_comboBox.setObjectName(u"discount_filter_listWidget")
        self.discount_filter_comboBox.setMaximumSize(QSize(150, 16777215))
        self.discount_filter_comboBox.setStyleSheet(u"QComboBox {\n"
                                                    "	border: 1px solid #53555e;\n"
                                                    "	border-radius: 5px;\n"
                                                    "	padding: 5px;\n"
                                                    "	background: white;\n"
                                                    "}\n"
                                                    "\n"
                                                    "QComboBox:focus {\n"
                                                    "	outline: none;\n"
                                                    "    border: 2px solid #673ae7;\n"
                                                    "}")

        self.horizontalLayout_3.addWidget(self.discount_filter_comboBox)

        self.discount_filter_label = QLabel(self.discount_filter_farme)
        self.discount_filter_label.setObjectName(u"discount_filter_label")
        self.discount_filter_label.setStyleSheet(u"QLabel {\n"
                                                 "	color:  #53555e;\n"
                                                 "	font-size: 12px;\n"
                                                 "	font-weight: 400;\n"
                                                 "}\n"
                                                 "")

        self.horizontalLayout_3.addWidget(self.discount_filter_label)

        self.horizontalLayout.addWidget(self.discount_filter_farme)

        self.cards_layout.addWidget(self.search)

        self.records = QFrame(self)
        self.records.setObjectName(u"records")
        self.records.setMinimumSize(QSize(0, 40))
        self.records.setMaximumSize(QSize(700, 40))
        self.records.setFrameShape(QFrame.NoFrame)
        self.records.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.records)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.nav_to_recored_button = QPushButton(self.records)
        self.nav_to_recored_button.setObjectName(u"nav_to_recored_button")
        self.nav_to_recored_button.setStyleSheet(u"QPushButton {\n"
                                                 "	padding: 10px 15px;\n"
                                                 "	background: #e1e4ff;\n"
                                                 "	color: black;\n"
                                                 "	font-size: 14px;\n"
                                                 "	font-weight: 500;\n"
                                                 "	border: none;\n"
                                                 "	border-radius: 5px;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "	color: white;\n"
                                                 "}")

        self.nav_to_recored_button.setText('Ближайшие записи')
        self.horizontalLayout_4.addWidget(self.nav_to_recored_button)
        self.cards_layout.addWidget(self.records)

        self.search_lineEdit.textChanged.connect(self.on_search_change)

        self.price_filter_comboBox.currentIndexChanged.connect(self.on_price_filter_change)
        self.discount_filter_comboBox.currentIndexChanged.connect(self.on_discount_filter_change)

        self.nav_to_recored_button.clicked.connect(self.on_nav_to_records_button_click)

        self.make_cards(self.card_list)

    def on_nav_to_records_button_click(self):
        self.records_screen = RecordScreen()
        self.records_screen.show()
        self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().close()

    def make_cards(self, cards: List[ServiceModel]):
        for i in reversed(range(self.cards_layout.count())):
            item = self.cards_layout.itemAt(i).widget()
            if isinstance(item, Ui_Card):
                item.setParent(None)

        for service in cards:
            card = Ui_Card(self.is_admin, service)
            self.cards_layout.addWidget(card)

    def on_search_change(self, state: str):
        for i in range(self.cards_layout.count()):
            item = self.cards_layout.itemAt(i).widget()
            if isinstance(item, Ui_Card):
                item.show() if state.lower() in item.title_label.text().lower() else item.hide()

    def on_price_filter_change(self):
        index = self.price_filter_comboBox.currentIndex()
        card_list_copy = self.card_list.copy()
        if index == 0:
            self.make_cards(self.card_list)
        else:
            sorted_card_list = services_price_sort(index == 1, card_list_copy)
            self.make_cards(sorted_card_list)

        self.on_search_change(self.search_lineEdit.text().strip())

    def on_discount_filter_change(self):
        text = self.discount_filter_comboBox.currentText()
        if text.lower().strip() == 'все':
            return self.make_cards(self.card_list)
        down, up = [int(floor) for floor in text.strip().split() if floor.isnumeric()]
        for i in range(self.cards_layout.count()):
            item = self.cards_layout.itemAt(i).widget()
            if isinstance(item, Ui_Card):
                discount = item.discount_label.text()[-3:].strip()[:-1]
                if discount.isnumeric():
                    item.show() if down <= int(discount) <= up else item.hide()
                elif discount == '' and down == 0:
                    item.show()
                else:
                    item.hide()




