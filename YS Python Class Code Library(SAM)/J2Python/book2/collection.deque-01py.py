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

a = [1,2,3,4,5]

print ("ID of a :", id(a))

q = deque(a)  # deque 한 결과를 보관  

#시계방향 회전 
print(q.rotate(2)) # 회전 시키고 

print(q,id(q))

result = list(q)


print("dequeue result: ", result )


#%%

q.rotate(-2)

print(q, id(q))
r = list (q)

print ("original list : ", r, id(r))


