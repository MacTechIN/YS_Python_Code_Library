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
print("df : \n" )
print(df)

df2 = df.set_index('이름', inplace=False)


print("df2 : \n" )
print(df2)
print('\n')

def get_member (member):
	name=[]
	for item in df2.index:
		name.append(item)
	return name
student_list = get_member(df2)
print(student_list)


#%%
##각학생의 평균및 총점 구하는 함수 정의 

def mysum(score):
	sum = 0 
	for i in score:
		sum+=i
	return int(sum) 

def myave(score):
	sum=0
	coun = 0 
	for i in score:
		sum+=i
		coun += 1
	return int(sum/coun) 


#%%
def score_list(sl):
	df3 = []
	for i in range(len(sl)):
		temp = df2.loc[sl[i]]
		df2['총점'] = mysum(temp)
		df2['평균'] = myave(temp)
		df3.append(temp)
	return df3
	
		

temp_list = score_list(student_list)

df4 = pd.DataFrame(temp_list)


print("result : \n")
print(df4)


"""
b = df.iloc[0, 0]
		 print(b)
		 print('\n')

"""

#%%
# 행 인덱스를 사용하여 행 1개를 선택

select_sj = df2.loc['서준']
print([select_sj]) 
print(type([select_sj]))
sum = mysum(select_sj)
ave = myave(select_sj)
print("서준 총점:" , sum)
print("서준 평규 : ", ave)

#%%
#상기 내용을 바탕으로 전체 df2에 대한 루프를 만들면 아래와 같다 



