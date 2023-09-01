#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:09:34 2023

@author: sam
"""

import bisect

scores=[33,99,77,70,89,90,100]
grade = 'FDCBA'
result = []

for score in scores:
	#점수가 정렬되어 삽이될 수 있는 포지션을 반환 
	pos = bisect.bisect([60,70,80,90], score)
	grade = grade[pos]
	print(pos,grade)
	result.append(grade)
	
	
print(scores)
print(result)