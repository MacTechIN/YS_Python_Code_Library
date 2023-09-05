#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 15:56:35 2023

@author: sam
"""
#판다스


import pandas as pd 

#tuple..
tuple_data = ('길동', '2023-09-01','남',True)
#%%
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

#%%
print (sr['이름'])
print (sr.loc['이름'])
 
 #%%

#원수 : index로 직접 접근  
print (sr[0]) # 권고하지 않는다. : 경고 index  FutureWarning: Series.__getitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To access a value by position, use `ser.iloc[pos]`

#%%

#
print(sr.iloc[0]) # iloc로 접근으로 사용하기 바람. 

#%%
#인덱스를 활용하여 여러 원소 선택하기 

print(sr[[1,2,3]]) #권장하지 않음. 


#%%

#튜플은 지원하지 않음. 
print (sr[('이름','생년월일','성별','학생여부')])


#%%

# 범위를 지정하여 원소 선텍 
# 판다스만읜 일반적 형태일 리스트와 나옴. 
# List 의 slice 처럼 범위를 지정하여 진정된 마지막 인덱스 포함. 
# '생년월일'부터 '학생여부'까지 
print(sr['생년월일':'학생여부'])

