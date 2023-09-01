#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:06:13 2023

@author: sam
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget): #QWiget 을 넣어서 MyApp 콜 

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box) #Box style 

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel) #그림자 효과 
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)  #수직 
        splitter1.addWidget(midleft) # 중간 에 1번 위치 시킴 (좌우)
        splitter1.addWidget(midright) 

        splitter2 = QSplitter(Qt.Vertical) # TOP 
        splitter2.addWidget(top)  
        splitter2.addWidget(splitter1)  
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2) # HBox Vertical  
        self.setLayout(hbox) 

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__': # 시작점 
   app = QApplication(sys.argv) # QT Main Application Call app 로 저장 
   ex = MyApp()  ## 메인 호출 
   sys.exit(app.exec_()) #시스템 종료 