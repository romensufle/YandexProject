import sys
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


class Adding(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Adding()
    ex.show()
    sys.exit(app.exec())