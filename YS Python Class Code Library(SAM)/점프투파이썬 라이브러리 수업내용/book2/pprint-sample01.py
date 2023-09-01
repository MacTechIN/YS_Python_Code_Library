#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 13:54:44 2023

@author: sam
"""
# pprint : pretty print 
# dict , json format 을 보기좋게 출력 

import pprint

#dict  
result = {'userId': 1, 'id': 1, 
 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 
 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

print(result )
print('-'*50)

#%%
pprint.pprint(result)



#%%

str()
