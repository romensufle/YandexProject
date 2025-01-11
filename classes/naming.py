import sys
import io

import classes.adding
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
    <width>498</width>
    <height>306</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLineEdit" name="word_line">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>140</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>140</y>
     <width>61</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Название:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>200</y>
     <width>55</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Язык:</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="translate_line">
   <property name="geometry">
    <rect>
     <x>170</x>
     <y>200</y>
     <width>181</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="add_word">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>250</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавить</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>40</y>
     <width>381</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Придумайте название для нового списка</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Name(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.name = ''
        self.language = ''
        self.date = datetime.date.today()

        self.add_word.clicked.connect(self.get_name)

    def get_name(self):
        if self.word_line.text() and self.translate_line.text():
            self.name = self.word_line.text()
            self.language = self.translate_line.text()

            con = sqlite3.connect('classes/slovarik.sqlite')
            cur = con.cursor()
            sql = f'''
                INSERT INTO katalog(language, spisok_name, date) VALUES("{self.language}", "{self.name}", "{self.date}")
            '''
            cur.execute(sql)
            con.commit()
            con.close()
            self.ma = classes.adding.Adding(self.name, self.language)
            self.ma.show()
            self.close()
            # припрутить передачу choosen_item и choosen_language


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Name()
    ex.show()
    sys.exit(app.exec())
