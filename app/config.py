import os
import string
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    def mini_to_mascu(self,text):
        return text.title()


#Ce script pour montrer les configuration de app, dans ce moment on n'utilise pas
