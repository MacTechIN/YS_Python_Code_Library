#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:12:12 2023

@author: sam
"""

#2023 09 01 
#오전 세션 

from tkinter import * 



root = Tk()
listbox = Listbox(root)
listbox.pack()

for item in ["item one", "item two", "item three", "item four"]:
	listbox.insert(END, item)

root.mainloop()  ## 메세지를 처리해준다. 

