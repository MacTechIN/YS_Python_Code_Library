#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:22:58 2023

@author: sam
"""
import time


def elapsed(original_func):
	@functools.wraps(original_func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = original_func(*args, **kwargs)
		end = time.time()
		print("함수 수행시간: %f 초" % (end - start))
		return result
	return wrapper


@elapsed
def add(a, b):
    """ 두 수 a, b를 더한값을 리턴하는 함수 """
    return a + b


result = add(3, 4)
#%%
@elapsed
def test(n):
	if n == 1:
		return n 
	return n * test(n-1)

#%%

test(100)


#%%

print(add)
print(add(10,20)) 

#%%
help(add)
## hlep 호출 하면 add의 주석이 출력 이 안되고 elapsed에 선언된 주석이 나온다 




