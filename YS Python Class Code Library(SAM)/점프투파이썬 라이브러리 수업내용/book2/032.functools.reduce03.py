#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:02:59 2023

@author: sam
"""

from functools import reduce

#x : 결과값 , 누적잢
#y : iterable 가능한  데이터의 갱신값 

def maxvals(*args):
	return reduce(lambda x , y:  x if x > y else y , args)



#%%

data = [2,7,9,10,1] 


print("maxvals", maxvals(*data))
#%%

print("maxvals", maxvals(9,5,6,3,2))


#%%


#재귀호출 (자기 자신을 다시 호출)로 구현 해라 

def mymul(n):
	if n ==1:
		return n
	return n * mymul(n-1)
#%%

print(mymul(5))
	 
  

#%%	  

a = [1,2,3,4]

def myfunc2 (a):
	size = len(a)
	result = 0 
	if size ==(1):
		return result
	  
	  


#%%

print(myfunc2(2))