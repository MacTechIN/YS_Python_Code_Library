#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 10:02:59 2023

@author: sam
"""

from functools import reduce

#x : 결과값 , 누적잢
#y : iterable 가능한  데이터의 갱신값 

def maxfunc(x,y):
	print(f"x({x}) , y({y})")
	return x if x > y else y 

#%%

data = [2,7,9,10,1] 


result  = reduce(maxfunc, data)
print( data, result )

#%%

import random 
 
data = [x for x in range(11)]
 
random.shuffle(data)
 
print ("*"* 20)
print(data)
print ("*"* 20)
 
r  = reduce(maxfunc, data)
print( data, r)

 



