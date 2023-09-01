#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:12:12 2023

@author: sam
"""

#2023 09 01 
#오전 세션 

#리스트박스 이벤트
#03. 이벤트 선택 반응 구현 추가  
from tkinter import * 
import tkinter.messagebox

#%%
def event_for_listbox(event):
	w = event.widget
	index = int(w.curselection()[0])
	value = w.get(index)
	msg = f"selected item index({index}) , value ({value}) !!"
	tkinter.messagebox.showinfo("리스트 선택 : ", msg)
	print("리스트 박스가 클릭 되었습니다.", msg)
	
root = Tk()

listbox = Listbox(root)
listbox.pack()



for item in ["item one", "item two", "item three", "item four"]:
	listbox.insert(END, item)

#이벤트 헨들러 - <<이벤트호출문장형식>>
listbox.bind("<<ListboxSelect>>", event_for_listbox)

root.mainloop()  ## 메세지를 처리해준다. 

