#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:59:52 2023

@author: sam
"""

import random 

result = [] 

while len(result) < 6:
	num = random.randint(1,45)
	result.append(num)
	
print(result )