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

mul3 = mul(n=3) #3을 곱하는 함수 
mul5 = mul(n=5) #5를 곱하는 함수 


print(mul3(n=10)) # 30 = 3 * 10 
print(mul5(n=10)) # 50 = 5 * 10 

#mul 함수가 한개이지만, 이 것을 mul3, mul5 숫자에 맞도록 함수를 만들언 놓고 사용 하려는 목적임.


#%%
a= 2
print(mul(a))
