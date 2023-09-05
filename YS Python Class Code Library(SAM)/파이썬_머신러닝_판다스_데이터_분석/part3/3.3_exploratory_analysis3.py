# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg1.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

#%%

print(df[0:9].mean(axis=1))

#%%
## Name drop(삭제) 시킴 
df.drop('name', axis=1, inplace=True)
#%%

print(df.mean())
# 전체 평균값 
#%%

for x in range(len(df.columns)-1):
	cols = df.iloc[ :,x]
print('\n')

#%%

#horsepower 

print(df['horsepower'].mean())


#%%

print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')

#%%
#필요한 컬럼만뽑아서 평균값 구하기 , 리스트[] 로 만들어야함.  

print(df[['mpg','weight']].mean())

#%%

# 중간값 
print(df.median())
print('\n')
print(df['mpg'].median())
#%%

# 최대값 
print(df.max())
print('\n')
print(df['mpg'].max())
#%%
# 최소값 
print(df.min())
print('\n')
print(df['mpg'].min())
#%%
# 표준편차 
print(df.std())
print('\n')
print(df['mpg'].std())
#%%
# 상관계수 
print(df.corr())
print('\n')

print(df[['mpg','weight']].corr())