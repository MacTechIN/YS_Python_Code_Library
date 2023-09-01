#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:43:24 2023

@author: sam
"""

a = [1,2,3,4]
b = [2,3,4,5,6,7]


for i in range(len(a)):
	if a[i] in b :
		print("값있음")
	else:
		print("다름")

#%%	
	
for i in range(len(a)):
	if a[i] not in b:
		print("값없음")
			 