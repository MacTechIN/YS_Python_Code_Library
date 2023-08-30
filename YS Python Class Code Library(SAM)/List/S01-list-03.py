#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:01:24 2023

@author: sam
"""

#리스트의 요소에 다른 리스트를 저장 

e = [1,2, ['Life', 'is']]

print(e)

print (e[0])
print (e[1])
print (e[2]) #[;life,'is']
print (e[-1]) #[;life,'is']



#%%

print(e[2][0]) #'life' 
print(e[2][1]) #'is' 


#%%

ex = e[-1]
print(ex[0])
print(ex[1])
#변수로 받아 사용하면 편하다 
#교재 P-79

