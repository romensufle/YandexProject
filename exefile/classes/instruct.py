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
    <width>1142</width>
    <height>657</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>70</x>
     <y>50</y>
     <width>1001</width>
     <height>551</height>
    </rect>
   </property>
   <property name="text">
    <string>TextLabel</string>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>'''


class Instr(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        lst = []
        st = ''
        with open('classes/инструкция.txt', encoding='utf8') as f:
            for el in f.readlines():
                lst.append(el.rstrip())
        for el in lst:
            st += el
            st += '\n'
        self.label.setStyleSheet("font: 13pt")
        self.label.setText(st)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Instr()
    ex.show()
    sys.exit(app.exec())
