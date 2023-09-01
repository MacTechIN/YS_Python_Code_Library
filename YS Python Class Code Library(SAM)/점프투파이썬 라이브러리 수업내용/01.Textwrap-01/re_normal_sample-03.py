#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:43:08 2023

@author: sam
"""



##정규식 이용 

import re 

#%%
# 알파벳 소문자 a ~ z 까지 임의의 문자가 한번이라도 나오는 패턴을 찾아라 
# 문자열의 처음부터 
p = re.compile("[a-z]+")

s= "hello world"

m= p.match(s)
if m != None:
	print("m.span(영역) : ", m.span(), "m.span 타입: ", type(m.span()))
	sp, ep = m.span()
	print("매치된문자열 : ", s[sp:ep])

#%%

p = re.compile("[a-zA-z, ]+")

s ='Hello Word!1234'

m = p.match(s)

if m !=None:
	i , j = m.span() 
	print("Matched Words: " , s[i:j] )