# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'records_uiJkOuKs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Records_MainWindow(object):
    def setupUi(self, Records_MainWindow):
        if not Records_MainWindow.objectName():
            Records_MainWindow.setObjectName(u"Records_MainWindow")
        Records_MainWindow.resize(800, 800)
        Records_MainWindow.setMinimumSize(QSize(800, 800))
        Records_MainWindow.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(Records_MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(800, 800))
        self.centralwidget.setMaximumSize(QSize(800, 800))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(800, 800))
        self.container.setMaximumSize(QSize(800, 800))
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.header = QFrame(self.container)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setFrameShape(QFrame.NoFrame)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.header)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.nav_to_catalog_button = QPushButton(self.header)
        self.nav_to_catalog_button.setObjectName(u"nav_to_catalog_button")
        self.nav_to_catalog_button.setMaximumSize(QSize(100, 16777215))
        self.nav_to_catalog_button.setStyleSheet(u"QPushButton {\n"
"padding: 10px 15px;\n"
"background: #ff4a6d;\n"
"color: white;\n"
"font-size: 14ppx;\n"
"font-weight: 500;\n"
"border: none;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: black;\n"
"}")

        self.verticalLayout_3.addWidget(self.nav_to_catalog_button)


        self.verticalLayout_2.addWidget(self.header)

        self.main = QFrame(self.container)
        self.main.setObjectName(u"main")
        self.main.setFrameShape(QFrame.StyledPanel)
        self.main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(self.main)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.recored_scroll_container = QWidget()
        self.recored_scroll_container.setObjectName(u"recored_scroll_container")
        self.recored_scroll_container.setGeometry(QRect(0, 0, 780, 727))
        self.scrollArea.setWidget(self.recored_scroll_container)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout_2.addWidget(self.main)


        self.verticalLayout.addWidget(self.container)

        Records_MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Records_MainWindow)

        QMetaObject.connectSlotsByName(Records_MainWindow)
    # setupUi

    def retranslateUi(self, Records_MainWindow):
        Records_MainWindow.setWindowTitle(QCoreApplication.translate("Records_MainWindow", u"MainWindow", None))
        self.nav_to_catalog_button.setText(QCoreApplication.translate("Records_MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

