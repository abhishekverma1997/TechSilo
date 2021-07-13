# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 16:32:44 2021

@author: Abhishek
"""

from flask import Flask, render_template, request
from flask import render_template_string
import pickle
import numpy as np
from random import randint

import pymysql.cursors
import pandas as pd
from datetime import datetime

from itertools import combinations


app = Flask(__name__)


current_user_email="None"
current_user_id = 0

def current_user_fn(email_id, user_id):
    global current_user_email
    global current_user_id
    current_user_email=email_id
    current_user_id = user_id

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/pitt_nivesh_main')
def home():
	return render_template('index2.html')

@app.route('/user_profile')
def user_profile():
    
    
    con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = con.cursor()
    qry = 'SELECT * FROM user_profile WHERE '
    qry = qry + 'email LIKE %s '
    cursor.execute(qry, (current_user_email)) 
            
    rows = cursor.fetchall()
            
    con.commit()
    con.close()

    con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = con.cursor()
    qry_add = 'SELECT * FROM user_address WHERE '
    qry_add = qry_add + 'user_id = %s '
    cursor.execute(qry_add, (current_user_id)) 

    rows1 = cursor.fetchall()

    con.commit()
    con.close()

    return render_template('user_profile_page.html',what_profile=rows, user_name_what=current_user_email, what_address=rows1)




    

@app.route('/user_reg', methods=['POST'])
def user_registration():
    if request.method == 'POST':
        #return render_template('index2.html')
        user_id = request.form['user_id']
        email_id = request.form['email']
        password = request.form['password']
        user_name = request.form['user_name']
        dob = request.form['dob']
        gender = request.form['gender']
        bio = request.form['bio']

        street1 = request.form['st1']
        street2 = request.form['st2']
        city = request.form['city']
        state = request.form['state']
        country = request.form['country']
        zip = request.form['zip']


        
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

        cursor = con.cursor()
        qry = 'SELECT * FROM user_login WHERE '
        qry = qry + 'email LIKE %s '
        cursor.execute(qry, (email_id)) 
        
        rows = cursor.fetchall()
        
        con.commit()
        con.close()
        
        if(len(rows)==1):
            
            return render_template('index2.html', what= "USER ALREADY EXISTS" )
        else:
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

            cursor = con.cursor()
            qry = 'INSERT INTO user_login (user_id, email, password)'
            qry = qry + 'VALUES(%s, %s, %s)'
            qry2 = 'INSERT INTO user_profile (user_id, name, email, dob, gender, bio)'
            qry2 = qry2 + 'VALUES(%s, %s, %s, %s, %s, %s)'
            qry3 = 'INSERT INTO accounts (user_id, balance, status)'
            qry3 = qry3 + 'VALUES(%s, %s, %s)'
            qry4 = 'INSERT INTO user_address (user_id, street1, street2, city, state, country, zip)'
            qry4 = qry4 + 'VALUES(%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(qry, (user_id, email_id, password)) 
            cursor.execute(qry2, (user_id, user_name, email_id, dob, gender, bio))
            cursor.execute(qry3, (user_id, 10000, 1)) 
            cursor.execute(qry3, (user_id, 10000, 1))
            cursor.execute(qry4, (user_id, street1, street2, city, state, country, zip))
            con.commit()
            con.close()
                
            return render_template('index2.html', what= "USER SUCESSFULLY REGISTERED")
            
        

        
        
 

@app.route('/home_page')
def user_home_page():
    return render_template('pitt_nivesh_home.html', user_name_what=current_user_email)

@app.route('/log_out_to_user_reg')
def log_out_to_user_reg():
    global current_user_email
    global current_user_id
    current_user_email="None"
    current_user_id = 0
    return render_template('index.html')

@app.route('/login_user')
def login_user():
    return render_template('login_auth.html')


@app.route('/user_authentication',methods=['POST'])
def user_authentication():
    if request.method == 'POST':
        email_id = request.form['email']
        password = request.form['password']
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        cursor = con.cursor()
        
        qry = 'SELECT * FROM user_login WHERE '
        qry = qry + 'email LIKE %s AND password LIKE %s '
        
        cursor.execute(qry, (email_id, password)) 
    
        rows = cursor.fetchall()
        
        #print(len(rows))
        
        #print(rows[0]['email'])
        
        con.commit()
        con.close()
        
        
        if(len(rows)==0):
            
            return render_template('login_auth.html', what= "USER DOES NOT EXIST" )
        
        if(rows[0]['email']==email_id and rows[0]['password']==password):
            
            #return render_template('login_auth.html', what=rows[0]['email'])
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
            cursor = con.cursor()
            
            qry = 'SELECT user_id FROM user_login WHERE '
            qry = qry + 'email LIKE %s'
            
            
            cursor.execute(qry, (email_id)) 
            
            rows = cursor.fetchall()
            con.commit()
            con.close()
            
            user_id = rows[0]['user_id']
        
            
            current_user_fn(email_id, user_id)
            
            return user_home_page()
            
        
        else:
            return render_template('login_auth.html', what= "USER DOES NOT EXIST" )
            
        
        
    
    
        

@app.route('/stock_search')
def stock_search_button():
    
    return render_template('stocks.html', user_name_what=current_user_email)
    
           
@app.route('/stock', methods=['POST'])
def stock_search():
    if request.method == 'POST':
        stock_id_info = request.form['stock_id_info']
        
        #stk_id='AAPL'
        
        con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
        cursor = con.cursor()
        qry = 'SELECT * FROM available_stocks WHERE '
        qry = qry + 'symbol LIKE %s ORDER BY timestamp DESC'
        
        cursor.execute(qry, (stock_id_info)) 
    
        rows = cursor.fetchall()
        
        con.commit()
        
        con.close()
        
        #for index in range(len(rows)):
            #print("{} \t {}".format(rows[index]['symbol'],rows[index]['stock_id']))
        
        #{{ what }}<br>
        #<br>
        
        return render_template('stocks.html', what=rows, user_name_what=current_user_email)
    
    
@app.route('/buy_stocks_button')
def buy_stocks_button():

    return render_template('buy_stock.html', user_name_what=current_user_email)     

@app.route('/buy_stocks', methods=['POST'])
def buy_stocks():
    if request.method == 'POST':
        stock_symbol = request.form['stock_symbol']
        stock_volume = request.form['stock_volume']
        stock_fav = request.form['fav_stock']
        
        try:
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
            cursor = con.cursor()
            
            #args = [stock_symbol, stock_volume, current_user_email, current_user_id]
            
            if(stock_fav=='yes'):
                
                
                r = cursor.callproc('sp_trx', (stock_symbol, stock_volume, current_user_email, current_user_id, 1,0))
                
            else:
               
                r = cursor.callproc('sp_trx', (stock_symbol, stock_volume, current_user_email, current_user_id, 0,0))
            
            #print(result_args)
            
            
        
        except pymysql.connect.Error as error:
            
            return render_template('buy_stock.html', what='ROLL-BACKED : ERROR OCCURED WHILE BUYING STOCKS', user_name_what=current_user_email)
        
        
        finally:
            con.close()
            
            if len(r)>0:
                return render_template('buy_stock.html', what='STOCK BOUGHT SUCCESS', user_name_what=current_user_email)
            else:
                return render_template('buy_stock.html', what='ROLL-BACKED : ERROR OCCURED WHILE BUYING STOCKS', user_name_what=current_user_email)
                
        

        

            

@app.route('/friend_search')

def friend_search_button():

    return render_template('friend.html', user_name_what=current_user_email)     

        

@app.route('/friends', methods=['POST'])

def friend_add():

    if request.method == 'POST':

        group_name = request.form['group_name']

        friend_info1 = request.form['friend_info1']

        friend_info2= request.form['friend_info2']

        friend_info3 = request.form['friend_info3']
        
        friend_1_user_id= -1
        friend_2_user_id= -1
        friend_3_user_id= -1
    
      
        #CHECK IF ADMIN AND GROUP NAME ALREADY EXISTS

        current_user_id_test=6

        con = pymysql.connect(host='134.209.169.96',

                             user='pitt_nivesh',

                             password='pitt_Nivesh_123@!',

                             db='pitt_nivesh',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

       

        cursor = con.cursor()

        qry = 'SELECT * FROM collaboration WHERE '

        qry = qry + 'admin = %s '

       
        cursor.execute(qry, (current_user_id_test))

    

        rows = cursor.fetchall()

        con.commit()

       

        con.close()
        
        # CHECKING IF ADMIN ALREADY HAS IS AN ADMIN OF SAME GROUP NAME
        
        if(rows[0]['group_name']==group_name and rows[0]['admin']==current_user_id_test):
            
            return render_template('friend.html', what= "ADMIN WITH THE SAME GROUP NAME ALREADY EXIST" )
            
        
        #FRIEND's EXIST OR NOT 
        
        con = pymysql.connect(host='134.209.169.96',

                             user='pitt_nivesh',

                             password='pitt_Nivesh_123@!',

                             db='pitt_nivesh',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

       

        cursor = con.cursor()

        qry = 'SELECT * FROM user_profile WHERE '

        qry = qry + 'email LIKE %s '
        
        cursor.execute(qry, (friend_info1))

        rows_f1 = cursor.fetchall()

        con.commit()

        con.close()
        
       
        
        if(len(rows_f1)==0):
            
            return render_template('friend.html', what= "FRIEND 1 DOES NOT EXIST" )
        
        else:
            
            friend_1_user_id = rows_f1[0]['user_id']
            
        

        # FRIEND 2
        
        con = pymysql.connect(host='134.209.169.96',

                             user='pitt_nivesh',

                             password='pitt_Nivesh_123@!',

                             db='pitt_nivesh',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

       

        cursor = con.cursor()

        qry = 'SELECT * FROM user_profile WHERE '

        qry = qry + 'email LIKE %s '

        
        cursor.execute(qry, (friend_info2))

        rows_f2 = cursor.fetchall()
        

        con.commit()

        con.close()
        
        if(len(rows_f2)==0):
            
            return render_template('friend.html', what= "FRIEND 2 DOES NOT EXIST" )
        
        else:
            
            friend_2_user_id = rows_f2[0]['user_id']
            
            
            
        
        # FRIEND 3
        
        con = pymysql.connect(host='134.209.169.96',

                             user='pitt_nivesh',

                             password='pitt_Nivesh_123@!',

                             db='pitt_nivesh',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

       

        cursor = con.cursor()

        qry = 'SELECT * FROM user_profile WHERE '

        qry = qry + 'email LIKE %s '

        
        cursor.execute(qry, (friend_info3))

        rows_f3 = cursor.fetchall()
        

        con.commit()

        con.close()
        
        if(len(rows_f3)==0):
            
            return render_template('friend.html', what= "FRIEND 3 DOES NOT EXIST" )
        
        else:
            
            friend_3_user_id = rows_f3[0]['user_id']
            
        
        
        
        con = pymysql.connect(host='134.209.169.96',

                             user='pitt_nivesh',

                             password='pitt_Nivesh_123@!',

                             db='pitt_nivesh',

                             charset='utf8mb4',

                             cursorclass=pymysql.cursors.DictCursor)

       

        cursor = con.cursor()

        qry = 'INSERT INTO collaboration (group_name, admin, friend_1,friend_2,friend_3)'

        qry = qry + 'VALUES(%s, %s, %s, %s, %s)'
        
        cursor.execute(qry, (group_name, current_user_id, friend_1_user_id, friend_2_user_id, friend_3_user_id))

        con.commit()

        con.close()
        
        return render_template('friend.html', what= "COLLABORATION GROUP FORMED SUCCESSFULLY" )


@app.route('/view_collab')
def view_collab_button():
    con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    cursor = con.cursor()
    qry = 'SELECT * FROM collaboration WHERE '
    qry = qry + '%s in (admin,friend_1,friend_2,friend_3) '
    cursor.execute(qry, (current_user_id))         
    rows = cursor.fetchall()
    temp={}
    rec=[]
    con.commit()
    con.close()
    for index in range(len(rows)):
        temp['groupname']=rows[index]['group_name']
        if(current_user_id!=rows[index]['admin']):
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            qry='SELECT * FROM user_login WHERE '
            qry= qry + 'user_id LIKE %s'
            cursor.execute(qry, (rows[index]['admin']))
            row = cursor.fetchall()
            temp['admin']=rows[index]['email']
            con.commit()
            con.close()
        
        else:
            temp['admin']=current_user_email
        if(current_user_id!=rows[index]['friend_1']):
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            cursor = con.cursor()
            qry='SELECT * FROM user_login WHERE '
            qry= qry + 'user_id LIKE %s'
            val=rows[index]['friend_1']
            cursor.execute(qry, (val))
            row = cursor.fetchall()
            temp['friend1']=row[index]['email']
            con.commit()
            con.close()
        else:
            temp['friend1']=current_user_email
        if(current_user_id!=rows[index]['friend_2']):
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            cursor = con.cursor()
            qry='SELECT * FROM user_login WHERE '
            qry= qry + 'user_id LIKE %s'
            val=rows[index]['friend_2']
            cursor.execute(qry, (val))
            row = cursor.fetchall()
            temp['friend2']=row[index]['email']
            con.commit()
            con.close()
        else:
            temp['friend2']=current_user_email
        if(current_user_id!=rows[index]['friend_3']):
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            cursor = con.cursor()
            qry='SELECT * FROM user_login WHERE '
            qry= qry + 'user_id LIKE %s'
            val=rows[index]['friend_3']
            cursor.execute(qry, (val))
            row = cursor.fetchall()
            temp['friend3']=row[index]['email']
            con.commit()
            con.close()
        else:
            temp['friend3']=current_user_email
        temp1=temp.copy()
        rec.append(temp1)
        temp.clear()
    
    
    return render_template('collab.html',what_collab=rec,user_name_what=current_user_email)

@app.route('/view_transaction')
def view_transaction_button():
    con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    qry='SELECT * from transact WHERE '
    qry= qry + 'user_id LIKE %s'
    cursor.execute(qry, (current_user_id))
    rows=cursor.fetchall()
   
    
    return render_template('transaction.html',what_collab=rows,user_name_what=current_user_email)

@app.route('/buy_stocks_collab_button')
def buy_stocks_collab_button():
    return render_template('buy_stocks_collab.html', user_name_what=current_user_email)


@app.route('/buy_stocks_collab', methods=['POST'])
def buy_stocks_collab():
    if request.method == 'POST':
        group_name = request.form['group_name']
        f1_cont = request.form['f1_cont']
        f2_cont = request.form['f2_cont']
        f3_cont = request.form['f3_cont']
        stock_symbol = request.form['stock_symbol']
        stock_volume = request.form['stock_volume']
        
        try:
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        
            cursor = con.cursor()
            
            #args = [stock_symbol, stock_volume, current_user_email, current_user_id]
            
            
            r = cursor.callproc('sp_trx_collab', (group_name, f1_cont, f2_cont, f3_cont, stock_symbol, stock_volume, current_user_id,0))
            
            #print(result_args)
        
        except pymysql.connect.Error as error:
            
            return render_template('buy_stocks_collab.html', what='ROLL-BACKED : ERROR OCCURED WHILE BUYING STOCKS', user_name_what=current_user_email)
        
        
        finally:
            con.close()
            
            if len(r)>0:
                return render_template('buy_stocks_collab.html', what='STOCK BOUGHT TOGETHER SUCCESS', user_name_what=current_user_email)
            else:
                return render_template('buy_stocks_collab.html', what='ROLL-BACKED : ERROR OCCURED WHILE BUYING STOCKS', user_name_what=current_user_email)
                
@app.route('/view_investedstock')
def view_investedstock_button():
    con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    qry='SELECT * from invested WHERE '
    qry= qry + 'user_id LIKE %s'
    cursor.execute(qry, (current_user_id))
    rows=cursor.fetchall()
    print(rows)
   
    
    return render_template('investedstock.html',what_collab=rows,user_name_what=current_user_email)
    
        
        
    
if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)
