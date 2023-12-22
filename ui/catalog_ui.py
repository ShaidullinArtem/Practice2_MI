# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catalog_uivsYDhM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow_Catalog(object):
    def setupUi(self, MainWindow_Catalog):
        if not MainWindow_Catalog.objectName():
            MainWindow_Catalog.setObjectName(u"MainWindow_Catalog")
        MainWindow_Catalog.resize(800, 800)
        MainWindow_Catalog.setMinimumSize(QSize(800, 800))
        MainWindow_Catalog.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(MainWindow_Catalog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 15, 10, 10)
        self.search = QFrame(self.container)
        self.search.setObjectName(u"search")
        self.search.setMinimumSize(QSize(0, 40))
        self.search.setMaximumSize(QSize(16777215, 40))
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


        self.verticalLayout_2.addWidget(self.search)

        self.content = QFrame(self.container)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(self.content)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName(u"scroll_content")
        self.scroll_content.setGeometry(QRect(0, 0, 750, 695))
        self.scroll_content.setStyleSheet(u"")
        self.scrollArea.setWidget(self.scroll_content)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.container)

        MainWindow_Catalog.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_Catalog)

        QMetaObject.connectSlotsByName(MainWindow_Catalog)
    # setupUi

    def retranslateUi(self, MainWindow_Catalog):
        MainWindow_Catalog.setWindowTitle(QCoreApplication.translate("MainWindow_Catalog", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.search_lineEdit.setInputMask("")
        self.search_lineEdit.setText("")
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow_Catalog", u"\u042f \u0445\u043e\u0447\u0443 \u043d\u0430\u0439\u0442\u0438 ...", None))
        self.price_filter_label.setText(QCoreApplication.translate("MainWindow_Catalog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0446\u0435\u043d\u0435: ", None))
        self.discount_filter_label.setText(QCoreApplication.translate("MainWindow_Catalog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u043e \u0441\u043a\u0438\u0434\u043a\u0435: ", None))
    # retranslateUi

