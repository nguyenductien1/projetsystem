#!/usr/bin/env python
import os
import sys
from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes, models
#Ce script pour créer l'environnement de flask, pour definir le "app" comme l'application serveur par défault