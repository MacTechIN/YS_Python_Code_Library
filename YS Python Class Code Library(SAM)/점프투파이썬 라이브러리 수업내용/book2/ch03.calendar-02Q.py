#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:54:18 2023

@author: sam
"""


#윤년 
#calendar.isleap 


import datetime
import calendar

year = 2020
#year = 2022 #윤년 
isleap = calendar.isleap(year)

tfleap = "윤년" if isleap else "평년"

print(f"({year})년은 {tfleap}입니다.")

#%%

# 2020 = 윤년

#문제 함수 isleap2(연도)를 만들어 
#조건 : 윤년이면 true, 평년이면 False 리턴 
"""
1. 윤년은 4년에 한번씩 온다.
2. 100년에 한 번씩 안온다.
3. 400년에 한번 씩 온다. 

기원1년 , 4, 8...... 100(평년) 1년, 4, ~~~~~ 100년, * 4 1년째 온다 

 

"""

year = "2020"



def isleap2(year):	
	 return False if year%400==400 else False if year%100==100 else False if year%4==0 else True


print(isleap2(2024))

#%%

result = []

for i in range(1000):
	if i%4 == 0:
		result.append(i)
		
print(result)
print("="*20)

for leap in result:
	if leap%100 and leap%400:
		break

		
		
print(result)	
		
	
	



#%%
import calendar

real = []

for i in range(1000):
	if calendar.isleap(i):
		real.append(i)
		
		
print("real isleap is ", real)

print('*' * 40)

#%%

my_real = []

for i in range(100):
	if isleap2(i):
		my_real.append(i)
		
		
print("my_real isleap is ", my_real)

#%%

c = list(set(real) - set(my_real))
d = list (set(my_real)- set(real))

print(c==d)
