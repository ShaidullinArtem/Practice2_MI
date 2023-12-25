import os
from typing import List

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout


class Images(QWidget):
    def __init__(self, *, images_list: List[str], parent=None):
        QWidget.__init__(self, parent=parent)
        self.images_list = images_list

        images_layout = QHBoxLayout(self)
        for path in self.images_list:
            image = QLabel()
            image.setAlignment(Qt.AlignCenter)
            image.setMinimumSize(150, 150)
            image.setMaximumSize(150, 150)
            image.setStyleSheet(u"QLabel {\n"
                                             "	background: #eecdcd;\n"
                                             "	border: 1px solid #cbcbcb;\n"
                                             "	border-radius: 5px;\n"
                                             "}")
            image.setObjectName(u'image')
            image_path = f'../media/service_images/{path}'
            if os.path.isfile(image_path):
                image.setScaledContents(True)
                pixmap = QPixmap(image_path)
                image.setPixmap(pixmap)
            else:
                image.setText('Изображение не найдено')

            images_layout.addWidget(image)

