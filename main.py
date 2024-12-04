import sys
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Zubrilo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kat = []
        con = sqlite3.connect('slovarik.sqlite')
        cur = con.cursor()
        sql = '''
            SELECT DISTINCT spiski.spisok_name FROM katalog
            LEFT JOIN spiski ON katalog.spisok_id = spiski.id
        '''
        res = cur.execute(sql).fetchall()
        con.close()
        for el in res:
            self.kat.append(el[0])

        uic.loadUi('uic/main_window.ui', self)  # Загружаем дизайн
        self.lang = 'Английский'
        self.date = 1
        self.katalog.addItems([ev for ev in self.kat])
        self.info.clicked.connect(self.i)
        self.pushButton.clicked.connect(self.tr)
        self.pushButton_2.clicked.connect(self.ed)
        self.pushButton_3.clicked.connect(self.ad)
        self.pushButton_4.clicked.connect(self.delete)
        self.use_filter.clicked.connect(self.filter)
        self.lang_filter.currentTextChanged.connect(self.f_lang)
        self.date_filter.currentTextChanged.connect(self.f_date)

    def f_lang(self, l):
        self.lang = l

    def filter(self):
        pass

    def f_date(self, d):
        if d == 'Новые':
            self.date = 1
        elif d == 'Старые':
            self.date = -1

    def i(self):
        pass
    # сюда воткнуть info

    def tr(self):
        pass
    # здесь класс training

    def ad(self):
        pass
    # сюда воткнуть add_sp для создания нового списка

    def delete(self):
        pass
    # здесь класс delete

    def ed(self):
        pass
    # здесь класс edit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zubrilo()
    ex.show()
    sys.exit(app.exec())
