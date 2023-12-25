# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_serviceEOopED.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_EditService(object):
    def setupUi(self, EditService):
        if not EditService.objectName():
            EditService.setObjectName(u"EditService")
        EditService.resize(800, 800)
        EditService.setMinimumSize(QSize(800, 800))
        EditService.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(EditService)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.header = QFrame(self.container)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.title_label = QLabel(self.header)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"QLabel {\n"
"	color: #3f3f3f;\n"
"	font-size: 24px;\n"
"	font-weight: bold;\n"
"}")

        self.horizontalLayout.addWidget(self.title_label)


        self.verticalLayout_2.addWidget(self.header)

        self.main = QFrame(self.container)
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(0, 400))
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.service_field_container_2 = QFrame(self.main)
        self.service_field_container_2.setObjectName(u"service_field_container_2")
        self.service_field_container_2.setFrameShape(QFrame.NoFrame)
        self.service_field_container_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.service_field_container_2)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.service_title_label_2 = QLabel(self.service_field_container_2)
        self.service_title_label_2.setObjectName(u"service_title_label_2")
        self.service_title_label_2.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"}")

        self.horizontalLayout_3.addWidget(self.service_title_label_2)

        self.service_title_lineEdit_2 = QLineEdit(self.service_field_container_2)
        self.service_title_lineEdit_2.setObjectName(u"service_title_lineEdit_2")
        self.service_title_lineEdit_2.setMinimumSize(QSize(600, 0))
        self.service_title_lineEdit_2.setMaximumSize(QSize(600, 16777215))
        self.service_title_lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.horizontalLayout_3.addWidget(self.service_title_lineEdit_2)


        self.verticalLayout_3.addWidget(self.service_field_container_2)

        self.service_field_container_3 = QFrame(self.main)
        self.service_field_container_3.setObjectName(u"service_field_container_3")
        self.service_field_container_3.setFrameShape(QFrame.NoFrame)
        self.service_field_container_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.service_field_container_3)
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.service_cost_label = QLabel(self.service_field_container_3)
        self.service_cost_label.setObjectName(u"service_cost_label")
        self.service_cost_label.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"}")

        self.horizontalLayout_4.addWidget(self.service_cost_label)

        self.service_cost_lineEdit = QLineEdit(self.service_field_container_3)
        self.service_cost_lineEdit.setObjectName(u"service_cost_lineEdit")
        self.service_cost_lineEdit.setMinimumSize(QSize(600, 0))
        self.service_cost_lineEdit.setMaximumSize(QSize(600, 16777215))
        self.service_cost_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.horizontalLayout_4.addWidget(self.service_cost_lineEdit)


        self.verticalLayout_3.addWidget(self.service_field_container_3)

        self.service_field_container_4 = QFrame(self.main)
        self.service_field_container_4.setObjectName(u"service_field_container_4")
        self.service_field_container_4.setFrameShape(QFrame.NoFrame)
        self.service_field_container_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.service_field_container_4)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.service_duration_in_seconds_label = QLabel(self.service_field_container_4)
        self.service_duration_in_seconds_label.setObjectName(u"service_duration_in_seconds_label")
        self.service_duration_in_seconds_label.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"}")

        self.horizontalLayout_5.addWidget(self.service_duration_in_seconds_label)

        self.service_duration_in_seconds_lineEdit = QLineEdit(self.service_field_container_4)
        self.service_duration_in_seconds_lineEdit.setObjectName(u"service_duration_in_seconds_lineEdit")
        self.service_duration_in_seconds_lineEdit.setMinimumSize(QSize(600, 0))
        self.service_duration_in_seconds_lineEdit.setMaximumSize(QSize(600, 16777215))
        self.service_duration_in_seconds_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.horizontalLayout_5.addWidget(self.service_duration_in_seconds_lineEdit)


        self.verticalLayout_3.addWidget(self.service_field_container_4)

        self.service_field_container = QFrame(self.main)
        self.service_field_container.setObjectName(u"service_field_container")
        self.service_field_container.setFrameShape(QFrame.NoFrame)
        self.service_field_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.service_field_container)
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.service_discount_label = QLabel(self.service_field_container)
        self.service_discount_label.setObjectName(u"service_discount_label")
        self.service_discount_label.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"}")

        self.horizontalLayout_2.addWidget(self.service_discount_label)

        self.service_discount_lineEdit = QLineEdit(self.service_field_container)
        self.service_discount_lineEdit.setObjectName(u"service_discount_lineEdit")
        self.service_discount_lineEdit.setMinimumSize(QSize(600, 0))
        self.service_discount_lineEdit.setMaximumSize(QSize(600, 16777215))
        self.service_discount_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.horizontalLayout_2.addWidget(self.service_discount_lineEdit)


        self.verticalLayout_3.addWidget(self.service_field_container)

        self.service_field_container_5 = QFrame(self.main)
        self.service_field_container_5.setObjectName(u"service_field_container_5")
        self.service_field_container_5.setFrameShape(QFrame.NoFrame)
        self.service_field_container_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.service_field_container_5)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.service_description_label = QLabel(self.service_field_container_5)
        self.service_description_label.setObjectName(u"service_description_label")
        self.service_description_label.setStyleSheet(u"QLabel {\n"
"	color: #666666;\n"
"	font-size: 12px;\n"
"	font-weight: 400;\n"
"}")

        self.horizontalLayout_6.addWidget(self.service_description_label)

        self.service_description_lineEdit = QLineEdit(self.service_field_container_5)
        self.service_description_lineEdit.setObjectName(u"service_description_lineEdit")
        self.service_description_lineEdit.setMinimumSize(QSize(600, 60))
        self.service_description_lineEdit.setMaximumSize(QSize(600, 16777215))
        self.service_description_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.horizontalLayout_6.addWidget(self.service_description_lineEdit)


        self.verticalLayout_3.addWidget(self.service_field_container_5)


        self.verticalLayout_2.addWidget(self.main)

        self.footer = QFrame(self.container)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.NoFrame)
        self.footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.footer)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.images = QFrame(self.footer)
        self.images.setObjectName(u"images")
        self.images.setFrameShape(QFrame.StyledPanel)
        self.images.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.images)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(self.images)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 751, 191))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.images)

        self.buttons = QFrame(self.footer)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMinimumSize(QSize(0, 120))
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.buttons)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.add_image_container = QFrame(self.buttons)
        self.add_image_container.setObjectName(u"add_image_container")
        self.add_image_container.setMaximumSize(QSize(400, 16777215))
        self.add_image_container.setFrameShape(QFrame.StyledPanel)
        self.add_image_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.add_image_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.add_new_image_button = QPushButton(self.add_image_container)
        self.add_new_image_button.setObjectName(u"add_new_image_button")
        self.add_new_image_button.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_5.addWidget(self.add_new_image_button)

        self.new_image_title_lineEdit = QLineEdit(self.add_image_container)
        self.new_image_title_lineEdit.setObjectName(u"new_image_title_lineEdit")
        self.new_image_title_lineEdit.setStyleSheet(u"QLineEdit {\n"
"	padding: 5px 10px;\n"
"	border: 1.2px solid #666666;\n"
"	color: #666666;\n"
"	font-size: 13px;\n"
"	font-weight: 400;\n"
"	border-radius: 5px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border: 1px solid #888888;\n"
"}")

        self.verticalLayout_5.addWidget(self.new_image_title_lineEdit)


        self.horizontalLayout_8.addWidget(self.add_image_container)

        self.nav_container = QFrame(self.buttons)
        self.nav_container.setObjectName(u"nav_container")
        self.nav_container.setFrameShape(QFrame.StyledPanel)
        self.nav_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.nav_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.update_service_button = QPushButton(self.nav_container)
        self.update_service_button.setObjectName(u"update_service_button")
        self.update_service_button.setStyleSheet(u"QPushButton {\n"
"	padding: 10px 15px;\n"
"	background: #ff4a6d;\n"
"	color: white;\n"
"	font-size: 14px;\n"
"	font-weight: 500;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"}")

        self.horizontalLayout_9.addWidget(self.update_service_button)

        self.nav_to_catalog_button = QPushButton(self.nav_container)
        self.nav_to_catalog_button.setObjectName(u"nav_to_catalog_button")
        self.nav_to_catalog_button.setStyleSheet(u"QPushButton {\n"
"	padding: 10px 15px;\n"
"	background: #ff4a6d;\n"
"	color: white;\n"
"	font-size: 14px;\n"
"	font-weight: 500;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"}")

        self.horizontalLayout_9.addWidget(self.nav_to_catalog_button)


        self.horizontalLayout_8.addWidget(self.nav_container)


        self.verticalLayout_4.addWidget(self.buttons)


        self.verticalLayout_2.addWidget(self.footer)


        self.horizontalLayout_7.addWidget(self.container)

        EditService.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditService)

        QMetaObject.connectSlotsByName(EditService)
    # setupUi

    def retranslateUi(self, EditService):
        EditService.setWindowTitle(QCoreApplication.translate("EditService", u"MainWindow", None))
        self.title_label.setText(QCoreApplication.translate("EditService", u"\u041e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0443\u0441\u043b\u0443\u0433\u0438", None))
        self.service_title_label_2.setText(QCoreApplication.translate("EditService", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435:", None))
        self.service_cost_label.setText(QCoreApplication.translate("EditService", u"\u0421\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c:", None))
        self.service_duration_in_seconds_label.setText(QCoreApplication.translate("EditService", u"\u0414\u043b\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:", None))
        self.service_duration_in_seconds_lineEdit.setInputMask("")
        self.service_discount_label.setText(QCoreApplication.translate("EditService", u"\u0421\u043a\u0430\u0438\u0434\u043a\u0430:", None))
        self.service_description_label.setText(QCoreApplication.translate("EditService", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.add_new_image_button.setText(QCoreApplication.translate("EditService", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.new_image_title_lineEdit.setPlaceholderText(QCoreApplication.translate("EditService", u"\u0418\u043c\u044f \u043d\u043e\u0432\u043e\u0433\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f", None))
        self.update_service_button.setText(QCoreApplication.translate("EditService", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.nav_to_catalog_button.setText(QCoreApplication.translate("EditService", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

