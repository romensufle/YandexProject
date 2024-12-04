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
    <width>708</width>
    <height>423</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QListWidget" name="listWidget">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>40</y>
     <width>501</width>
     <height>331</height>
    </rect>
   </property>
  </widget>
  <widget class="QPushButton" name="add_word">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>250</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Добавить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="delete_word">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>340</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Удалить</string>
   </property>
  </widget>
  <widget class="QPushButton" name="edit_word">
   <property name="geometry">
    <rect>
     <x>580</x>
     <y>295</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string>Изменить</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>

'''


class Edit(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Edit()
    ex.show()
    sys.exit(app.exec())