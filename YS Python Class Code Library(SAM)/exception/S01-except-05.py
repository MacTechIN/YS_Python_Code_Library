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


list = [1,3,5] #0,1,2

try : 
	list[3] = 99 
except IndexError as ex: 
	print(ex)

print("Finished")


