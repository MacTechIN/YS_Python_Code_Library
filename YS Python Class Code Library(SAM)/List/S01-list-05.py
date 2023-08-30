#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 14:01:24 2023

@author: sam
"""

e= [1,2,['life','is']]

ex = e[-1]
print(ex[0])
print(ex[1])
#변수로 받아 사용하면 편하다 
#교재 P-79

#%%

#리스트 e의 마지막 요소를 새로운 변수로 참조한 후 
#변경하면 ? 

ex[0] = 'Go'
ex[1] = 'On'

print(ex,id(ex))
print(e,id(ex))

#%%

#리스트안의 리스트 요소를 새로운 내용으로 변경 하면 
#기존 그 요소를 가리키고 있는 변수는 ? 

e[-1] = [10,20,30]

print(e, id(e))
print(e[-1], id(e[-1]))

#새로 바뀌기 전의 내용을 가지고 있다. 
print(ex, id(ex))

ex[0] = 99

print(ex,id(ex))

#%%




