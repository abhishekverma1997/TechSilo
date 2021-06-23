from datetime import timedelta
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

import pymongo

from datetime import date

import json

import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#from spotify_etl import run_spotify_etl

#'start_date': datetime(2021, 6, 17)
#'start_date': datetime(2021, 6, 17, 8, 42),
    #'end_date': datetime(2021, 6, 17, 8, 45),

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 6, 17, 00),
    'email': ['svermaan@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

#schedule_interval=timedelta(minutes=5)

dag = DAG(
    'HOLIDAY_ETL_DAG',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval='@daily'
    
)

def just_a_function():
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
    
    rcvr_address = ['abv21@pitt.edu','onlineabhinav1987@gmail.com','pranav.verma.dssd@gmail.com']
    
    #,'onlineabhinav1987@gmail.com','pranav.verma.dssd@gmail.com'
    
    
    for r_address in rcvr_address:
        
        #The mail addresses and password
        sender_address = ENTER EMAIL ADDRESS (GMAIL)
        sender_pass =  ENTER EMAIL ADDRESS PASSWORD (GMAIL)
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
    
    
    
    
    
    
    

run_etl = PythonOperator(
    task_id='TASK_1',
    python_callable=just_a_function,
    dag=dag,
)

run_etl
