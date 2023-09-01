#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:45:23 2023

@author: sam
"""

from collections import defaultdict

#문자열의 각문자를 딕셔러리로 키로 만들고 
#각 문자에 빈도수를 값으로 지정 

text = "Life is too short, You need to pyhon"

d = defaultdict(int)

for c in text:
	d[c] += 1 

print(dict(d))

print("-" * 100)

#%%
d1 = dict()
print(type(d))
for key in text:
	if key not in d1:
		d1[key] =0 
	d1[key] += 1
	

print (d1)
print("-" * 100)
	
#%%

#0으로 최기화 

dd = defaultdict(int)

## <class 'collections.defaultdict'> defaultdict(<class 'int'>, {})
print(type(dd), dd)

# 참조해서 해당하는 키가 없으면, 키에 해당하는 키를 생성하고 값은 0으로 초기화 
for c in text:
	## dd[c] = dd[c] + 1
	dd[c]+= 1

print(dict(dd))

#%%
