from typing import List

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLineEdit, QListWidget, QLabel

from models import ServiceModel
from ui.card_ui import Ui_Card


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
        self.price_filter_listWidget = QListWidget(self.price_filter_farme)
        self.price_filter_listWidget.setObjectName(u"price_filter_listWidget")
        self.price_filter_listWidget.setMaximumSize(QSize(150, 16777215))
        self.price_filter_listWidget.setStyleSheet(u"QListWidget {\n"
                                                   "	border: 1px solid #53555e;\n"
                                                   "	border-radius: 5px;\n"
                                                   "	padding: 5px;\n"
                                                   "	background: white;\n"
                                                   "}\n"
                                                   "\n"
                                                   "QListWidget:focus {\n"
                                                   "	outline: none;\n"
                                                   "    border: 2px solid #673ae7;\n"
                                                   "}")

        self.horizontalLayout_2.addWidget(self.price_filter_listWidget)

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
        self.discount_filter_listWidget = QListWidget(self.discount_filter_farme)
        self.discount_filter_listWidget.setObjectName(u"discount_filter_listWidget")
        self.discount_filter_listWidget.setMaximumSize(QSize(150, 16777215))
        self.discount_filter_listWidget.setStyleSheet(u"QListWidget {\n"
                                                      "	border: 1px solid #53555e;\n"
                                                      "	border-radius: 5px;\n"
                                                      "	padding: 5px;\n"
                                                      "	background: white;\n"
                                                      "}\n"
                                                      "\n"
                                                      "QListWidget:focus {\n"
                                                      "	outline: none;\n"
                                                      "    border: 2px solid #673ae7;\n"
                                                      "}")

        self.horizontalLayout_3.addWidget(self.discount_filter_listWidget)

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

        self.search_lineEdit.textChanged.connect(self.on_search_change)

        for service in self.card_list:
            card = Ui_Card(self.is_admin, service)
            self.cards_layout.addWidget(card)

    def on_search_change(self, state: str):
        for i in range(self.cards_layout.count()):
            item = self.cards_layout.itemAt(i).widget()
            if isinstance(item, Ui_Card):
                item.show() if state.lower() in item.title_label.text().lower() else item.hide()
