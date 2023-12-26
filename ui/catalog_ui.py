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
        # self.search_lineEdit.setText("")
        # self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow_Catalog", u"\u042f \u0445\u043e\u0447\u0443 \u043d\u0430\u0439\u0442\u0438 ...", None))
        # self.price_filter_label.setText(QCoreApplication.translate("MainWindow_Catalog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0446\u0435\u043d\u0435: ", None))
        # self.discount_filter_label.setText(QCoreApplication.translate("MainWindow_Catalog", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u043f\u043e \u0441\u043a\u0438\u0434\u043a\u0435: ", None))
    # retranslateUi

