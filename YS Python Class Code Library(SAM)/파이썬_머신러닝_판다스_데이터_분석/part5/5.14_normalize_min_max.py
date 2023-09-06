# -*- coding: utf-8 -*-

#정규화 (Normalization)- min, max chart 

#각 열에 속하는 데이터 값을 동일한 크기 기준으로 나누 비율을 나타냄 

#0~1 , -1~0



# 라이브러리 불러오기
import pandas as pd
import numpy as np

#정규화 (normalization)
#각 열에 속하는 데ㅣ터 값을 동일한 크기 기준으로 나눈 비율로 나타냄 
#값 : horsepower
#데이터 범위 : 0~1,
#범위 : (값-최소값) / (최대값 - 최소값)
#horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장 



# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

df2 = df 
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']  

# horsepower 열의 누락 데이터('?') 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df['horsepower'] = df['horsepower'].astype('float')      # 문자열을 실수형으로 변환
	
df2['horsepower'].replace('?', np.nan, inplace=True)      # '?'을 np.nan으로 변경
df2.dropna(subset=['horsepower'], axis=0, inplace=True)   # 누락데이터 행을 삭제
df2['horsepower'] = df2['horsepower'].astype('float')

  
# horsepower 열의 통계 요약정보로 최대값(max)과 최소값(min)을 확인
print(df.horsepower.describe())
print('\n')

#%%
#no13 data 

df2.horsepower = df2.horsepower / abs(df2.horsepower.max()) 

print(df2.horsepower)
print('\n')
print(df2.horsepower.describe())

















#%%
# 최대값 : 1 
# horsepower : 열의  
# horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
min_x = df.horsepower - df.horsepower.min()

print(min_x)
#%%

min_max = df.horsepower.max() - df.horsepower.min()

df.horsepower2 = min_x / min_max

print(df.horsepower2.head())
print('\n')
print(df.horsepower2.describe())


#%%

# df['horsepower'] 데이터를 이용하여 차트를 그려라

import matplotlib as plt 





