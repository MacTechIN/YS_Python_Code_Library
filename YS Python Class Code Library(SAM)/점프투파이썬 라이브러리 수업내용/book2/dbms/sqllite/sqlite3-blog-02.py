#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:52:36 2023

@author: sam
"""

import sqlite3


#접속 
conn = sqlite3.connect("blog.db")

#커서 생성 
cur = conn.cursor()

#쿼리 : 검색조건으로 결과셋을 얻음 
#cur.execute("SELECT * FROM blog")
cur.execute("SELECT * FROM blog WHERE id IN(1)")
#쿼리의 결과를 얻음 : list객체에 담음 

data= cur.fetchall()

for d in data: 
	print (d) #출력 

#접속종료 
conn.close() 