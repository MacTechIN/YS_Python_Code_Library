#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 11:06:13 2023

@author: sam
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget): #QWiget 을 넣어서 MyApp 콜 

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2') #Alt+ 2: 클릭

        btn3 = QPushButton('Button3', self)
        btn3.setText('Button&3')
		
		#Layout : 배치 
        vbox = QVBoxLayout() # 박스타입레이아웃, 여러 가지 레이아웃 방식 지원 , CSSㄴ레이아웃 처럼 자신만의 방식이 있다. 
        vbox.addWidget(btn1) #버튼의속성을 가진 위젯을 
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox) ㅣ#레이아웃 구성 (레이아웃은 컨테이너 역활을 함. 박스형태의 틀)
        self.setWindowTitle('QPushButton') 
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__': # 시작점 
   app = QApplication(sys.argv) # QT Main Application Call app 로 저장 
   ex = MyApp()  ## 메인 호출 
   sys.exit(app.exec_()) #시스템 종료 