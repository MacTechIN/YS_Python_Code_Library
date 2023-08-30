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


x =10
y =0


z = x/y  #eroDivisionError: division by zero

print(z)


#%%




x =10
y =0
z=0

try:
    z = x/y 
except ZeroDivisionError as e:
    print("오류발생 : 0으로 나누려고 했습니다.", e)
	print("에외발생 : ", ex)


#%%

try : 
	print("x=", x)
	print("y=", y)
	print("z=", z)
	
except NameError as ex:
	print("예외발생 : ",ex)
	
print("The END")
	
	 