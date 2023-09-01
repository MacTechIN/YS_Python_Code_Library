#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:28:43 2023

@author: sam
"""

# 스크롤 버튼 만들기 
# 셀 정보 가져오기 


import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget() # 데이터 값을 보관하고 수정하는 기능이 들어있음. 
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.label = QLabel('')

        self.scrollToTop = QPushButton('Scroll to Top')
        self.scrollToTop.clicked.connect(self.tableWidget.scrollToTop)

        self.scrollToBottom = QPushButton('Scroll to Bottom')
        self.scrollToBottom.clicked.connect(self.tableWidget.scrollToBottom)

        self.tableWidget.cellClicked.connect(self.set_label) #이벤트 등록 : siginal, slot  event func: cellClicked -> set_label Calling 

        rand_items = np.random.randint(1, 100, size=(20, 4)) # 난수 발생  숫자 , 행령(20*4) 

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_items[i, j]))) # tableWidget.setItem ()  셀에 값을 지정함 ) 
				# 난수 를 스트링으로 변환 i,j(x,y) 로 넣어 값을 가져다 QTableWidgetItem()에 넣어서 setItem으로 넣어서 테이블위젯에 으로 넘겨줌  
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.label)
        layout.addWidget(self.scrollToTop)
        layout.addWidget(self.scrollToBottom)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

    def set_label(self, row, column):
        item = self.tableWidget.item(row, column)
        value = item.text()
        label_string = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())