from app import app
from flask import render_template, request
from datetime import datetime
from app.models import getGlobalData
from app.models import getDepartementData
from app.config import Config
import string
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    with open("data/france_global.json", "r") as f:
        my_dict = json.load(f)
    date = my_dict['FranceGlobalLiveData'][0]['date']
    
    if 'casConfirmes' not in my_dict['FranceGlobalLiveData'][0]: 
        casConfirmes= "not availble"
    else:
        casConfirmes= my_dict['FranceGlobalLiveData'][0]['casConfirmes']

    deces = my_dict['FranceGlobalLiveData'][0]['deces']
    return render_template('index.html', title='Situation COVID19 en France', date = date, casConfirmes = casConfirmes, deces = deces)

@app.route('/search_by_date', methods=['POST'])
def search_by_date():
    departement_data = getDepartementData()
    date = request.form['bday']
    departement = request.form['departement']
    departement_data.get_file_by_date(date)
    data_json = departement_data.get_departement_data(date, departement)
    nom = data_json['dep_data'][0]['nom']
    hospitalises = data_json['dep_data'][0]['hospitalises']
    deces = data_json['dep_data'][0]['deces']
    return '<div class="row">'+'<div class="col-lg-2">'+ 'Date: ' + date +'</div>' + '<div>' + '<div class="col-lg-2">'+ 'Département: ' + nom +'</div>' + '<div>' + '<div class="col-lg-2">'+ 'Déces: ' + str(deces) +'</div>' + '<div>'+ '<div class="col-lg-2">'+ 'Hospitalises: ' + str(hospitalises) + '</div>'+ '</div>'
