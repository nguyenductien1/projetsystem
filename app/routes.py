from app import app
from flask import render_template, request
from datetime import datetime, date
from app.models import getGlobalData        #importer la class pour récupérer les données global.
from app.models import getDepartementData   #importer la class getDepartementDate, cette class contient lles fonction pour la recherche situation des départment par date et nom
from app.config import Config               #importer la configuation du server flask
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

@app.route('/search_by_date', methods=['POST']) #cette route pour la fonction de recherche par date et par nom du département 
def search_by_date():
    
    departement_data = getDepartementData() #apelle la class getDepartementData
    date = request.form['bday']             #date qui vient de la demande de client side
    departement = request.form['departement'] #nom du département qui vient de la demande de client side
    if datetime.today() < datetime.strptime(date, '%Y-%m-%d'): #ce condition pour enlever les erreurs de recherches
        return '<div class="row">'+'<div class="col-lg-4">' + 'Date dois être en présent ou passé'+ '</div>' + '<div>' 
    else: 
        departement_data.get_file_by_date(date) #apelle le fonction pour récupérer le fichier json de la date recherche si il n'existe pas 
        data_json = departement_data.get_departement_data(date, departement) #apelle le fonction pour récupérer le résultat de recherche
        nom = data_json['dep_data'][0]['nom']
        hospitalises = data_json['dep_data'][0]['hospitalises']
        deces = data_json['dep_data'][0]['deces']
        return '<div class="row">'+'<div class="col-lg-2">'+ 'Date: ' + date +'</div>' + '<div>' + '<div class="col-lg-2">'+ 'Département: ' + nom +'</div>' + '<div>' + '<div class="col-lg-2">'+ 'Déces: ' + str(deces) +'</div>' + '<div>'+ '<div class="col-lg-2">'+ 'Hospitalises: ' + str(hospitalises) + '</div>'+ '</div>'
        #ce fonction retourne le resultat de la recherche sous les formats des tag de html5.
@app.route('/get_hospital_mois', methods=['GET']) #ce route pour retourner le resultat sous format json pour l'affichage de graph nouvelles cas hospitalises par mois
def get_hospital_mois():
    with open('data/_hospitalises.json', 'r') as f:
        my_dict = json.load(f)
        return my_dict

@app.route('/get_nombre_confirmes', methods=['GET']) #ce route pour retourner le resultat sous format json pour l'affichage de graph nouvelles cas confirmés par mois
def get_nombre_confirmes():
    with open('data/_casConfirmes.json', 'r') as f:
        my_dict = json.load(f)
        return my_dict