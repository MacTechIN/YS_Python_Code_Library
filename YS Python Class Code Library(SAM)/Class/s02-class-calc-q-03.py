#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 13:38:57 2023

@author: sam
"""

class Plus:
	def __init__(self,initval):
		self.tot = initval
		
	def addition(self, val):
		self.tot += val 
		
class Minus:
	def __init__(self, initval = 0):
		self.tot = initval
		
	def substract(self, val):
		self.tot += val 		
			
class Mul:
	def __init__(self,initval):
		self.tot = initval
		
	def mul(self, val):
		self.tot *= val 

class Div:
	def __init__(self,initval):
		self.tot = initval
		
	def mul(self, val):
		self.tot /= val		
	
		
class Calc(): 
	def __init__(self, initval):
		super.__init__(self,initval)
		
#%%
#1. 클레스의 Static Method 는 (@staticmethod) 정적 메서드 
#2. 선언 @staticmethod  
#3. 클레스이름.method() 호출
#4. - class이름.staticmethod() or objectname.staticmethod()



#%%		
				
class CalcProto():
	def __init__(self, initval = 0):
		self.initval = initval
		
	def total(self):
		return self.tot;
	
	def avg(self):
		return self.tot/self.cnt
	
	def count(self):
		self.cnt += 1
		
	def clear(self, initval = 0 ):
		self.tot = initval
		self.cnt = 0 

#%%


		

calc = Calc(10)
