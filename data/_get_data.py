#! /usr/bin/env python
from datetime import timedelta,date
import requests
import json
import string
from pathlib import Path
import re

start_date = date(2020,1,1)
end_date = date.today()
date_count = timedelta(days=1)
date_range=(start_date, end_date)
while start_date <= end_date:
    date_str = start_date.strftime('%Y-%m-%d')
    my_file = Path(date_str+".json")
    if not my_file.is_file():
        request = requests.get("https://coronavirusapi-france.now.sh/AllDataByDate?date="+date_str)
        stt = request.status_code
        json_text = request.text
        if stt==200:
            all_departement = open(date_str+".json", "w")
            all_departement.write(json_text)
            all_departement.close()
    start_date = start_date + date_count
#ce script pour récupérer les données à jour.