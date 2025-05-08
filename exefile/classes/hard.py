import sys
import io
import classes.training

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
    <width>415</width>
    <height>465</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QGroupBox" name="groupBox">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>100</y>
     <width>271</width>
     <height>301</height>
    </rect>
   </property>
   <property name="title">
    <string>Сложность</string>
   </property>
   <widget class="QPushButton" name="easy_hard">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>60</y>
      <width>191</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Легкая</string>
    </property>
   </widget>
   <widget class="QPushButton" name="main_hard">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>130</y>
      <width>191</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Средняя</string>
    </property>
   </widget>
   <widget class="QPushButton" name="hard_hard">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>200</y>
      <width>191</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Сложная</string>
    </property>
   </widget>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>20</y>
     <width>371</width>
     <height>61</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Выберите уровень сложности</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

class Hard(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.choosen_item = args[0]
        self.easy_hard.clicked.connect(self.easy)
        self.main_hard.clicked.connect(self.middle)
        self.hard_hard.clicked.connect(self.hard)
        self.wrdhrd = ''

    def easy(self):
        self.wrdhrd = '3'
        self.t = classes.training.Training(self.choosen_item, self.wrdhrd)
        self.t.show()
        self.close()

    # запускать тренировку, передавать уровень сложности 3 и меньше

    def middle(self):
        self.wrdhrd = '7'
        self.tr = classes.training.Training(self.choosen_item, self.wrdhrd)
        self.tr.show()
        self.close()

    # запускать тренировку, передавать уровень сложности 7 и меньше

    def hard(self):
        self.wrdhrd = '10'
        self.tr = classes.training.Training(self.choosen_item, self.wrdhrd)
        self.tr.show()
        self.close()
    # запускать тренировку, передавать уровень сложности 10 и меньше


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Hard()
    ex.show()
    sys.exit(app.exec())
