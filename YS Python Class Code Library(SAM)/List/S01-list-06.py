#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:01:24 2023

@author: sam
"""

e= [1,2,['life','is']]
print(e, id(e))

#%%
#e[-1] 의 요소를 참조 
ex = e[-1]
ex[0]=99

print(ex,id(ex))
print(e)

#새로운 리스트 메모리를 참조 
print("새로운 리스트 메모리를 참조 ")
ex= [10,20,30]
print(ex,id(ex))

print("e와 ex는  관계가 끊김")

ex[-1] = 'ex'
print(ex, id(ex))

#e는 변화가 없다. 
print(e, id(e))

#%%




