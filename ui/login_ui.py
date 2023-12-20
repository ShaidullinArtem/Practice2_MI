# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerczKUzC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow_Login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.container = QFrame(self.centralwidget)
        self.container.setObjectName(u"container")
        self.container.setFrameShape(QFrame.StyledPanel)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 25)
        self.logo = QFrame(self.container)
        self.logo.setObjectName(u"logo")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.logo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_image = QLabel(self.logo)
        self.logo_image.setObjectName(u"logo_image")
        self.logo_image.setPixmap(QPixmap(u"../media/login/beauty_logo.ico"))
        self.logo_image.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.logo_image)


        self.verticalLayout_2.addWidget(self.logo)

        self.pin_code_container = QFrame(self.container)
        self.pin_code_container.setObjectName(u"pin_code_container")
        self.pin_code_container.setMinimumSize(QSize(0, 80))
        self.pin_code_container.setMaximumSize(QSize(16777215, 80))
        self.pin_code_container.setFrameShape(QFrame.NoFrame)
        self.pin_code_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.pin_code_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pin_code_label = QLabel(self.pin_code_container)
        self.pin_code_label.setObjectName(u"pin_code_label")
        self.pin_code_label.setStyleSheet(u"QLabel {\n"
"	font-size: 16px;\n"
"	color: black;\n"
"	font-weight: medium;\n"
"}")

        self.verticalLayout_3.addWidget(self.pin_code_label)

        self.pin_code_lineEdit = QLineEdit(self.pin_code_container)
        self.pin_code_lineEdit.setObjectName(u"pin_code_lineEdit")
        self.pin_code_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    padding: 10px 5px;\n"
"	color: black;\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"}")

        self.verticalLayout_3.addWidget(self.pin_code_lineEdit)


        self.verticalLayout_2.addWidget(self.pin_code_container)

        self.customer_mode_container = QFrame(self.container)
        self.customer_mode_container.setObjectName(u"customer_mode_container")
        self.customer_mode_container.setMinimumSize(QSize(0, 40))
        self.customer_mode_container.setMaximumSize(QSize(16777215, 40))
        self.customer_mode_container.setFrameShape(QFrame.NoFrame)
        self.customer_mode_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.customer_mode_container)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.customer_check_box = QCheckBox(self.customer_mode_container)
        self.customer_check_box.setObjectName(u"customer_check_box")
        self.customer_check_box.setStyleSheet(u"QCheckBox {\n"
"	font-size: 16px;\n"
"	color: black;\n"
"}")

        self.horizontalLayout.addWidget(self.customer_check_box)


        self.verticalLayout_2.addWidget(self.customer_mode_container)

        self.submit_button = QPushButton(self.container)
        self.submit_button.setObjectName(u"pushButton")
        self.submit_button.setStyleSheet(u"QPushButton {\n"
"	background: #673ab7;\n"
"	padding: 10px 40px;\n"
"	color: white;\n"
"    font-weight: bold;\n"
"	font-size: 14px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background: #673ae7;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"	outline: none;\n"
"	border: none;\n"
"}")

        self.verticalLayout_2.addWidget(self.submit_button)


        self.verticalLayout.addWidget(self.container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434 \u0432 \u0441\u0438\u0441\u0442\u0435\u043c\u0443", None))
        self.logo_image.setText("")
        self.pin_code_label.setText(QCoreApplication.translate("MainWindow", u"PIN-\u041a\u043e\u0434:", None))
        self.customer_check_box.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438 \u0432 \u0440\u0435\u0436\u0438\u043c \u0433\u043e\u0441\u0442\u044f", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

