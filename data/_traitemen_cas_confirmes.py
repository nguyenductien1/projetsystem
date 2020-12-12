#! /usr/bin/env python
from datetime import timedelta,date
import json
from collections import defaultdict
import ast
#ce script pour traiter les données des nouveaux cas confirmés en France. Ce script va donner le fichier json qui a les donnée de chaque mois en France.
def cas_confirmes(date_str):
    with open(date_str+".json", "r") as f:
        my_dict = json.load(f)
        for element in my_dict['allFranceDataByDate']:
            if 'casConfirmes' in element and element['code']=='FRA': 
                return element['casConfirmes']
    
def new_cas_confirmes_by_date():
    start_date = date(2020,1,1)
    end_date = date.today()
    date_count = timedelta(days=1)
    total_month = 0
    data_date = ""
    while start_date <= end_date:
        if start_date != date(2020,1,1):
            date_moin = start_date - date_count 
            date_str = start_date.strftime('%Y-%m-%d')
            data_after = cas_confirmes(date_str)
            date_str_moin = date_moin.strftime('%Y-%m-%d')
            data_before = cas_confirmes(date_str_moin)
            if type(data_after)== int and type(data_before)==int:
                new_cas_confirmes = int(data_after) - int(data_before)
            else:
                new_cas_confirmes = 0
            if start_date.month == date_moin.month:
                total_month = total_month + new_cas_confirmes         
        else:
            new_cas_confirmes = cas_confirmes('2020-01-01')
            if type(new_cas_confirmes)==int:
                new_cas_confirmes = int(new_cas_confirmes)
            else:
                new_cas_confirmes = 0
        
        data_date = data_date + '('+ '"'+str(start_date.month)+ '"' + "," +  str(new_cas_confirmes) +')' + ','
        start_date = start_date + date_count
    data_total = ('['+data_date[:-1]+']')
    return data_total

#new_cas_confirmes_by_month:
data = new_cas_confirmes_by_date()
data_list = ast.literal_eval(data)
d = defaultdict(list)
for k,v in data_list:
    d[k].append(v)
sorted(d.items())
i = 1
data_text = ""
while i <=12:
    str_i = str(i)
    total_month = 0
    for item in d[str_i]:
        total_month = total_month + item
    data_text = data_text + '"'+'M'+str_i +'"'+ ':' + str(total_month) +','      
    i=i+1
data_text = '{'+data_text[:-1]+'}'
new_file = open('_casConfirmes.json',"w")
new_file.write(data_text)
new_file.close()