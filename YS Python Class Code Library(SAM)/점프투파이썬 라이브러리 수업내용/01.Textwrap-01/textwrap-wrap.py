#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:00:29 2023

@author: sam
"""


import textwrap

textwrap.shorten("Life is too short, you need python", 20 , placeholder ="[!!!]")

#결과 : 'Life is [...]' 

#%%

kor_text = "'한글은어떻게 표현되어야 하는가요?"

textwrap.wrap(kor_text,width=15)

#%%
import textwrap
longText = "Life is too short, you need python. " * 10

result = textwrap.wrap(longText, width = 70)
print("result len", len (result), type(result))

print(result)

#%%

for lst in result:
	print(lst)

#%%

#result 결과를 line feed 단위로 출력 

lineFeedResult = "\n".join(result)

print(lineFeedResult)



#%%

result2 = textwrap.fill(longText, width=70)
print(result2)