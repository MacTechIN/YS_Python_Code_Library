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



#%%

for r in q: #참조만 하기 때문에 데이터는 사라지지 않는다. 
	print(r)
	
print(q)

#확인 , 참조 만한다. 
r = q[1]
print( "q[r]:", r )




#%%
# pop()에 인덱스를 지정할 수 없다. 
# TypeError : deque.pop() takes no argument (1 given)
# print("q[1]:",q.pop(1))

#%%

# 스텍 (Stack ) : LIFO(Last in Firt Out), 후입선출 

r = q.popleft()
print("popleft() : r= ", r, "deque = ", q )




#%%
# 처음부터 하나씩 꺼내면서 데이터는 지움  

while q:
	r = q.popleft()
	print(r)

print(q)



