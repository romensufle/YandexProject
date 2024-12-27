import sys
import sqlite3

import classes.information
from classes import information, add_sp, adding, delete, hard, naming, training

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

global choose

class Zubrilo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.kat = []
        self.lang_sp = []
        self.date_sp = []
        uic.loadUi('uic/main_window.ui', self)  # Загружаем дизайн

        con = sqlite3.connect('slovarik.sqlite')
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
        self.choosen_item = ''
        self.choosen_language = ''

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
        self.choosen_item = s.split('\t')[0]
        self.choosen_language = s.split('\t')[1]
        print(self.choosen_language, self.choosen_item)

    def f_lang(self, l):
        self.lang = l

    def f_date(self, d):
        self.date = d

    def filter(self):
        if self.lang != '':
            con = sqlite3.connect('slovarik.sqlite')
            cur = con.cursor()
            sql1 = f'''SELECT katalog.spisok_name, language, date FROM katalog
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
            con = sqlite3.connect('slovarik.sqlite')
            cur = con.cursor()
            sql1 = f'''
                        SELECT katalog.spisok_name, language, date FROM katalog
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
        classes.information.Info()
    # сюда воткнуть info

    def tr(self):
        classes.training.Training().choosen_item = self.choosen_item
    # здесь класс training

    def ad(self):
        classes.add_sp.Add_sp()
    # сюда воткнуть add_sp для создания нового списка

    def delete(self):
        classes.delete.Delete().choosen_item = self.choosen_item
    # здесь класс delete

    def ed(self):
        classes.adding.Adding().choosen_item, choosen_language = self.choosen_item, self.choosen_language
    # здесь класс edit


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Zubrilo()
    ex.show()
    sys.exit(app.exec())
