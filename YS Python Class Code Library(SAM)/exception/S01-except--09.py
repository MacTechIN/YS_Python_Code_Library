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

#%%
#사용자 정의 예외 

#Exception 최상위 예외 클래스를 상속을 받음 
class MyError(Exception):
	def __init__(self,why,msg):
		super().__init_(msg)
		self.why = why 



#%%
#예외 발생 


def say_nic(nick):
	if nick=='바보':
		raise MyError("바보" , "나를 너무 무시해서 용서가안됨.")
	
	print(nick)
#%%
say_nic('바보')



#%%


try : 
	say_nic("천사")
	say_nic("바보")
	say_nic("사람")
except MyError as e:
	print("예외발생",e)



#%%



val = 100
list = [0,1,2,3,2,10] #0,1,2
tot = 0

try:
	for x in list: 
		tot += val / list[x] 
except:
	print("에외발생 !! 원인모름")
else: 
	print("else: 예외가 발생되지 않으면 처리")
finally:
	print("무조건 처리됨.")

print("tot : ", tot)

#%%