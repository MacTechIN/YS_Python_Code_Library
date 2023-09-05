#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 23:35:45 2023

@author: sam
"""

#127.0.0.1:5000 (localhost:5000)
from flask import Flask , jsonify 

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello_World! from Flask"

@app.route('/hithere')
def hi_there():
	return "I just hit /hithere"

@app.route('/message')
def calc():
	rj = {
		   'name' : 'SamLEE',
			   'Phone' : '01058136550'
	   }
	
	return jsonify(rj)

if __name__ == '__main__':
	app.run()