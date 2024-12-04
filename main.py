import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Zubrilo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/main_window.ui', self)  # Загружаем дизайн




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zubrilo()
    ex.show()
    sys.exit(app.exec())