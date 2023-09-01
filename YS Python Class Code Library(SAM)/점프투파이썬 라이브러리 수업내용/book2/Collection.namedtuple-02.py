#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 10:25:08 2023

@author: sam
"""

#Collections.namedtuple 

from collections import namedtuple

#리스트에 튜플 요소를 3건 가지고 있다. 
data = [
		('홍길동', 23, "01022022020"),
		('김철수', 23, "01012024340"),
		('이영희', 18, "01022012345"),
]

print(type (data[1]))


#%%


# namedtuple ('대표이름', '첫번째, 요소 이름...)
Employee = namedtuple('Employee', 'name, age, cellphone')

print (type (Employee))

#%%
data = [Employee(emp[0], emp[1], emp[2]) for emp in data]

print(type(data))



"""
data2 = []
for emp in data:
	name , age, cellphone = emp 
	data2.append(Employee(name,age,cellphone))

data = data2 
print('data2 : ', data2)
"""
#%%

#기존방식 
print(" # 전체 출력 ")
for emp in data:
	name , age, cellphone = emp 
	print("name ", name)
	print('age :', age)
	print('cellphone :',cellphone)
	


#%%

emp = data [0]

print('emp:', type (emp))
print(emp.name)
print(emp.age)
print(emp.cellphone)

