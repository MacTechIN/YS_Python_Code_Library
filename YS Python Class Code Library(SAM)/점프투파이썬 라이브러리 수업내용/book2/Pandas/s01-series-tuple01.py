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

#tuple..
tuple_data = ('길동', '2023-09-01','남',True)

#Default index 는 정수형 위치 인덱스 : 0,1,2,3...
#인덱스 부여시 적용 할수 있음 * 데이터와 인덱스는 숫자가 맞아야함. 
sr = pd.Series(tuple_data, index = ['이름', '생년월일', '성별', '학생여부'])

print(sr)
print (type(sr))

#인덱스(index), 값(value)

 #%%

#index 는 ranges 와 동일하다 
print("index : ", sr.index) # Index(['이름', '생년월일', '성별', '학생여부'], dtype='object')
print("values :", sr.values) # ['길동' '2023-09-01' '남' True]


 
 