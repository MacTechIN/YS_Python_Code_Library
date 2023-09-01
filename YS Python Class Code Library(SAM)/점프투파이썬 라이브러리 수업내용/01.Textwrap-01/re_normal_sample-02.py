#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:43:08 2023

@author: sam
"""

data = """
홍길동의 주민번호는 800905-1049118 입니다. 
그리고 고길동의 주민번호는 700905-1059119 입니다.
그렇다면 누가 형님일까요?
"""

result = []
for line in data.split("\n"):
	print(">", line)
	word_result = []
	for word in line.split(" "):
		if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
			word = word[:6] + "-" + "*******"
			word_result.append(word)
			result.append(" ".join(word_result))
print("\n".join(result))

#%%

slst = data.split('\n')

print(len(slst))

#%%

result = []
for line in data.split('\n'):
	word_result=[]
	for word in line.split(" "):
		print(word) 
		if word == 14 and word[:6] and word[7:]:
			word = 


#%%

