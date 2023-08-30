#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:28:59 2023

@author: sam
"""

#dict : 사전형 

#{Key : Value}
#특징 : 1. 검색(탐색)속도가 빠름, 2,처리용량을 많이 차지 한다. 3.순차검색속도가 느리다.
#키는 변하지 않는 값을 사용해야한다. 
#키로 리스트는 사용할수 없다. ㅅ
#Tuple 는 사용할수 있다. 

#빈 딕셔너리 생성 

dt = {}

print(type (dt)) #<class "dict>


#%%

dt = { "title" : "파이선의 이해 ",
	  "Author" : "파이선",
	  "content" : "파이선은 자유롭다" } 

print(dt)


#키를 이용하여 Value 값을변경
dt['title'] = "파이썬의 문법 "	
		
print (dt)



	
#%%

#값이 없으면 
#KeyError : '타이틀'

# print(dt['title2']) #KeyError: 'title2'

# 없는 키를 넣으면 새로 추가 됨. 
dt['타이틀'] = "파이썬 이해"

print(dt['타이틀']) #KeyError: 'title2'

#%%
#삭제

del dt['타이틀']

# print (dt[타이틀]) NameError: name '타이틀' is not defined