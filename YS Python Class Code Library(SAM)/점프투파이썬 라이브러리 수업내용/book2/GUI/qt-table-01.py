#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:18:55 2023

https://codetorial.net/articles/qtablewidget_pyqt5_2.html

@author: sam
"""

import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.clearBtn = QPushButton('Clear')
        self.clearBtn.clicked.connect(self.tableWidget.clear) # 버튼이 눌리면 내용을 다 지워라 

		#20*4 행렬의 난수 1~100까지 생성 
        rand_items = np.random.randint(1, 100, size=(20, 4))
		
        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_items[i, j])))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        layout.addWidget(self.clearBtn)
        self.setLayout(layout)

        self.setWindowTitle('PyQt5 - QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())