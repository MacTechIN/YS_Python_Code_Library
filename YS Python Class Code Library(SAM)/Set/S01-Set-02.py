#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 17:21:04 2023

@author: sam
"""

#집합 : set
#합집합 ,교집합, 차집합 

#특징 : 1.중복을 허용하지 않음. 2.순서가 없다. (인덱스가없다), 3.

#%%

# 합집합 

s1 = set([1,2,3,4,5,6])

s2 = set([4,5,6,7,8,9])


su = s1 | s2
print(su)

#%%

#교집합 

si = s1 & s2

print(si )


#%%

#차집합

sd = s1 - s2

print(sd)