#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:03:00 2023

@author: sam
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) # LCD 창 
        dial = QDial(self) # 다이얼 

        vbox = QVBoxLayout()  #Layout Vertical Box 
        vbox.addWidget(lcd) 
        vbox.addWidget(dial) 
        self.setLayout(vbox) 

        dial.valueChanged.connect(lcd.display) # 다이얼에 값이 바뀌면 LCD 에 연결 해라 

        self.setWindowTitle('Signal and Slot') #
        self.setGeometry(600, 600, 200, 200
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())