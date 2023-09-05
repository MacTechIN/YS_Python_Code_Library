#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 16:55:54 2023

@author: sam
"""

# 판다스
# 데이터 프레임 : DF DATA FRAME
# 2차원 배열, 행/렬 (matrix)
# 행 : 인덱스 , row index
# 열 : column , Series 

#%%

#dict 
# 키는 열 이름 

import pandas  as pd 

data = { 
		 'c0' : [1,2,3,], # 컬럼, 시리즈 
		 'c1' : [4,5,6,], # 컬럼, 시리즈
		 'c2' : [7,8,9], # 컬럼, 시리즈
		 'c3' : [10,11,12], # 컬럼, 시리즈
		 'c4' : [13,14,15]	 # 컬럼, 시리즈	
}


df = pd.DataFrame(data, index =['첫번째','두번째','세번째'])
print(type(df)) # <class 'pandas.core.frame.DataFrame'>

#디폴트 
print (df)

#출력
"""
   c0  c1  c2  c3  c4
0   1   4   7  10  13
1   2   5   8  11  14
2   3   6   9  12  15

"""
