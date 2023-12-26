# -*- coding: utf-8 -*-
import datetime
import decimal

from PyQt5 import QtCore
################################################################################
## Form generated from reading UI file 'card_uiBlzuFN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from database import Database
from models import ServiceModel
from screens.edit_service_screen import EditServiceScreen


class Ui_Card(QWidget):
    def __init__(self, is_admin: bool, service: ServiceModel):
        QWidget.__init__(self)
        self.service = service
        self.is_admin = is_admin

        self.service_db = Database(table_name='Service', model=ServiceModel)

        self.resize(750, 200)
        self.setMinimumSize(QSize(750, 200))
        self.setMaximumSize(QSize(750, 200))
        self.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self)
        self.container.setObjectName(u"container")
        self.container.setStyleSheet(u"")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.image_wrapper = QFrame(self.container)
        self.image_wrapper.setObjectName(u"image_wrapper")
        self.image_wrapper.setMinimumSize(QSize(200, 0))
        self.image_wrapper.setMaximumSize(QSize(200, 16777215))
        self.image_wrapper.setStyleSheet(u"QFrame {\n"
                                         "	background: #eecdcd;\n"
                                         "	border: 1px solid #cbcbcb;\n"
                                         "	border-radius: 5px;\n"
                                         "}")
        self.image_wrapper.setFrameShape(QFrame.NoFrame)
        self.image_wrapper.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.image_wrapper)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.image = QLabel(self.image_wrapper)
        self.image.setObjectName(u"image")
        self.image.setScaledContents(True)
        self.pixmap = QPixmap(f'../media/service_images/{self.service.main_image_path}')

        self.verticalLayout.addWidget(self.image)

        self.horizontalLayout_2.addWidget(self.image_wrapper)

        self.content = QFrame(self.container)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_label = QLabel(self.content)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"QLabel {\n"
                                       "	color: #94a2ab;\n"
                                       "	font-size: 14px;\n"
                                       "	font-weight: 600;\n"
                                       "}")

        self.verticalLayout_2.addWidget(self.title_label)

        self.price_label = QLabel(self.content)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setStyleSheet(u"QLabel {\n"
                                       "	color: #94a2ab;\n"
                                       "	font-size: 13px;\n"
                                       "	font-weight: 500;\n"
                                       "}")

        self.verticalLayout_2.addWidget(self.price_label)

        self.discount_label = QLabel(self.content)
        self.discount_label.setObjectName(u"discount_label")
        self.discount_label.setStyleSheet(u"QLabel {\n"
                                          "	color: #94a2ab;\n"
                                          "	font-size: 12px;\n"
                                          "	font-weight: 500;\n"
                                          "}")

        self.verticalLayout_2.addWidget(self.discount_label)

        self.footer = QFrame(self.content)
        self.footer.setObjectName(u"footer")
        self.footer.setLayoutDirection(Qt.LeftToRight)
        self.footer.setStyleSheet(u"")
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(15)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 120, 0)

        self.join_to_service_button = QPushButton(self.footer)
        self.join_to_service_button.setObjectName(u"nav_to_edit_button")
        self.join_to_service_button.setMaximumSize(QSize(380, 16777215))
        self.join_to_service_button.setStyleSheet(u"QPushButton {\n"
                                                  "	border: 1.5px solid #94a2ab;\n"
                                                  "	color: #94a2ab;\n"
                                                  "	padding: 5px 10px;\n"
                                                  "	font-size: 12px;\n"
                                                  "	font-weight: 600;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover {\n"
                                                  "	border: 1.5px solid #cdd6ee;\n"
                                                  "	color: #cdd6ee;\n"
                                                  "}")

        self.nav_to_edit_button = QPushButton(self.footer)
        self.nav_to_edit_button.setObjectName(u"nav_to_edit_button")
        self.nav_to_edit_button.setMaximumSize(QSize(250, 16777215))
        self.nav_to_edit_button.setStyleSheet(u"QPushButton {\n"
                                              "	border: 1.5px solid #94a2ab;\n"
                                              "	color: #94a2ab;\n"
                                              "	padding: 2px 5px;\n"
                                              "	font-size: 12px;\n"
                                              "	font-weight: 600;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "	border: 1.5px solid #cdd6ee;\n"
                                              "	color: #cdd6ee;\n"
                                              "}")

        self.horizontalLayout_3.addWidget(self.nav_to_edit_button if self.is_admin else self.join_to_service_button)

        self.remove_service_button = QPushButton(self.footer)
        self.remove_service_button.setObjectName(u"remove_service_button")
        self.remove_service_button.setMaximumSize(QSize(130, 16777215))
        self.remove_service_button.setStyleSheet(u"QPushButton {\n"
                                                 "	border: 1.5px solid #94a2ab;\n"
                                                 "	color: #94a2ab;\n"
                                                 "	padding: 2px 5px;\n"
                                                 "	font-size: 12px;\n"
                                                 "	font-weight: 600;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover {\n"
                                                 "	border: 1.5px solid #cdd6ee;\n"
                                                 "	color: #cdd6ee;\n"
                                                 "}")
        if self.is_admin:
            self.remove_service_button.setFlat(False)
            self.join_to_service_button.close()
            self.horizontalLayout_3.addWidget(self.remove_service_button)
        else:
            self.nav_to_edit_button.close()
            self.remove_service_button.close()

        self.verticalLayout_2.addWidget(self.footer)

        self.horizontalLayout_2.addWidget(self.content)

        self.horizontalLayout.addWidget(self.container)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    # setupUi

    def retranslateUi(self, card):
        card.setWindowTitle(QCoreApplication.translate("card", u"Form", None))
        self.image.setText("")
        self.image.setPixmap(self.pixmap)
        self.title_label.setText(self.service.title)
        self.price_label.setText(self.get_price())
        self.discount_label.setText(self.get_discount())
        self.join_to_service_button.setText(QCoreApplication.translate("card", u"Записаться", None))
        self.nav_to_edit_button.setText(QCoreApplication.translate("card",
                                                                   u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                   None))
        self.remove_service_button.setText(
            QCoreApplication.translate("card", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))

        self.remove_service_button.clicked.connect(self.on_remove_service_button_click)

        self.nav_to_edit_button.clicked.connect(self.on_edit_service_button_click)

        self.join_to_service_button.clicked.connect(self.join_to_service_button_click)
        # retranslateUi

    def get_price(self) -> str:
        current_price = self.service.cost - decimal.Decimal(
            self.service.discount) * 100 if self.service.discount > 0 else self.service.cost
        return f'{int(current_price)} рублей за {self.service.duration_in_seconds // 60} минут'

    def get_discount(self) -> str:
        return f'* Скидка {int(self.service.discount * 100) if not int(self.service.discount) > 0 else int(self.service.discount)}%' if self.service.discount > 0 else ''

    def on_edit_service_button_click(self):
        self.edit_screen = EditServiceScreen(servie=self.service, is_admin=self.is_admin)
        self.edit_screen.show()
        self.parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().parentWidget().close()

    def on_remove_service_button_click(self):
        try:
            self.service_db.delete(model_id=int(self.service.id))
        except:
            pass
        self.close()

    def join_to_service_button_click(self):
        try:
            self.service_db.create_order(101, self.service.id, datetime.datetime.utcnow())
            QMessageBox.about(self, "Успех", "Вы успешно записались на процедуру")
        except Exception as e:
            QMessageBox.about(self, "Ошибка", f'Кажется что-то пошло не так {e}')