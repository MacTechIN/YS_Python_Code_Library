# -*- coding: utf-8 -*-

import pandas as pd

# 딕셔서리를 정의
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
print('\n')

# c1 열을 기준으로 내림차순 정렬 
ndf = df.sort_values(by='c1', ascending=False)
print(ndf)