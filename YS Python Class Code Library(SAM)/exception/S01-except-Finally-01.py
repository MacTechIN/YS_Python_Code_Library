#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:53:12 2023

@author: sam
"""

#에외 처리 
#런타임 오류 처리 
#실행시간에 발생하는 오류 처리 
#런타임 오류가 발생하면 프로그램 종료함. 
# e= ZeroDivisionError("division by zero") 


val = 100
list = [10,1,3,5,0] #0,1,2
tot = 0

try:
	for x in list: 
		tot += val / list[x] 
except:
	print("에외발생 !! 원인모름")

#%%