#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:01:24 2023

@author: sam
"""

#리스트 연산 : sort , reverse 

#%%
a = [9,6,2,5,4,1,3,8,7]

print ("원본 : ", a)

a.reverse() 
print('그냥뒤집기 : ' , a )

##오름차순으로 정렬 
a.sort()
print('오름차순 : ' , a)

#내림차순으로 정렬 
a.reverse()
print('내림차순 : ', a)