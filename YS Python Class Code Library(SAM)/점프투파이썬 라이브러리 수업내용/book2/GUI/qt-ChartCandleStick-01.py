#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:06:50 2023

@author: sam
"""

import sys 

from PyQt5.QtWidgets import *
from PyQt5.QtChart import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import * 

import pyupbit
import time
from pandas import Series

SITE_NAME = ["KRW-ETH", "KRW-BTC"]

#Thread 
class Worker(QThread):#사이트에서 실시간으로 데이터를 수신하고 있음 (쓰레드/Background)
    price = pyqtSignal(float)
    def __init__(self):
        super().__init__()
     #Background 에서 계속 돌고 있음 
    def run(self):
        while True:
            cur_price = pyupbit.get_current_price(SITE_NAME[0]) #pyupbit 회사에서 Received Data
            self.price.emit(cur_price)
            time.sleep(1)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # thread 
        self.worker = Worker()
		#Call back 등록 함수 호출 (이름만사용 () 없음), 데이터를 수신하면 호출될 함수 : Self.get_price()
        self.worker.price.connect(self.get_price) 
        self.worker.start() 

        self.minute_cur = QDateTime.currentDateTime()   # current
        self.minute_pre = self.minute_cur.addSecs(-60)  # 1 minute ago
        self.ticks = Series(dtype='float64')  # Pandas시리즈 객체 생성 : 수신된 데이터를 판다스 객체로 보관

        # window size
        self.setMinimumSize(800, 400)
		#분당 80회 수신 (?) 인터벌:1분 
        df = pyupbit.get_ohlcv(SITE_NAME[0], interval='minute1', count=80)
		#판다스 데이터 프레임 
		
        # data : Candle chart 
        self.series = QCandlestickSeries() #
        self.series.setIncreasingColor(Qt.red) #양봉 컬러 
        self.series.setDecreasingColor(Qt.blue) # 음봉 컬러 

        # initial OHLC feeding  
		# df.index 는 판다스의 데이터 프레임 
        for index in df.index:
            open = df.loc[index, 'open'] #시가
            high = df.loc[index, 'high'] #최고가 
            low = df.loc[index, 'low']  #최저가 
            close = df.loc[index, 'close'] # 종가 

            # time conversion 시간 관련 
            format = "%Y-%m-%d %H:%M:%S"
            str_time = index.strftime(format)
            dt = QDateTime.fromString(str_time, "yyyy-MM-dd hh:mm:ss")
            ts = dt.toMSecsSinceEpoch()
            #ts = index.timestamp() * 1000
            #print(ts)

            elem = QCandlestickSet(open, high, low, close, ts)
            self.series.append(elem) #시리즈 값 증가 

        # chart object
        chart = QChart()
        chart.legend().hide()
        chart.addSeries(self.series)         # data feeding

        # X axis (X 축)
        axis_x = QDateTimeAxis()
        axis_x.setFormat("hh:mm:ss")
        chart.addAxis(axis_x, Qt.AlignBottom)
        self.series.attachAxis(axis_x)
		# Y Axis (Y 축) 
        axis_y = QValueAxis()
        axis_y.setLabelFormat("%i")
        chart.addAxis(axis_y, Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        # margin
        chart.layout().setContentsMargins(0, 0, 0, 0)

        # displaying chart
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.setCentralWidget(chart_view)

	#준비작업 
    @pyqtSlot(float)
    def get_price(self, cur_price): #현제 수신된 가격 
        # append current price
        dt = QDateTime.currentDateTime()
        self.statusBar().showMessage(dt.toString())
        self.ticks[dt] = cur_price #판다스의 시리즈에 시간대별 저장 
        # check whether minute change        #if dt.time().minute() != self.minute_cur.time().minute():


        ts = dt.toMSecsSinceEpoch()
        print(ts, cur_price) #현재 가격 

        sets = self.series.sets()
        last_set = sets[-1]                  
		
		
        open = last_set.open()
        high = last_set.high()
        low = last_set.low()
        close = last_set.close()
        ts1 = last_set.timestamp()
        self.series.remove(last_set)        # remove last set
		
		#하나의 봉 (싯가 , 최고 최저 , 이전시간  )
        new_set = QCandlestickSet(open, high, low, cur_price, ts1)
        self.series.append(new_set)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()