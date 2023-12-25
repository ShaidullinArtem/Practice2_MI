import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QVBoxLayout, QStackedWidget
from _decimal import Decimal

from database import Database
from models import ServiceModel, ServicePhotoModel
from screens.catalog_screen import CatalogScreen
from ui.edit_service_ui import Ui_EditService
from ui.widgets import images_widget


class EditServiceScreen(QMainWindow):
    def __init__(self, *, is_admin: bool = False, servie: ServiceModel = None):
        super(EditServiceScreen, self).__init__()
        self.catalog_screen = None
        self.ui = Ui_EditService()
        self.ui.setupUi(self)
        self.setWindowTitle("Обновление услуги")
        self.ui.scrollArea.verticalScrollBar().setEnabled(False)


        self.service = servie
        self.is_admin = is_admin
        self.service_db = Database(
            table_name='Service',
            model=ServiceModel
        )

        self.service_photo_db = Database(
            table_name='ServicePhoto',
            model=ServicePhotoModel,
        )

        self.ui.service_title_lineEdit_2.setText(str(self.service.title))
        self.ui.service_cost_lineEdit.setText(str(self.service.cost))
        self.ui.service_duration_in_seconds_lineEdit.setText(str(self.service.duration_in_seconds))
        self.ui.service_discount_lineEdit.setText(str(self.service.discount))
        self.ui.service_description_lineEdit.setText(str(self.service.description))


        self.service_image_photo = self.service_photo_db.get_by_query(f'ServiceID = {self.service.id}')
        self.service_images = [self.service.main_image_path] + [path.photo_path for path in self.service_image_photo]

        self.ui.nav_to_catalog_button.clicked.connect(self.on_nav_to_catalog_button_click)
        self.ui.update_service_button.clicked.connect(self.on_update_servie_button_click)

        self.ui.service_cost_lineEdit.textChanged.connect(
            lambda state: self.check_number_instance(
                state=state,
                widget=self.ui.service_cost_lineEdit
            )
        )
        self.ui.service_duration_in_seconds_lineEdit.textChanged.connect(
            lambda state: self.check_number_instance(
                state=state,
                widget=self.ui.service_duration_in_seconds_lineEdit
            )
        )
        self.ui.service_discount_lineEdit.textChanged.connect(
            lambda state: self.check_number_instance(
                state=state,
                widget=self.ui.service_discount_lineEdit
            )
        )

        self.ui.add_new_image_button.clicked.connect(self.on_add_new_image_button_click)

        self.make_images_scroll()

        self.show()

    def make_images_scroll(self):
        images_layout = QVBoxLayout(self)
        stack = QStackedWidget()
        widget = images_widget.Images(images_list=self.service_images)
        stack.addWidget(widget)

        images_layout.addWidget(stack)

        self.ui.scrollAreaWidgetContents.setLayout(images_layout)

    def on_nav_to_catalog_button_click(self):
        self.catalog_screen = CatalogScreen(is_admin=self.is_admin)
        self.catalog_screen.show()
        self.close()

    def check_number_instance(self, *, state: str, widget: QLineEdit):
        if not state.isnumeric():
            widget.setText(state[:-1])

    def on_update_servie_button_click(self):
        title = self.ui.service_title_lineEdit_2.text().strip()
        cost = self.ui.service_cost_lineEdit.text()
        duration_in_seconds = self.ui.service_duration_in_seconds_lineEdit.text()
        discount = self.ui.service_discount_lineEdit.text()
        description = self.ui.service_description_lineEdit.text().strip()
        if '' in [title, cost, duration_in_seconds, discount, description]:
            return self.ui.update_service_button.setText('Заполните все поля')

        new_model = ServiceModel(
            id=self.service.id,
            title=title,
            cost=float(cost),
            duration_in_seconds=int(duration_in_seconds),
            discount=Decimal(discount),
            description=description,
            main_image_path=self.service.main_image_path
        )

        if new_model == self.service:
            return self.ui.update_service_button.setText('Нужно изменить хотя бы одно поле')

        try:
            self.service_db.update_service(new_model=new_model)
            QMessageBox.about(self, "Успех", "Вы успешно нобовили услугу")
        except Exception as e:
            QMessageBox.about(self, "Ошибка", f'Кажется что-то пошло не так {e}')

        self.catalog_screen = CatalogScreen(is_admin=self.is_admin)
        self.catalog_screen.show()
        self.close()

    def on_add_new_image_button_click(self):
        image_name = self.ui.new_image_title_lineEdit.text().strip()
        if image_name == '':
            return self.ui.add_new_image_button.setText('Заполните поле')
        elif image_name.rfind('.png') == -1 and image_name.rfind('.jpg') == -1:
            return self.ui.add_new_image_button.setText('Укажите раширение файла')
        elif image_name in self.service_images:
            return self.ui.add_new_image_button.setText('Картинка с таким именем уже существует')


        try:
            self.service_photo_db.create_service_image(
                service_id=self.service.id,
                photo_path=image_name
            )

            QMessageBox.about(self, "Успех", "Вы успешно добавили картинку")
        except Exception as e:
            QMessageBox.about(self, "Ошибка", f'Кажется что-то пошло не так {e}')

        self.catalog_screen = CatalogScreen(is_admin=self.is_admin)
        self.catalog_screen.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EditServiceScreen()
    sys.exit(app.exec_())
