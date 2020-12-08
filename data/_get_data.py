#! /usr/bin/env python
from datetime import datetime
import requests
import json
import string
from pathlib import Path
import re
m = range(1,13)
d = range(1,31)
for i in m:
    for j in d:
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
        #print(date)
        my_file = Path(date+".json")
        if not my_file.is_file():
            request = requests.get("https://coronavirusapi-france.now.sh/AllDataByDate?date="+date)
            stt = request.status_code
            json_text = request.text
            if stt==200:
                all_departement = open(date+".json", "w")
                all_departement.write(json_text)
                all_departement.close()