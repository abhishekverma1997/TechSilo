import calendarific

import requests

import json

api_1 = "https://calendarific.com/api/v2/holidays?&api_key=ec92ccb1587f256574eaae065d36b56c66228ceb&country="
api_2 = "&"
api_3 = "year="

api_final = api_1 + 'US' + api_2 + api_3 + "2020"

print(api_final)

api_testing = requests.get(api_final)

response_holiday_2021 = requests.get("https://calendarific.com/api/v2/holidays?&api_key=ec92ccb1587f256574eaae065d36b56c66228ceb&country=US&year=2021")

response_country_code = requests.get("https://calendarific.com/api/v2/countries?&api_key=ec92ccb1587f256574eaae065d36b56c66228ceb")


print(response_holiday_2021.json()['response']['holidays'][0]['country']['name'])
print(response_holiday_2021.json()['response']['holidays'][0]['name'])
print(response_holiday_2021.json()['response']['holidays'][0]['description'])
print(response_holiday_2021.json()['response']['holidays'][0]['date']['iso'])

print(len(response_holiday_2021.json()['response']['holidays']))



for j in range(len(response_holiday_2021.json()['response']['holidays'])):
    print(response_holiday_2021.json()['response']['holidays'][j]['country']['id'])
    print(response_holiday_2021.json()['response']['holidays'][j]['name'])
    print(response_holiday_2021.json()['response']['holidays'][j]['description'])
    print(response_holiday_2021.json()['response']['holidays'][j]['date']['iso'])
    print("  **********************************   ")

    

api_text = json.dumps(response.json(), sort_keys=True, indent=4)

print(api_text)

print(response_country_code.json())

print(response_country_code.json()['response']['countries'][228]['country_name'])
print(response_country_code.json()['response']['countries'][228]['iso-3166'])

print(len(response_country_code.json()['response']['countries']))

country_code_list = []
country_name_list = []

for i in range(len(response_country_code.json()['response']['countries'])):
    country_code_list.append(response_country_code.json()['response']['countries'][i]['iso-3166'])
    country_name_list.append(response_country_code.json()['response']['countries'][i]['country_name'])
    

print(country_name_list)
print(country_code_list)    
print(len(country_name_list))
print(len(country_code_list))


for i in country_code_list:
    
    api_1 = "https://calendarific.com/api/v2/holidays?&api_key=ec92ccb1587f256574eaae065d36b56c66228ceb&country="
    api_2 = "&"
    api_3 = "year="
    api_final = api_1 + i + api_2 + api_3 + "2021"
    response_holiday_2021 = requests.get(api_final)
    for j in range(len(response_holiday_2021.json()['response']['holidays'])):
        
        mydb = client['Holidays2021_country_list']

        information = mydb.Holiday_List
        
        
        records={'country_id':response_holiday_2021.json()['response']['holidays'][j]['country']['id'],
                 'country_name':response_holiday_2021.json()['response']['holidays'][j]['country']['name'],
                 'h_name':response_holiday_2021.json()['response']['holidays'][j]['name'],
                 'h_info':response_holiday_2021.json()['response']['holidays'][j]['description'],
                 'h_date':response_holiday_2021.json()['response']['holidays'][j]['date']['iso']
                }
        
        information.insert_one(records)
    
    
    
    
    





import pymongo
import dnspython


client = pymongo.MongoClient(""ENTER MONGODB LINK"")

db = client.test


mydb = client['Holidays2021']

information = mydb.Holiday_List


records={'country_id':'IN','h_name':'NY',
         'h_info':'New years'
        }

information.insert_one(records)






