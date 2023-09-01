#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 16:37:14 2023

@author: sam
"""

import datetime

today = datetime.date.today()

print(today)

#%%

#오늘부터 100일은 언제 ?
print("100일째는 ? ", today + datetime.timedelta(days=100))

#%%

sd = datetime.datetime(2023,7,21)
ed = datetime.datetime(2024,1,16)

td = ed - sd 
tt = (td/7) * 5 * 8

print(f"우리 수업일수 : 일수({td}), 시간({tt}) ") 

#%%





