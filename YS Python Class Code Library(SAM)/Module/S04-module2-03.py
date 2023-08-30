#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:10:59 2023

@author: sam
"""
 
#모듈 파이썬 확장자 .py 생략함. 
#mod1.py 

from mod3 import add, sub, PI, Math

radius = 75
a = 100
b = 200 


#함수더하기 
a1 = add(a,b)
b1 = sub(a,b)


print("PI : " ,PI)

print(f"add({a}, {b}) -> {add(a,b)}")
print(f"add({a}, {b}) -> {sub(a,b)}")

print (f"원에 넓이({radius}) -> {Math.circlearea(radius)}")

#%%
