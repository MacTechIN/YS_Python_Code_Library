#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 15:08:18 2023

@author: sam
"""

# 모듈이란 함수나 변수 또는 클래스를 모아놓은 파이썬 파일이다. 

PI = 3.141592

#Class define

class Math:
	@staticmethod
	def circlearea(r):
		return PI * (r**2)


def add(a, b):
	return a+b 

def sub(a,b):
	return a-b 


print("[mod2.py] __name__ : ", __name__)

if __name__ == "__main__":
	a = 10 
	b = 20
	
	print(f"add({a}, {b}) -> {add(a,b)}")
	print(f"add({a}, {b}) -> {sub(a,b)}")
	
	print (f"원에 넓이({a}) -> {Math.circlearea(a)}")