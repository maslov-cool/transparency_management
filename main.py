import io
import sys
from PIL import Image

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

my_widget_design = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>416</width>
    <height>440</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QSlider" name="alpha">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>10</y>
      <width>41</width>
      <height>371</height>
     </rect>
    </property>
    <property name="sliderPosition">
     <number>99</number>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="QLabel" name="image">
    <property name="geometry">
     <rect>
      <x>110</x>
      <y>30</y>
      <width>291</width>
      <height>261</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>416</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class AlphaManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(my_widget_design)
        uic.loadUi(f, self)

        self.alpha.setMinimum(0)
        self.alpha.setMaximum(255)
        self.alpha.setValue(255)

        self.alpha.valueChanged.connect(self.update)

        # Изображение
        self.pixmap = QPixmap('orig.jpg')
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

    def update(self):
        im = Image.open("orig.jpg")
        im.putalpha(self.alpha.value())
        im.save('new.png')
        # Изображение
        self.pixmap = QPixmap('new.png')
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())


