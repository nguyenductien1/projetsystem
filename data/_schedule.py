#! /usr/bin/env python
#Il faut installer python-crontab: pip3 install python-crontab
#Ce script nous permet de lancer les code python chaque 12 hours, ça peut permet de récuperer les données pour l'affichage des graphs.

from crontab import CronTab
import sys
cron = CronTab(tab='tiennd')

job_get_data = cron.new(command='python3 /home/tiennd/Desktop/ProjetSystem/covid19france/data/_get_data.py')
job_get_data.hour.every(11)

job_cas_confirmes = cron.new(command='python3 /home/tiennd/Desktop/ProjetSystem/covid19france/data/_traitement_cas_confirmes.py')
job_cas_confirmes.hour.every(12)

job_hospitalises = cron.new(command='python3 /home/tiennd/Desktop/ProjetSystem/covid19france/data/_traitement_hospitalises.py')
job_hospitalises.hour.every(12)

#Vérifier les configuations de schédules.
for item in cron:
    print(item)

cron.write()