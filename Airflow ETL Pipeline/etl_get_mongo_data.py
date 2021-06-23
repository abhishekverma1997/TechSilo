# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:39:58 2021

@author: Abhishek
"""
import pymongo

from datetime import date

import json

import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


client = pymongo.MongoClient("ENTER MONGODB LINK")

db = client.test

mydb = client['Holidays2021_country_list']

information = mydb.Holiday_List

today_date = str(date.today())

holiday_today = information.find({'h_date':today_date})

test_string = ""

for records in holiday_today:
    
    test_string = test_string + records['country_name'] + "\n" + records['h_date']+ "\n" + records['h_name'] + "\n" + records['h_info'] + "\n" + "\n"
    



mail_content = test_string

rcvr_address = ['abv19.pitt@yandex.com']

#,'onlineabhinav1987@gmail.com','pranav.verma.dssd@gmail.com'


for r_address in rcvr_address:
    #The mail addresses and password
    sender_address = ENTER GMAIL ADDRESS
    sender_pass = ENTER GMAIL PASSWORD
    receiver_address = r_address
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Holidays Around the World On '+ today_date  #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent to '+ receiver_address)
    






