import sys
import io
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
    <width>660</width>
    <height>372</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QListWidget" name="listWidget">
   <property name="geometry">
    <rect>
     <x>140</x>
     <y>60</y>
     <width>380</width>
     <height>81</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>20</pointsize>
    </font>
   </property>
  </widget>
  <widget class="QGroupBox" name="groupBox">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>170</y>
     <width>471</width>
     <height>131</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="title">
    <string>Введите перевод</string>
   </property>
   <widget class="QLineEdit" name="translate_line">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>30</y>
      <width>380</width>
      <height>81</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
  </widget>
  <widget class="QPushButton" name="analiz">
   <property name="geometry">
    <rect>
     <x>410</x>
     <y>310</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Начать</string>
   </property>
  </widget>
  <widget class="QPushButton" name="analiz_2">
   <property name="geometry">
    <rect>
     <x>540</x>
     <y>310</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Завершить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Training(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.choosen_item = 'Yandex'  # поменяяяять
        self.hard_training = '10'  # и эт тоже
        self.base = []
        self.click = 0
        self.end = False
        self.translate_line.setStyleSheet("font: 16pt MS Shell Dlg 2")

        con = sqlite3.connect('slovarik.sqlite')
        cur = con.cursor()

        sql = f'''
            SELECT katalog.word, katalog.translation FROM katalog 
            WHERE spisok_name LIKE "{self.choosen_item}" AND hard LIKE "{self.hard_training}"
        '''
        res = cur.execute(sql).fetchall()
        con.close()

        for el in res:
            self.base.append((el[0], el[1]))
        self.lenght = len(self.base)
        self.item = 0
        self.analiz.clicked.connect(self.proverka)
        self.analiz_2.clicked.connect(self.stop)

    def proverka(self):
        if self.item + 1 > self.lenght and self.end == False:
            self.listWidget.clear()
            self.translate_line.setText('Список закончился')
            self.end = True
        elif self.item + 1 > self.lenght and self.end == True:
            self.close()
        else:
            if self.click % 2 == 0:
                self.analiz.setText('Проверить')
                self.click += 1
            self.listWidget.clear()
            self.listWidget.addItems([self.base[self.item][0]])
            if self.translate_line.text() and self.click % 2 != 0:
                if self.translate_line.text() == self.base[self.item][1]:
                    con = sqlite3.connect('slovarik.sqlite')
                    cur = con.cursor()
                    sql1 = f'''
                        SELECT hard FROM katalog
                        WHERE word LIKE "{self.base[self.item][0]}"
                        AND spisok_name LIKE "{self.choosen_item}"
                    '''

                    res = cur.execute(sql1).fetchall()
                    hrd = 0
                    for el in res:
                        hrd = el[0]
                    if int(hrd) == 0:
                        hrd = 1

                    sql2 = f'''
                        UPDATE katalog SET hard = {int(hrd) - 1}
                        WHERE word LIKE "{self.base[self.item][0]}"
                        AND spisok_name LIKE "{self.choosen_item}"
                    '''
                    cur.execute(sql2)
                    con.commit()
                    con.close()
                    self.translate_line.setText('Правильно!')
                    self.analiz.setText('Продолжить')
                else:
                    con = sqlite3.connect('slovarik.sqlite')
                    cur = con.cursor()
                    sql1 = f'''
                        SELECT hard FROM katalog
                        WHERE word LIKE "{self.base[self.item][0]}"
                        AND spisok_name LIKE "{self.choosen_item}"
                    '''

                    hrd = 0
                    res = cur.execute(sql1).fetchall()
                    for el in res:
                        hrd = el[0]
                    if int(hrd) == 10:
                        hrd = 9

                    sql2 = f'''
                        UPDATE katalog SET hard = {int(hrd) + 1}
                        WHERE word LIKE "{self.base[self.item][0]}"
                        AND spisok_name LIKE "{self.choosen_item}"
                    '''
                    cur.execute(sql2)
                    con.commit()
                    con.close()
                    self.translate_line.clear()
                    self.translate_line.setText(f'Нет! Перевод - {self.base[self.item][1]}')
                    self.analiz.setText('Продолжить')
                self.click += 1
                self.item += 1
            print(self.click, self.item)

    def stop(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Training()
    ex.show()
    sys.exit(app.exec())
