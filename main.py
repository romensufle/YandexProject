import sys
import sqlite3

import classes.information
from classes import information, add_sp, adding, delete, hard, naming, training

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class Zubrilo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.choosen_item = 'Yandex'
        self.choosen_language = ''
        self.kat = []
        self.lang_sp = []
        self.date_sp = []
        uic.loadUi('uic/main_window.ui', self)  # Загружаем дизайн

        con = sqlite3.connect('classes/slovarik.sqlite')
        cur = con.cursor()
        sql1 = '''
            SELECT DISTINCT katalog.spisok_name, language, date FROM katalog
        '''
        res1 = cur.execute(sql1).fetchall()

        sql2 = '''
            SELECT DISTINCT katalog.language FROM katalog
        '''
        res2 = cur.execute(sql2).fetchall()

        sql3 = '''
            SELECT DISTINCT date FROM katalog
        '''
        res3 = cur.execute(sql3).fetchall()
        con.close()

        for el in res1:
            self.kat.append(f'{el[0]} \t {el[1]} \t {el[2]}')
        self.kat.sort()

        for el in res2:
            self.lang_sp.append(el[0])

        for el in res3:
            self.date_sp.append(el[0])

        self.setWindowTitle('Zubrilo')
        self.lang = ''
        self.date = 0


        self.katalog.addItems([ev for ev in self.kat])
        self.lang_filter.addItems([la for la in self.lang_sp])
        self.date_filter.addItems([da for da in self.date_sp])

        self.info.clicked.connect(self.i)
        self.pushButton.clicked.connect(self.tr)
        self.pushButton_2.clicked.connect(self.ed)
        self.pushButton_3.clicked.connect(self.ad)
        self.pushButton_4.clicked.connect(self.delete)
        self.use_filter.clicked.connect(self.filter)
        self.lang_filter.currentTextChanged.connect(self.f_lang)
        self.date_filter.currentTextChanged.connect(self.f_date)
        self.katalog.currentTextChanged.connect(self.choose)

    def choose(self, s):
        self.choosen_item = s
        self.choosen_language = s
        if self.choosen_item and self.choosen_language:
            self.choosen_item = self.choosen_item.split('\t')[0].strip()
            self.choosen_language = self.choosen_language.split('\t')[1].strip()

    def f_lang(self, l):
        self.lang = l

    def f_date(self, d):
        self.date = d

    def filter(self):
        if self.lang != '':
            con = sqlite3.connect('classes/slovarik.sqlite')
            cur = con.cursor()
            sql1 = f'''SELECT DISTINCT katalog.spisok_name, language, date FROM katalog
                        WHERE language LIKE "{self.lang}"
                    '''
            res1 = cur.execute(sql1).fetchall()
            self.katalog.clear()
            self.kat = []
            for el in res1:
                self.kat.append(f'{el[0]} \t {el[1]} \t {el[2]}')
            con.close()

            self.katalog.addItems([ev for ev in self.kat])
        if self.date != 0:
            con = sqlite3.connect('classes/slovarik.sqlite')
            cur = con.cursor()
            sql1 = f'''
                        SELECT DISTINCT katalog.spisok_name, language, date FROM katalog
                        WHERE date LIKE "{self.date}"
                    '''
            res1 = cur.execute(sql1).fetchall()
            self.kat = []
            for el in res1:
                self.kat.append(f'{el[0]} \t {el[1]} \t {el[2]}')
            con.close()
            self.katalog.clear()
            self.katalog.addItems([ev for ev in self.kat])

    def i(self):
        self.inf = classes.information.Info()
        self.inf.show()

    # сюда воткнуть info

    def tr(self):
        self.tr = classes.hard.Hard(self.choosen_item)
        self.tr.show()
        self.close()

    # здесь класс training

    def ad(self):
        self.add = classes.add_sp.Add_sp()
        self.add.show()
        self.close()
    # сюда воткнуть add_sp для создания нового списка

    def delete(self):
        self.dele = classes.delete.Delete(self.choosen_item)
        self.dele.show()
        self.close()
    # здесь класс delete

    def ed(self):
        self.ede = classes.adding.Adding(self.choosen_item, self.choosen_language)
        self.ede.show()
        self.close()
    # здесь класс edit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zubrilo()
    ex.show()
    sys.exit(app.exec())
