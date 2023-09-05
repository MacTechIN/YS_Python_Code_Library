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
print('count1 :', df.count()) #전체 데이터 행 기준으로 갯수 
print(df[:].count()) # 전체 행에 대해서 갯수 
print(df[:].mean()) #전체 행에 대해서 평균

#%%
#행의 범위에 대해서 갯수 
# 즉  8건 
print(df[10:12])
print('count2 :', df[10:12].count())


#%%

print(df.iloc[:,:0]) #전체행에서 0번째 컬럼만 선택 함. 
print(df.iloc[:,:1]) #전체행에서 0번째 컬럼만 선택 함. 

#%%

#전체 행에서 부터 0부터 8번째 까지의 칼럼 선택 
print(df.iloc[:,:8])
print(df.iloc[:,:8].mean().mean)


#%%

#행 10부터 14번까지 중에 1,2번째 행만 보여라 
print(df[10:15][1:3])

#%%

for x in range(len(df.columns)-1):
	col = df.iloc[x]
	print(col, ':' , df[col].mean())

print('\n')

#%%

#평균값 : horsepower 칼럼을 제외하고 평균 

print (df.iloc[:, 0:3].mean(), '\n' ,df.iloc[:, 4:7].mean())


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