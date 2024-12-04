import sys
import sqlite3
import io

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
    <width>443</width>
    <height>176</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>110</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Да</string>
   </property>
  </widget>
  <widget class="QPushButton" name="pushButton_2">
   <property name="geometry">
    <rect>
     <x>260</x>
     <y>110</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Нет</string>
   </property>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>30</y>
     <width>351</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>12</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Вы точно хотите удалить этот список?</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Delete(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.deleting)
        self.pushButton_2.clicked.connect(lambda: self.close())

    def deleting(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Delete()
    ex.show()
    sys.exit(app.exec())