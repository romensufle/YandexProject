import sys
import io

from classes import instruct

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>699</width>
    <height>334</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>20</y>
     <width>201</width>
     <height>51</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>16</pointsize>
    </font>
   </property>
   <property name="text">
    <string>О приложении: </string>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>90</y>
     <width>111</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Разработчик:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>93</y>
     <width>71</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>romensufle</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_4">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>130</y>
     <width>141</width>
     <height>21</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="text">
    <string>Текущая версия:</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_5">
   <property name="geometry">
    <rect>
     <x>210</x>
     <y>133</y>
     <width>55</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>1.0</string>
   </property>
  </widget>
  <widget class="QLabel" name="image_label">
   <property name="geometry">
    <rect>
     <x>370</x>
     <y>20</y>
     <width>300</width>
     <height>276</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
  <widget class="QPushButton" name="inst">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>250</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Инструкция</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class Info(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.image_logo = QImage('logo.jpg')
        self.pixmap = QPixmap.fromImage(self.image_logo)
        self.image_label.setPixmap(self.pixmap)
        self.inst.clicked.connect(self.instruction)

    def instruction(self):
        instruct.Instr()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Info()
    ex.show()
    sys.exit(app.exec())
