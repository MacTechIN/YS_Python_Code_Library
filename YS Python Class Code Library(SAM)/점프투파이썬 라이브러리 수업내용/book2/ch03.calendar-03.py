#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:54:18 2023

@author: sam
"""


#윤년 
#calendar.isleap 


#import datetime
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

def isleap2(year):	
	 return True if year%400 == 0 else False if year%100 == 0 else True if year%4==0 else False 
 
for year in range(1,5000):
	if calendar.isleap(year) != isleap2(year):
		print( "오차발생 real = " ,year)
		break 
else :
	print("완벽합니다.")
	
#%%

def isLeap2(year):
	if year % 4 == 0  and (year %100 != 0 or year % 400 ==0):
		return True
	else :
		return False

print(isleap2(2002)) 

#%%


def isleap3(year):
	if year % 4 == 0 :
		if year % 100 != 0 or year % 400 == 0 :
			return True 
		else:
			return False
	else:
		return False

print(isleap3(2002)) 



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

print("1600yr is leap ?", calendar.isleap(3000))	

year = range(1,1220)
temp1 = []

temp3 = []

for i in year:
	if  (i%4 == 0 and (x%100 == 0)) or (x%200 == 0) or (x%300 == 0):
		temp1.append(i)		
print("temp1:", temp1)
#%%

# 4로 나눠지지만 100 으로 나눠지면 제외시키기 

arr1 = range(1,200)
t1 = []

for x in arr1:
	if x%4 == 0 : 
		t1.append(x)

t2 = []
for x in range(len(t1)):
		a = t1[x]
		if a%100 == 0:
		

#%%
			
def removetiem(lst[], item):
	temp=[]
	for i in lst:
		if i != item:
			temp.append(i)
	return temp 

testlist = [10,20,30,40,50]

test = removetiem(testlist,20)
p


		
	 
	


#%%
t2=[]

for y in arr1:
	if x%4
		t2.append(x)
print(t2)

#%%


temp2 = []
year2 = range (1,1220)

for i in year:
	if calendar.isleap(i) is True:
		temp2.append(i)

print("Real Leap Year :" , temp2)

#%%


for x in temp:
	if (x%100 == 0) or (x%200 == 0) or (x%300 == 0):
		leapyear1.append(x)
print("leap1 :". leapyear1)

for y in leapyear1:
	if y%400 == 0 :
		leapyear2.append(y)
		 
print(leapyear2)
		  





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


#%%
# rhwo 
