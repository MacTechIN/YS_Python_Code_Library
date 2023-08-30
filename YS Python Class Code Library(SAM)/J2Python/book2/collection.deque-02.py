#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:27:47 2023

@author: sam
"""

#collection.deque : 디큐 
# 양방향 자료형 
# 큐 (Queue) : FIFO (First in first out) 선입선출 
# 스텍 (Stake) : LIFO (Last in Fist out ) 후입선출 


from collections import deque 

a = [1,3,5,7,9]


q = deque(a)

print(q)

#%%

for r in q: #참조만 하기 때문에 데이터는 사라지지 않는다. 
	print(r)
	
print(q)

#%%


# pop() 꺼내면 기존 데이터 사라짐.
# 맨 마지막 데이터 : 9를 꺼내고 지움 
r = q.pop()
print("pop() : r= ", r, "deque = ", q )


#%%
# 뒤에서 부터 꺼낸다. 낸다. 

while q:
	r = q.pop()
	print(r)





