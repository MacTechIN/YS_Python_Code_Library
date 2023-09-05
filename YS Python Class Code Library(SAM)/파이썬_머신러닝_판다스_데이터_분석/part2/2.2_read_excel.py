# -*- coding: utf-8 -*-
#pip install openpyxl 설치요망 

import pandas as pd

# read_excel() 함수로 데이터프레임 변환 
df1 = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl')            # header=0 (default 옵션)
df2 = pd.read_excel('./남북한발전전력량.xlsx', engine='openpyxl', 
                    header=None)  # header=None 옵션

# 데이터프레임 출력
print(df1)
print('\n')
print(df2)