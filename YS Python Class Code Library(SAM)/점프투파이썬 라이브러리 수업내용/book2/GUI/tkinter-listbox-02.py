#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:12:12 2023

@author: sam
"""

#2023 09 01 
#오전 세션 

#리스트박스 이벤트 반응 구현 

from tkinter import * 

#%%
def event_for_listbox(event):
	print("리스트박스가 클릭 되었습니다.")


#%%


root = Tk()
listbox = Listbox(root)
listbox.pack()

#이벤트 헨들러 - <<이벤트호출문장형식>>
listbox.bind("<<ListboxSelect>>", event_for_listbox)

for item in ["item one", "item two", "item three", "item four"]:
	listbox.insert(END, item)

#%%
root.mainloop()  ## 메세지를 처리해준다. 

