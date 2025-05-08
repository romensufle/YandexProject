import sys
import io

import main
import datetime
import sqlite3

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>338</width>
    <height>205</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLineEdit" name="word_line">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>30</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>30</y>
     <width>55</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Слово:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>90</y>
     <width>55</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Перевод:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="translate_line">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>90</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="add_word">
   <property name="geometry">
    <rect>
     <x>200</x>
     <y>150</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Adding(QMainWindow):  # НАДО СДЕЛАТЬ ТАК, ЧТОБЫ ПОТОМ КАТАЛОГ ОБНОВЛЯЛСЯ
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.date = datetime.date.today()

        self.word = ''
        self.translation = ''
        self.choosen_item = args[0]  # поменять на входную переменную!!!
        self.choosen_language = args[1]  # ЗДЕСЬ ТОЖЕ!!!
        self.add_word.clicked.connect(self.add_wrd)

    def add_wrd(self):
        if self.word_line.text() and self.translate_line.text():
            self.word = self.word_line.text()
            self.translation = self.translate_line.text()
            con = sqlite3.connect('classes/slovarik.sqlite')
            cur = con.cursor()
            sql = f'''
                SELECT katalog.spisok_name FROM katalog 
                WHERE spisok_name LIKE "{self.choosen_item}"
            '''
            res = cur.execute(sql).fetchall()

            sql2 = f'''
                INSERT INTO katalog(word, translation, language, spisok_name, date, hard) 
                VALUES("{self.word}", "{self.translation}", "{self.choosen_language}", "{self.choosen_item}",
                 "{self.date}", 1)
            '''

            cur.execute(sql2)
            con.commit()
            con.close()
            self.close()
            self.m = main.Zubrilo()
            self.m.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Adding()
    ex.show()
    sys.exit(app.exec())
