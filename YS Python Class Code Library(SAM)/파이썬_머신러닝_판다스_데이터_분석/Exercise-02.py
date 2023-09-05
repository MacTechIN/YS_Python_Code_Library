#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 09:03:30 2023

@author: sam
"""

"""
[문제] 아래의 데이터프레임을 이용하여 총점과 평균을 구하라 

1. '이름'을 인덱스로 지정
2. 각 학생의 총점 과 평균  
3. 각 과목별 총점과 평균 
4. 전체를 새로운 하나의 데이터 프레임으로 구성 


"""

#%%

#  DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장 

import pandas as pd 

exam_data = {'이름' : ['서준', '우현','인아'],
			 '수학' : [90, 80, 70],
			 '영어' : [98, 89, 95],
			 '음악' : [85, 95,100],
			 '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print("df : " )
print(df)

df2 = df.set_index('이름', inplace=False)

print("\n")

print("df2 :" )
print(df2)
print('\n')


#%%
# 총 

#%%
#상기 내용을 바탕으로 전체 df2에 대한 루프를 만들면 아래와 같다 



