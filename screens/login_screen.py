import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from env import Environment
from screens import CatalogScreen
from ui import Ui_MainWindow_Login
from utlis.error import PinCodeEmptyOrInvalidValue


class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.catalog_screen = None
        self.ui = Ui_MainWindow_Login()
        self.ui.setupUi(self)

        self.is_admin = True

        self.ui.submit_button.clicked.connect(self.on_submit_button_click)
        self.ui.customer_check_box.stateChanged.connect(self.on_customer_check_box_change)

        self.show()

    def on_customer_check_box_change(self, state: QtCore.Qt.CheckState):
        self.is_admin = QtCore.Qt.Checked != state
        self.ui.pin_code_lineEdit.setEnabled(self.is_admin)

    def on_submit_button_click(self):
        if self.is_admin:
            try:
                code = self.ui.pin_code_lineEdit.text()
                if len(code) == 0:
                    raise PinCodeEmptyOrInvalidValue('Заполните поле pin-кода')
                if code != Environment.PIN_CODE:
                    raise PinCodeEmptyOrInvalidValue('Неверный pin-код')
            except PinCodeEmptyOrInvalidValue as e:
                self.ui.submit_button.setText(e.message)
                return

        self.catalog_screen = CatalogScreen(is_admin=self.is_admin)
        self.catalog_screen.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginScreen()
    sys.exit(app.exec_())
