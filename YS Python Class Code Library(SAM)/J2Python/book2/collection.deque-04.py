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

#%%

#디큐와 리스트의 차이 
from collections import deque 

lst = [1,3,5,7,9]

#%%

#list.pop(index)

print("pop():", lst.pop() , lst ) # Arg넣지않으면 맨마지막 것이 나온다. 

print("pop():", lst.pop(0) , lst )

print("pop():", lst.pop(2) , lst )
