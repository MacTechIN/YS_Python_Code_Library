#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:56:35 2023

@author: sam
"""
#판다스
#conda activate YSIT2023 (각자 다름)
# pip install pandas 


import pandas as pd 

#list ....
list_data = ['2023-0901',3.14,'ABC',100,True]

#Default index 는 정수형 위치 인덱스 : 0,1,2,3...
sr = pd.Series(list_data)

print(sr)
print (type(sr))

#인덱스(index), 값(value)

 #%%

#index 는 ranges 와 동일하다 
print("index : ", sr.index) # RangeIndex(start=0, stop=5, step=1)
print("values :", sr.values) # ['2023-0901' 3.14 'ABC' 100 True]


 
 