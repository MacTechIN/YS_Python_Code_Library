#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 17:09:42 2023

@author: sam
"""

import pandas as pd


# list 
# 리스트의 2차원 배열 형태는 행 , 열 

data = [
	[15, '남', '덕영중'], #준서
	[17, '여', '수리중']  #예은 
]

df = pd.DataFrame(data, 
				  index=['준서','예은'], 
				  columns= ['나이','성별','학교'])

df2 = pd.DataFrame(data)    



print(df)

print(df2)
#%%

#인넥스와 열이름을 변경 

df.index = ['학생1','학생2']
df.columns = ['age', 'Gd','School']

print (df)

#%%
#인덱스와 열이름을 일부 변경 

df2= df.rename (index = {"학생1":"시웅"})

print(df2)

#%%

df2= df.rename (index = {"학생1":"시웅"} , columns={"age":"연세"})

print(df2)

#%%
#인덱스와 열이름을 이부 변경 
# inplace = True 

df3 = df2.rename(columns= {"연세": "춘추"}, inplace= True)

print('사본', df3)
print('원본', df2)


#%%

#행 / 열 / 삭제 

# 행삭제 :  axis = 0 
	
df4 = df2.drop('시웅',axis=0)
print(df4) 

# 열삭제 : axis = 1
df5 = df4.drop('School',axis=1)
print(df5) 

#%%
