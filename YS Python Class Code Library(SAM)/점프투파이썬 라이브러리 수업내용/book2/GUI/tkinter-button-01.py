#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:12:12 2023

@author: sam
"""

#2023 09 01 
#오전 세션 - button 구현  

#버튼 클릭 이벤트
# 버튼 클릭 이벤트 선택 반응 구현 추가 
 
from tkinter import * 
import tkinter.messagebox

def onevent(event):
	w = event.widget
	msg = f"button click ({w}) : 버튼이 클릭되었습니다."
	tkinter.messagebox.showinfo("버튼 선택 : ", msg)
	
root = Tk()

btn = Button(root, text ="여기를 클릭해 주세요.")
btn.pack()

btn.bind("<Button-1>", onevent)

root.mainloop()  ## 메세지를 처리해준다. 

