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

#dict 
#  형태 : "key" : value , ....
dict_data = {'a': 1, 'b': 2, 'c':3}
#시리즈는 일차원 형태임. (딕셔너리)
sr = pd.Series(dict_data)

print(sr)
print (type(sr))

#인덱스(index), 값(value)

 