# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 10:14:55 2021

@author: Abhishek
"""

from flask import Flask, render_template, request
from flask import render_template_string
import pickle
import numpy as np


import pymysql.cursors
import pandas as pd
import datetime
from itertools import combinations


import csv

with open('prices.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    stock_id_demo = 10
    for row in csv_reader:
        if line_count == 0:
            print(', '.join(row))
            line_count += 1
        elif line_count<200:
            
            print(row[0]+','+row[1]+','+row[2]+','+row[3]+','+row[4]+','+row[5]+','+row[6])
            
            qry = 'INSERT INTO available_stocks ( stock_id, timestamp, symbol, low, high, open, close, volume)'
            qry = qry + 'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
            
            con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
            
            cursor = con.cursor()
            
            cursor.execute(qry, (stock_id_demo+1, row[0], row[1], row[4], row[5], row[2], row[3], row[6]))
            
            stock_id_demo = stock_id_demo+1
            
            con.commit()
            con.close()
            
            line_count += 1
            
    print(line_count)
    
    