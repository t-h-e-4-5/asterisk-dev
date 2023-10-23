#-----------------------------+++++++++++++++++++++++++D . E . B . U . T+++++++++++++++++++++++---------------------?#
#!------------------------++++++++++++++++++++++++D . E . B . U . T++++++++++++++++++++----------------------!#
    #!-------------------------+++++++++++++++++++D . E . B . U . T+++++++++++++++++----------------------!#   
        #!-----------------------+++++++++++++++++D . E . B . U . T++++++++++++++----------------------!#
            #!----------------------++++++++++++++D . E . B . U . T+++++++++++----------------------!#
                #!-----------------------+++++++++D . E . B . U . T++++++++----------------------!#
                    #!-----------------------+++++D . E . B . U . T+++++----------------------!#
                        #!-----------------------+D . E . B . U . T+----------------------!#
                            #!--------------------D . E . B . U . T--------------------!#



#?-----------------------------+++++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++---------------------?#
    #?---------------------------+++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++------------------?#
        #?------------------------++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++---------------?#
from app import app
from config import db
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
from models import Inscription
from datetime import date

#?-----------------------------+++++++++++++++++++++++++CONNEXION DB+++++++++++++++++++++++---------------------?#
    #?-------------------------+++++++++++++++++++++++++CONNEXION DB+++++++++++++++++++++++----------------?#
app.app_context().push()

#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#
    #?----------------------------++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#


global lang                   # Variable globale pour stocker le choix de la langue
#global parcours               # Variable globale pour stocker le choix du parcours
global domaine                # Variable globale pour stocker le choix du domaine
global btsFiliere             # Variable globale pour stocker le choix de la filière au BTS
global LpFiliere              # Variable globale pour stocker le choix de la filière de la Licence Professionnelle 
global LSoirFiliere           # Variable globale pour stocker le choix de la filière de la Licence du soir
global callerID               # Variable globale pour stocker le numéro de l'appellant 
global dateCall               # Variable globale pour stocker la date de l'appel 
global duree                  # Variable globale pour stocker la durée de l'appel 
global heur                   # Variable globale pour stocker l'heure de l'appel 
global modalite               # Variable globale pour stocker la modalité de payement 
global objectifs              # Variable globale pour stocker l'objectif de l'appel 
#global renseignements         # Variable globale pour stocker les renseignements de l'appel 
global buts                   # Variable globale pour stocker l'information fournis après l'objectif (C'est à dire peu importe si c'est l'inscription ou renseigments) 


#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#

@app.route('/')
def welcome():
    acc = "/var/lib/asterisk/sounds/custom/Audio/acceuil-eng-fr"
    return acc


#?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#

@app.route('/langues')
def choixLang():
    global lang
    lang = request.args.get('lang')
    if lang == '1':
        return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Inscription-fr"
    elif lang == '2':
        return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Inscription-eng"
    return 'Choix de langue non prise en compte'

#?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#

@app.route('/objectifs')
def choixObjectif():
    global lang
    global objectifs
    objectifs = request.args.get('objectif')
    
    if lang == '1':
        if objectifs == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/"
        elif objectifs == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/"
        return "CHOIX D'OBJECTIF NON PRISE EN COMPTE"
    elif lang == '2':
        if objectifs == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/"
        elif objectifs == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/"
        return "CHOIX D'OBJECTIF NON PRISE EN COMPTE"
    return "CHOIX DE LANGUE NON PRISE EN COMPTE"

#?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#

@app.route('/buts')
def choixButs():
    global lang
    global objectifs
    global buts
    buts = request.args.get('but')

    if lang == '1':
        if objectifs == '1':
            if buts == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
            elif buts == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-LPro-fr"
            elif buts == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
            return "CHOIX DE BUTS NON PRISE EN CHARGE"
        elif objectifs == '2':
            if buts == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/"
            elif buts == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/"
            elif buts == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/"
            return "CHOIX DE BUTS NON PRISE EN CHARGE"
        return "CHOIX DE OBJECTIFS NON PRISE EN CHARGE"
    elif lang == '2':
        if objectifs == '1':
            if buts == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
            elif buts == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-LPro-eng"
            elif buts == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
            return "CHOIX DE BUTS NON PRISE EN COMPTE"
        elif objectifs == '2':
            if buts == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/"
            elif buts == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/"
            elif buts == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/"
            return "CHOIX DE BUTS NON PRISE EN CHARGE"
        return "CHOIX DE OBJECTIFS NON PRISE EN COMPTE"
    return "CHOIX DE LANGUE NON PRISE EN COMPTE"


#?-----------------------------+++++++++++++++++++++++++CHOIX DE RENSEIGNEMENTS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE RENSEIGNEMENTS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE RENSEIGNEMENTS+++++++++++++++++++++++---------------------?#

@app.route('/renseignements')
def choixRenseignements():
    global lang
    global objectifs
    global renseignements
    renseignements = request.args.get('renseignement')

    if lang == '1':
        if objectifs == '1':
            if renseignements == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
            elif renseignements == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-LPro-fr"
            elif renseignements == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
            return "CHOIX DE PARCOURS NON PRISE EN CHARGE"
        return "CHOIX DE PARCOURS NON PRISE EN CHARGE"
    elif lang == '2':
        if renseignements == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
        elif renseignements == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-LPro-eng"
        elif renseignements == '3':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"
    return "CHOIX DE LANGUE NON PRISE EN COMPTE"
