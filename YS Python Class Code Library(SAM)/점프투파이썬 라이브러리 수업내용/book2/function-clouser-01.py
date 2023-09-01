#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:07:09 2023

@author: sam
"""

#클로져 (Clouser)
#it descrbe the fucntion that deploy interal function and returns It's internal function 

#클로져 함수 
def mul(m): #외부 함수 
	def wrapper(n): #내부 함수 
		return m * n  # m은 고정값 
	
	return wrapper

#%%

mul3 = mul(3) #3을 곱하는 함수 
mul5 = mul(5) #5를 곱하는 함수 


print(mul3(10)) # 30 = 3 * 10 
print(mul5(10)) # 50 = 5 * 10 

#mul 함수가 한개이지만, 이 것을 mul3, mul5 숫자에 맞도록 함수를 만들언 놓고 사용 하려는 목적임.

#%%
print(type(mul3))

#%%

##클래스를 이용 클로져 기능을 시뮬레이션 

class Mul:
	def __init__ (self, m):
		self.m = m 
		
		
	def mul (self, n):
		return  self.m * n 
	
	
	def __call__(self, n):
		return self.m * n 
	
	def value(self):
		return self.m
	
	
mul3 = Mul(3)
mul5 = Mul(5)

print(mul3.mul(10))
print(mul5.mul(10))
print(type(mul3))

print("="*50)
print(mul3(10))
print(mul5(10))
print(type(mul3))
print("="*50)
print(mul3(10), type(mul3),'n = ' , "" , 'm =', mul3.value())
