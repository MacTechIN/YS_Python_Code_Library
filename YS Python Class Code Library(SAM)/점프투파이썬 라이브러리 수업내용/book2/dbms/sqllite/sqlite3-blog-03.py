#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 13:52:36 2023

@author: sam
"""

import sqlite3

conn = sqlite3.connect("blog.db")
curr = conn.cursor()

#%%
def selectAll(cur):
	cur.execute("SELECT * FROM blog")
	try: 
		data = cur.fetchall()
		for d in data:
			print(d)
	except:
		print("db 조회오류 ")


def delete(cur, id_):
	sql = "DELETE FROM blog WHERE id = ?"
	try: 
		cur.execute(sql, (id_,))
	
	except:
		print("조회 오류")


def update(cur,id_, subject, content, date):
	sql = """
		UPDATE blog SET subject= ?,
			content = ?,
			date  = ? 
		WHERE id = ?
	""";
	try:
		cur.execute(sql,(subject, content, date,id_))
	
	except:
		print("update Error !!")
	
	
def insert(cur, id_ , subject, content, data):
	sql = "INSERT INTO blog VALUES (?,?,?,?)"
	try: 
		cur.execute(sql,(id_, subject, content, data))
	
	except:
		print("insert ERROR !!!")	

#%%

selectAll(curr)
insert(curr, 19, "십구구구", "십구의 내용", "20230931")
print("="*50)
selectAll(curr)
update(curr, 19,"구구단", "구구단을 외자", "20020101")
print("="*50)
selectAll(curr)
delete (curr, 19 )
print("="*50)
selectAll(curr)
print("="*50)
conn.commit()
conn.close()
#%%


