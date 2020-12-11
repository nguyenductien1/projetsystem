#! /usr/bin/env python
from datetime import datetime
import requests
import json
import string
from pathlib import Path
import re

m = range(1,13)
d = range(1,32)
text = ""

for i in m:
    total_mois = 0
    for j in d: 
        nbr_jour = 0 
        if i<10:
            if j<10:
                date='2020-'+'0'+str(i)+'-0'+str(j)
            if j>=10:
                date='2020-'+'0'+str(i)+'-'+str(j)
        elif i>=10: 
            if j>=10:
                date='2020-'+str(i)+'-'+str(j) 
            if j<10:
                date='2020-'+str(i)+'-0'+str(j)
        my_file = Path(date+".json")
        if not my_file.is_file():
            break             
        with open(date+".json", "r") as f:
            my_dict = json.load(f)
            nbr_jour_dep = 0
            for element in my_dict['allFranceDataByDate']:
                if 'nouvellesHospitalisations' in element:
                    nbr_jour_dep = nbr_jour_dep + int(element['nouvellesHospitalisations'])
                else:
                    nbr_jour_dep = nbr_jour_dep + 0
            nbr_jour = nbr_jour + nbr_jour_dep 
            #print("mois",' ',i,"jour",j,':', nbr_jour)
            total_mois = total_mois + nbr_jour
    #print(total_mois)
    text = text + '"'+'M'+str(i)+'"' +':'+str(total_mois) +',' 
    text_json = '{'+ text[:-1] +'}' 
#print(text_json)
new_file = open('_Mois'+".json", "w")
new_file.write(text_json)
new_file.close()
