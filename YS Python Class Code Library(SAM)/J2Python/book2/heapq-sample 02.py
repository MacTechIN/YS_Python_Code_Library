#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 12:22:01 2023

@author: sam
"""

#우선 순위 Queue

import heapq

data = [
    (12.23, "강보람"),
    (12.31, "김지원"),
    (11.98, "박시우"),
    (11.99, "장준혁"),
    (11.67, "차정웅"),
    (12.02, "박중수"),
    (11.57, "차동현"),
    (12.04, "고미숙"),
    (11.92, "한시우"),
    (12.22, "이민석"),
]

print(type(data[0]))

#오름차순으로 지정된 수만 꺼냄 
print(heapq.nsmallest(2, data))

#%%
l = len(data)
print(heapq.nsmallest(l, data))

h = []

for score in data:
	heapq.heappush(h, score)

#%%
#[주의] heappush() 를 사용하지 않는 리스트를 heappop() 을 사용하지 말라 

heapq.heapify(data) # heapqg화 시킨다. 

for x in range(l):
	print(heapq.heappop(data))
	
print(data)

#%%
lh  = len(h)


ranking = []

for x in range(lh):
	ranking.append(heapq.heappop(h))  # 꺼내고 삭제 

print("h", h)
print("Total Ranking : ", ranking  )

#%%

