# -*- coding: utf-8 -*-

import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
#%%
# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인 
print(df.count()) #Series
print('\n')

#Type : seriese 
print(type(df.count()))

#%%

# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))
print('\n')

#%%
# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인 

unique_values = df['origin'].value_counts() 


print(unique_values)
print('\n')

print(unique_values.sum()) # 총갯수

#%%
# value_counts 메소드가 반환하는 객체 타입 출력

print(type(unique_values))


#%%
#cylinders 칼럼의 값들의 갯수 

cylinder_values = df['cylinders'].value_counts() 

print(cylinder_values)

print("cylinder_values total : ", cylinder_values.sum())

#%%

origin = df['origin']
print(origin)

for item in origin :
	print(item)




