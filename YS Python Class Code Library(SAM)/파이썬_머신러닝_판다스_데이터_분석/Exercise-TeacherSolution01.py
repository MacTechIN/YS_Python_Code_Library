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



import pandas as pd 

exam_data = {'이름' : ['서준', '우현','인아'],
			 '수학' : [90, 80, 70],
			 '영어' : [98, 89, 95],
			 '음악' : [85, 95,100],
			 '체육' : [100, 90, 90]}

# 1. DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장 

df = pd.DataFrame(exam_data)
print("df : \n" )
print(df)

#%%
# 2.df를 인덱스를 이름으로 선택 
ndf = df.set_index("이름")


print(ndf)

cnt = len(ndf.columns) # 총 컬럼 의 갯수 
sr = ndf.loc[:, '수학':'체육']

print(sr)

#컬럼추가 

ndf['총점'] = 0 
ndf['평균'] = 0 

print(ndf)


#%%

print("#학생별 총점 및 평균")

for x in range(len(ndf)): # 행의 갯수 
	rows = ndf.iloc[x, :] #하나의 행을 추출 
	tot = 0 
	cnt = 0 
	for val in rows:
		tot += val
		cnt += 1 
	ndf.iloc[x,4] = tot #총점 
	ndf.iloc[x,5] = tot // cnt #평균값
	
print(ndf)



#%%

print("Solution 3")

for x in range(len(ndf)):  # 총 행의 갯수 
	rows = ndf.iloc[x, : ]
	tot = rows.sum()
	ndf.iloc[x,4] = tot
	ndf.iloc[x,5] = tot//cnt
	

#%%

rowcnt = len(ndf)
ndf.loc['총점'] = 0 
ndf.loc['평균'] = 0 

print("")
