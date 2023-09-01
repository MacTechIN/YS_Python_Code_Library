#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:06:13 2023

@author: sam
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget): #QWiget 을 넣어서 MyApp 콜 

    def __init__(self):
        super().__init__() #Constructor 
        self.initUI() #자신의 initUI 함수 호출 

    def initUI(self):
        self.setWindowTitle('Hello World Window')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()


if __name__ == '__main__': # 시작점 
   app = QApplication(sys.argv) # QT Main Application Call app 로 저장 
   ex = MyApp()  ## 메인 호출 
   sys.exit(app.exec_()) #시스템 종료 