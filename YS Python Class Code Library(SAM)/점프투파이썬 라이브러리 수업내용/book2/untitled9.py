#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:29:01 2023

@author: sam
"""

#enum 
# 상수집합 : 열거형 상수 
# 상수 형태 문자 

from datetime import date
from enum import IntEnum

## class 멤버 변수 의 형태 

class Week(IntEnum()):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

#%%

def get_menu(input_date):
	menu = {
        Week.MONDAY: "김치찌개",
        Week.TUESDAY: "비빔밥",
        Week.WEDNESDAY: "된장찌개",
        Week.THURSDAY: "불고기",
        Week.FRIDAY: "갈비탕",
        Week.SATURDAY: "라면",
        Week.SUNDAY: "건빵",
	}
	
	print(input_date ,": 요일 = " , input_date.isoweekday())
	return menu[input_date.isoweekday()]

#%%
print(get_menu(date(2023,7,30)))
print(get_menu(date.today()))


#%%

for week in Week:
	print("{}:{}".format(week.name, week.value))
	
	#%%
	
print("Sunday : {}:[]".format)