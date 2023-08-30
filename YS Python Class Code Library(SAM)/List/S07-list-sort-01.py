#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:01:24 2023

@author: sam
"""

#리스트 연산 
#리스트 추가 하기 
#순서가 유지 된다 ^^ 

a = [1,3,5]

a.append(7) 

print(a)


#%%

x = [1,2,3,4,5]
y = []
z = 3
for i in x :
	   y.append(i*3) 
	
print(y)


#%%



def mullist(x, z):
	y = []
	for i in x :
		y.append(i*z)
		
	return y


print(mullist(x,2))


