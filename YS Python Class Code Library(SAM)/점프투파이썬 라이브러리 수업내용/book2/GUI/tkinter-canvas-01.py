#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:12:12 2023

@author: sam
"""

#2023 09 01 
#오전 세션 

import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(False, False)

canvas=tkinter.Canvas(window, relief="solid", bd=2)

line=canvas.create_line(10, 10, 50, 10, 50, 150, 300, 150, fill="red")


canvas.pack()

window.mainloop()