#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:52:36 2023

@author: sam
"""
#sqlite3  connector 
#https://sqlitebrower.org/dl/

import sqlite3


#접속 
conn = sqlite3.connect("blog.db")

#커서 생성 

cur = conn.cursor()

cur.execute("SELECT count(*) FROM sqlite_master WHERE name = 'blog' ")
exist = cur.fetchone()

#테이블 생성 은 한번만 수행 
if exist[0] !=1:
	cur.execute("""
			CREATE TABLE blog (
				id integer PRIARY KEY,
				subject text,
				content text,
				date text
				)""")

#%%

#데이터 입력 
insert_sql = "INSERT INTO blog VALUES (%d, '%s', '%s', '%s')"

insert_data =[
	(3, '세번째 블러그', '세번째 블러그 내용', '20230831'),
	(4, '네번째 블러그', '네번째 블러그 내용', '20230831'),
	(5, '다섯번째 블러그', '다섯번째 블러그 내용', '20230831'),
	]

try:
	for d in insert_data:
		sql = insert_sql % (d[0], d[1], d[2], d[3])
		print(sql)
		cur.execute(sql)
except:
	print("sql 실행 오류")
finally:
	conn.commit()
	conn.close() 
