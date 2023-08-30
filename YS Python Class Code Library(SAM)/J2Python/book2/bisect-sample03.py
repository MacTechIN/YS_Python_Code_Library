#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:09:34 2023

@author: sam
"""

import bisect

scores=[60,33,99,77,70,89,90,99,100]
grades = 'FDCBA'
result = []

for score in scores: #기준점수 이상 
	#점수가 정렬되어 삽이될 수 있는 포지션을 반환 
	pos = bisect.bisect([60,70,80,90], score)
	grade = grades[pos]
	result[score].append()
	
#%%

xscore = list(zip(scores, result)) 
print(xscore)


