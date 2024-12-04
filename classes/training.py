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
     <x>530</x>
     <y>320</y>
     <width>111</width>
     <height>41</height>
    </rect>
   </property>
   <property name="text">
    <string>Проверить</string>
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Training()
    ex.show()
    sys.exit(app.exec())