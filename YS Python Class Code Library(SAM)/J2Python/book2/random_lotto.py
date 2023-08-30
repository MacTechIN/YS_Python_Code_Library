#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:59:52 2023

@author: sam
"""

#예상당첨번호 난수 6개를 만들어라 
#2. 임의의 숫자 6개를 키보드로 입력 받아
#3. 당첨 유무를 확인 하라 

#롯도 함수 를 만들어라 

import random 
import time

userNumbers=[]
lottNumbers=[]
matchResult = []

def GameStart():
	print("안녕하세요 롯도 담첨 확인 기계입니다.")
	time.sleep(0.5)
	print("당신의 번호를 6개 숫자(1~45)를 연속 입력 해주세요")
	time.sleep(1)
	while len(userNumbers) < 6:
		info = str(len(userNumbers))+" 번째 번호를 입력하세요    -> " 
		userInput = input(info)
		if userInput == "" or int(userInput) < 1 or int(userInput) > 45 or userInput == "  " :
			print(" 번호를 제대로 넣어줘요~!!! 제발 !!!")
		else: 
			userNumbers.append(int(userInput))
	
	lottNumbers = lottoNumber() 	
	checkLotto(lottNumbers, userNumbers)  
	print ("금주의 롯도번호는 : ", lottNumbers)

			
def lottoNumber():
	result = []
	while len(result) < 6:
		num = random.randint(1,45)
		if num not in result:
			result.append(num)
	return result
		
def checkLotto(result,userList):
	for i in result:
		for j in userList:
			if i == j:
				matchResult.append(i)

	if len(matchResult) == 5:
		print("축하드립니다. 담청 되셨습니다.!!!!! ")
	else:
		print("*"*50)
		print ("당신이 입력한 번호는 : ", userNumbers)
		print("당신이 맞춘 번호는 " , matchResult)
				

GameStart()
