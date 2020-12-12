#Ce script pour definir les functions du serveur
from datetime import datetime, date
import requests
import json
from flask import jsonify
import string
from pathlib import Path
import re

class getGlobalData(): #cette class pour récupérer les données de la situation globale actuelle de COVID 19 en France
    request = requests.get("https://coronavirusapi-france.now.sh/FranceLiveGlobalData")
    stt = request.status_code
    header = request.headers['content-type']
    encode = request.encoding
    text=request.text
    json = request.json()
    if stt==200:
        france_global = open("data/france_global.json", "w")
        france_global.write(text)
        france_global.close()
    #Cette class pour récupérer les données 
class getDepartementData(): #cette class pour récupérer les données de la situation de COVID19 des départements français. 
    def get_file_by_date(self, date): #ce fonction pour récupérer les données.
        my_file = Path("data/"+date+".json")
        if not my_file.is_file():
            request = requests.get("https://coronavirusapi-france.now.sh/AllDataByDate?date="+date) #c
            stt = request.status_code
            json_text = request.text
            if stt==200:
                all_departement = open("data/"+date+".json", "w")
                all_departement.write(json_text)
                all_departement.close()
    
    def get_departement_data(self, s_date,departement): #ce fonction pour traiter les données et retourner le résultat de recherche.
        with open("data/"+s_date+".json", "r") as f:
            my_dict = json.load(f)
        for element in my_dict['allFranceDataByDate']:
            s = departement 
            dept_code = "DEP-"+re.search(r'\(([^)]+)\)', s).group(1)
            if 'code' not in element:
                hospitalises = 'NA'
                reanimation = 'NA'
                nouvellesHospitalisations = 'NA'
                nouvellesReanimations = 'NA'
                deces = 'NA'
                gueris = 'NA'
                dep_data={'dep_data':[{'nom': nom, 'code': code, 'hospitalises': hospitalises, 'reanimation': reanimation,
                            'nouvellesHospitalisations': nouvellesHospitalisations, 'nouvellesReanimations': nouvellesReanimations, 'deces': deces, 'gueris': gueris}]}
                return dep_data
            else:
                if element['code'] == dept_code:
                    code = [element['code']][0]
                    nom  = [element['nom']][0]
                    hospitalises = [element['hospitalises']][0]
                    reanimation = [element['reanimation']][0]
                    nouvellesHospitalisations = [element['nouvellesHospitalisations']][0]
                    nouvellesReanimations = [element['nouvellesReanimations']][0]
                    deces = [element['deces']][0]
                    gueris = [element['gueris']][0]
                    dep_data={'dep_data':[{'nom': nom, 'code': code, 'hospitalises': hospitalises, 'reanimation': reanimation,
                            'nouvellesHospitalisations': nouvellesHospitalisations, 'nouvellesReanimations': nouvellesReanimations, 'deces': deces, 'gueris': gueris}]}
                    return dep_data