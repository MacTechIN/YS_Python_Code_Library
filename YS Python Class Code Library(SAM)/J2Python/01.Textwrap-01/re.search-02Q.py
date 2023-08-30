#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 소문자로 시작하고 공백 문자까지포함 
"""
Created on Tue Aug 29 11:08:59 2023

@author: sam
"""
#정규식 
#%%
import re


#p = re.compile("\d+[-/.]\d+[-/.]\d+")

p2 = re.compile("\d+[-/.]\d+[-/.]\d+")
p = re.compile("[0-9.\-/]+")
p3 = re.compile("\\[0-9]+[-][0-9]+[-][0-9]+\\")


s1 = '[2023-08-29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s2 = '[2023/08/29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s3 = '[23/08/29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s4 = '[23.08.29 10:15:31:009][WARN] 교환장비 통신 장애 발생'


strlist = [s1,s2,s3,s4]
print ("Using patter is ", p2)
for s in strlist:
	m= p3.search(s)
	if m!=None:
		print('m.span: ', m.span(), type(m.span())) #<class 'tuple'>
		sp, ep = m.span() #시작위치, 마지막위치 
		print(f"매치된 문자열: ({s[sp:ep]})")
#%%

import re


#p = re.compile("\\[\d+[-]\d+[-]\d+\\]")
#p = re.compile("\\[\d{4}[-]\d{2}[1]\d{2}\\]")
#p = re.compile("\\[\d{2,4}[-]\d{2}[-]\d{2}\\")
#p = re.compile("\\[(\d{2}|\d{4})[./-]\d{2}[./-]\d{2}\\]")
#p = re.compile("\\[(\d{2}|\d{4})[./-]\d{2}[./-]\d{2}\\]")


# \\ -> "\"문자로 인식  


#p2 = re.compile("\d+[-/.]\d+[-/.]\d+")
#p = re.compile("[0-9.\-/]+")
#p3 = re.compile("\\[0-9]+[-][0-9]+[-][0-9]+\\")

p = re.compile("\w+")


#<시식의 조건>
#일자 : 대괄호([]) 감싸 있어야 한다
#년 : 2자리 또는 4자리 
#월 : 2자리 
#일 : 2자리 
s1 = '(2023-08-20) 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s2 = '[2023/08/30] [10:15:31:009][WARN] 교환장비 통신 장애 발생'
s3 = '[23/08/29] [10:15:31:009][WARN] 교환장비 통신 장애 발생'
s4 = '[23.08.29] 10:15:31:009][WARN] 교환장비 통신 장애 발생'


strlist = [s1,s2,s3,s4]

print ("Using patter is ", p)
for s in strlist:
	m= p.search(s)
	if m!=None:
		print('m.span: ', m.span(), type(m.span())) #<class 'tuple'>
		sp, ep = m.span() #시작위치, 마지막위치 
		print(f"매치된 문자열: ({s[sp:ep]})")


#%%
## 위에 re 조건문을 바꾸면

p = re.compile("[]0-9]+[-/.][0-9]+[-/.][0-9]")

s1 = '[2023-08-29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s2 = '[2023/08/29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
s3 = '[23/08/29 10:15:31:009][WARN] 교환장비 통신 장애 발생'


strlist = [s1,s2,s3]

for s in strlist:
	m= p.search(s)
	if m!=None:
		print('m.span: ', m.span(), type(m.span())) #<class 'tuple'>
		sp, ep = m.span() #시작위치, 마지막위치 
		print(f"매치된 문자열: ({s[sp:ep]})")


	
#%%
s = '[2023-08-29 10:15:31:009][WARN] 교환장비 통신 장애 발생'

p = re.compile("\d+-[-]\d+[-]\d+")

m = p.search(s)

if m  !=None:
	print('m.span: ', m.span(), type(m.span()))
	sp, ep = m.span()
	print(f"매치된 문자열: ({s[sp:ep]})")
	


#%%

s = '[2023-08-29 10:15:31:009][WARN] 교환장비 통신 장애 발생'

p = re.compile("[0-9]+\s")

result = []
myStr = ''


m= p.findall(s)

for i in m:
	result.append(i)
	
for x in result:
	myStr += " " + x

print(myStr)

#%%
s = '[2023-08-29 10:15:31:009][WARN] 교환장비 통신 장애 발생'
p = re.compile("\w+")
m = p.findall(s)

str =[]

for i in m:
	print(i, type(i))

#%%	
str = "test"
print(str.len)
