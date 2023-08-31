#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:02:59 2023

@author: sam
"""

from functools import reduce

#x : 결과값 , 누적잢
#y : iterable 가능한  데이터의 갱신값 

def sumfunc(x,y):
	print(f"x({x}) , y({y})")
	return x+y


def mulfunc(x,y):
	print(f"x({x}) , y({y})")
	return x*y
#%%

data = [1,2,3,4,5] 

data2 = {2,4,6,8,10}

result = reduce(sumfunc,data)

print(result )


arr = [1,2]
result2 = reduce(sumfunc, arr)
print (result2)


#%%

result = reduce(mulfunc, data)
print(data, result)


result = reduce(mulfunc, data2)
print(data2, result)

