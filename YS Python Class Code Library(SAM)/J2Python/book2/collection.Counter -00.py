#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:15:32 2023

@author: sam
"""

import re
from collections import Counter

data = """
산에는 꽃 피네.
꽃이 피네.
갈 봄 여름없이
꽃이 피네.

산에
산에
피는 꽃은
저만치 혼자서 피어있네.

산에서 우는 새여
꽃이 좋아
산에서
사노라네.

산에는 꽃지네
꽃이 지네.
갈 봄 여름 없이
꽃이 지네.
"""

words =  re.findall(r'\w+', data)


#%%
words = data.split('\n') 

words2 = []
for wn in words:
	ws = wn.split(' ')
	for w in ws :
		s1 = w.strip('.')
		if s1 != "":
			words2.append(s1)

print(words2)

#%%
count = 0 
for i in words2:
	count += 1 

print ("Total Words count is ", count)

#%%

counter = Counter(words2)
print(counter.most_common(1)) # 빈도갑은 최상위 1개 



#%%

words2 = sorted(words)
print(words2)


#%%
print(counter.most_common(5)) #빈도값은 최상위 5개

#%%
count =   0 
for word in words:
	if word == "산에서":
		count += 1
		
		
print(count)
	
