# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designeraGNpwn.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow_Catalog(object):
    def setupUi(self, Ui_MainWindow_Catalog):
        if not Ui_MainWindow_Catalog.objectName():
            Ui_MainWindow_Catalog.setObjectName(u"Ui_MainWindow_Catalog")
        Ui_MainWindow_Catalog.resize(800, 800)
        Ui_MainWindow_Catalog.setMinimumSize(QSize(800, 800))
        self.centralwidget = QWidget(Ui_MainWindow_Catalog)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"	color: red;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"	color: blue;\n"
"}")
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.search_lineEdit = QLineEdit(self.search)
        self.search_lineEdit.setObjectName(u"search_lineEdit")
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


        self.verticalLayout_2.addWidget(self.search)

        self.content = QFrame(self.container)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.content)


        self.verticalLayout.addWidget(self.container)

        Ui_MainWindow_Catalog.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ui_MainWindow_Catalog)

        QMetaObject.connectSlotsByName(Ui_MainWindow_Catalog)
    # setupUi

    def retranslateUi(self, Ui_MainWindow_Catalog):
        Ui_MainWindow_Catalog.setWindowTitle(QCoreApplication.translate("Ui_MainWindow_Catalog", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.search_lineEdit.setInputMask("")
        self.search_lineEdit.setText("")
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("Ui_MainWindow_Catalog", u"\u042f \u0445\u043e\u0447\u0443 \u043d\u0430\u0439\u0442\u0438 ...", None))
    # retranslateUi

