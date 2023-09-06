# -*- coding: utf-8 -*-
# 누락 데이터 지움 
# df_thresh = df.dropna(axis=1, thresh=500) 

# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
#%%

# for 반복문으로 각 열의 NaN 개수 계산하기
# 유효하지 않은 데이터는 True 가됨.  유효한 데이터는 False 

missing_df = df.isnull() # T or F


#%%
col = 'age'
missing_count = missing_df[col].value_counts()  



#%%
# 'deck' 


col = 'deck'  
missing_count = missing_df[col].value_counts()  #
print(missing_count)

#%%

col = 'who'  
missing_count = missing_df[col].value_counts()  #
print(col, ':', missing_count[False])



#%%

for col in missing_df.columns:  # 컬럼을 하나씩 꺼내와서 
    missing_count = missing_df[col].value_counts()    # 각 열의 NaN 개수 파악
    try: 
        print(col, ' : ', missing_count[True])   # NaN 값이 있으면 개수를 출력
    except:
        print(col, ' : ', 0)                     # NaN 값이 없으면 0개 출력
   
#%%	
	   
# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500, inplace=True)  

print(df_thresh.columns)

"""
ndex(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive',
       'alone'],
      dtype='object')  # deck 삭제 ***

"""
#%%

# 만약 axis 가 0 (행) 이면 전체 삭제 
df_thresh = df.dropna(axis=0, thresh=100, inplace = True)  

print(df_thresh.columns)


#%%

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
# age 열(891 중 177개의NaN 값) 
# how= 'any' : 하나라도 존재하면 삭제 
df_age = df.dropna(subset=['age'], how='any', axis=0)  
print(len(df_age))

#%%
# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
# age 열(891 중 177개의NaN 값) 
# how= 'any' :  age , deck 양쪽 하나라도 존재하면 삭제
# how = 'all' : age , deck 양쪽 모두 NaN이면 삭제 
 
df_age = df.dropna(subset=['age','deck'], how='any', axis=0)  
print(len(df_age))
