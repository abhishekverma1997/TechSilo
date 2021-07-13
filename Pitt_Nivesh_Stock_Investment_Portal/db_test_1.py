# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:53:00 2021

@author: Abhishek
"""

import pymysql.cursors
import pandas as pd
import datetime
from itertools import combinations

con = pymysql.connect(host='134.209.169.96',
                             user='pitt_nivesh',
                             password='pitt_Nivesh_123@!',
                             db='pitt_nivesh',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = con.cursor()
qry = 'INSERT INTO user_login (user_id, email, password)'
qry = qry + 'VALUES(%s, %s, %s)'
cursor.execute(qry, (3, 'molly@gmail.com', 'mollyjohnson')) 
con.commit()
con.close()



try: 

    with con.cursor() as cur:
        qry = 'INSERT INTO user_login (user_id, email, password)'
        qry = qry + 'VALUES(%s, %s, %s)'

        cur.execute(qry, (2, 'King.Stephen@gmail.com', 'K!ngStephen' )) 
        con.commit()

finally:

    con.close()




<!--<h1>PITT NIVESH INC.</h1>-->
<p style="text-align:center;"><img src="pitt_nivesh.jpg", align='center'></p>




