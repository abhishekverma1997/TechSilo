# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:32:44 2021

@author: Abhishek
"""

from flask import Flask, render_template, request
import pickle
import numpy as np


import pymysql.cursors
import pandas as pd
import datetime
from itertools import combinations


app = Flask(__name__)

@app.route('/wtf')
def home():
	return render_template('index2.html')

@app.route('/user_reg', methods=['POST'])
def user_registration():
    if request.method == 'POST':
        #return render_template('index2.html')
        user_id = request.form['user_id']
        email_id = request.form['email']
        password = request.form['password']
        
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        cursor = con.cursor()
        qry = 'INSERT INTO user_login (user_id, email, password)'
        qry = qry + 'VALUES(%s, %s, %s)'
        cursor.execute(qry, (user_id, email_id, password)) 
        con.commit()
        con.close()
            
        return render_template('index2.html')
            
    
    
    


if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)