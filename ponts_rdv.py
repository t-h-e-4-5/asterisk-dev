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
from routes import app_routes, functions

#?-----------------------------+++++++++++++++++++++++++CONNEXION DB+++++++++++++++++++++++---------------------?#
    #?-------------------------+++++++++++++++++++++++++CONNEXION DB+++++++++++++++++++++++----------------?#
app.app_context().push()

#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES+++++++++++++++++++++++---------------------?#
    #?----------------------------++++++++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES++++++++---------------------?#

global pont_1
global pont_2
global pont_3
global pont_4
global pont_5
global pont_6
global callerNum
global time_call
global dateCall
global heur


#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES POUR LES FICHIERS+++++++++++++++++++++++---------------------?#
    #?----------------------------++++++++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES POUR LES FICHIERS+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++DECLARATIONS DES VARIABLES GLOBALES POUR LES FICHIERS+++++++++++++++++++++++---------------------?#

global file_welcome
global fr_file_objectif
global eng_file_objectif
global fr_file_inscription
global eng_file_inscription
global fr_file_renseignement
global eng_file_renseignement
global fr_file_domaine_bts_lps
global eng_file_domaine_bts_lps
global fr_file_domaine_lpj
global eng_file_domaine_lpj
global fr_file_admission
global eng_file_admission
global fr_file_formation
global eng_file_formation
global fr_file_info_date
global eng_file_info_date
global fr_filiere_tertiare_bts
global eng_filiere_tertiare_bts
global fr_filiere_tech_bts
global eng_filiere_tech_bts
global fr_file_filiere_st_lpj
global eng_file_filiere_st_lpj
global fr_file_filiere_shs_lpj
global eng_file_filiere_shs_lpj
global fr_file_filiere_seg_lpj
global eng_file_filiere_seg_lpj
global fr_file_filiere_tertiare_lps
global eng_file_filiere_tertiare_lps
global fr_file_filiere_tech_lps
global eng_file_filiere_tech_lps
global fr_bye
global eng_bye
global fr_file_frais_date_bts
global eng_file_frais_date_bts
global fr_file_frais_date_lpj
global eng_file_frais_date_lpj
global fr_file_faris_date_lps
global eng_file_faris_date_lps
global fr_file_mode_paie
global eng_file_mode_paie
global erreur

file_welcome = "/var/lib/asterisk/sounds/custom/son/Bienvenue"

fr_file_objectif = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_objectifs"
eng_file_objectif = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_objectifs"
fr_file_inscription = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_inscription"
eng_file_inscription = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_inscription"
fr_file_renseignement = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_reseignements"
eng_file_renseignement = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_renseignements"


fr_file_domaine_bts_lps = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_domaine_bts_lps"
eng_file_domaine_bts_lps = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_domaine_bts_lps"
fr_file_domaine_lpj = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_domaine_lpj"
eng_file_domaine_lpj = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_domaine_lpj"
fr_file_admission = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_admission"
eng_file_admission = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_admission"
fr_file_formation = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_formation"
eng_file_formation = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_formation"
fr_file_info_date = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_info_date"
eng_file_info_date = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_info_date"


fr_filiere_tertiare_bts = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_tertiare_bts"
eng_filiere_tertiare_bts = "/var/lib/asterisk/sounds/custom/son/fr_gsm/eng_filiere_tertiaire_bts"
fr_filiere_tech_bts = "/var/lib/asterisk/sounds/custom/son/eng_gsm/fr_filiere_tech_bts"
eng_filiere_tech_bts = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_filiere_tech_bts"
fr_file_filiere_st_lpj = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_st_lpj"
eng_file_filiere_st_lpj = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_filiere_st_lpj"
fr_file_filiere_shs_lpj = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_shs_lpj"
eng_file_filiere_shs_lpj = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_filiere_shs_lpj"
fr_file_filiere_seg_lpj = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_seg_lpj"
eng_file_filiere_seg_lpj = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_filiere_seg_lpj"
fr_file_filiere_tertiare_lps = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_tertiare_lps"
eng_file_filiere_tertiare_lps = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_filiere_tertiare_lps"
fr_file_filiere_tech_lps = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_filiere_tech_lps"
eng_file_filiere_tech_lps = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_fililere_tech_lps"

fr_bye = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_bye"
eng_bye = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_bye"


fr_file_frais_date_bts = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_frais_date_bts"
eng_file_frais_date_bts = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_frais_date_bts"
fr_file_frais_date_lpj = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_frais_date_lpj"
eng_file_frais_date_lpj = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_frais_date_lpj"
fr_file_faris_date_lps = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_frais_date_lps"
eng_file_faris_date_lps = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_frais_date_lps"


fr_file_mode_paie = "/var/lib/asterisk/sounds/custom/son/fr_gsm/fr_mode_payement"
eng_file_mode_paie = "/var/lib/asterisk/sounds/custom/son/eng_gsm/eng_mode_payement"

erreur = "/var/lib/asterisk/sounds/custom/son/erreur"



#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#

@app.route('/')
def welcome():
    return file_welcome

#?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++CHOIX DE LANGUE+++++++++++++++++++++++---------------------?#

@app.route('/pont1')
def choixLang():
    global pont_1
    pont_1 = request.args.get('pont_1')
    if pont_1 == '1': #!FR
        return fr_file_objectif
    elif pont_1 == '2': #!ENG
        return eng_file_objectif
    return erreur

#?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++CHOIX DE L'OBJECTIF+++++++++++++++++++++++---------------------?#

@app.route('/pont2')
def choixObjectif():
    global pont_1
    global pont_2
    pont_2 = request.args.get('pont_2')
    if pont_1 == '1':             #!FR
        if pont_2 == '1':         #!FR  #!INSCRIPTION
            return fr_file_inscription
        elif pont_2 == '2':       #!FR #!RENSEIGNEMENTS
            return fr_file_renseignement
        return erreur
    elif pont_1 == '2':           #!ENG 
        if pont_2 == '1':         #!ENG  #!INSCRIPTION
            return eng_file_inscription
        elif pont_2 == '2':       #!ENG  #!RENSEIGNEMENTS
            return eng_file_renseignement
        return erreur
    return erreur

#?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++CHOIX DE BUTS+++++++++++++++++++++++---------------------?#

@app.route('/pont3')
def choixButs():
    global pont_1
    global pont_2
    global pont_3
    pont_3 = request.args.get('pont_3')

    if pont_1 == '1':             #!FR
        if pont_2 == '1':         #!FR  #!INSCRIPTION
            if pont_3 == '1':     #!FR  #!INSCRIPTION #!BTS
                return fr_file_domaine_bts_lps
            elif pont_3 == '2':   #!FR  #!INSCRIPTION #!LPJ
                return fr_file_domaine_lpj
            elif pont_3 == '3':     #!FR  #!INSCRIPTION #!LPS
                return fr_file_domaine_bts_lps
            return erreur
        elif pont_2 == '2':         #!FR  #!RENSEIGNEMENTS 
            if pont_3 == '1':   #!FR  #!RENSEIGNEMENTS #!ADMISSION
                return fr_file_admission
            elif pont_3 == '2': #!FR  #!RENSEIGNEMENTS #!FORMATIONS
                return fr_file_formation
            elif pont_3 == '3': #!FR  #!RENSEIGNEMENTS #!DATE DE RENTREE
                return fr_file_info_date
            return erreur
        return erreur
    elif pont_1 == '2': #!ENG  
        if pont_2 == '1': #!ENG  #!INSCRIPTION 
            if pont_3 == '1':#!ENG  #!INSCRIPTION #!BTS
                return eng_file_domaine_bts_lps
            elif pont_3 == '2': #!ENG  #!INSCRIPTION #!LPJ
                return eng_file_domaine_lpj
            elif pont_3 == '3': #!ENG  #!INSCRIPTION #!LPS
                return eng_file_domaine_bts_lps
            return erreur
        elif pont_2 == '2':  #!ENG  #!RENSEIGNEMENTS
            if pont_3 == '1': #!ENG  #!RENSEIGNEMENTS #!ADMISSION
                return eng_file_admission
            elif pont_3 == '2': #!ENG  #!RENSEIGNEMENTS #!FORMATION
                return eng_file_formation
            elif pont_3 == '3': #!ENG  #!RENSEIGNEMENTS #!DATE DE RENTRE
                return eng_file_info_date
            return erreur
        return erreur
    return erreur

#?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#

@app.route('/pont4')
def choixDomaine():
    global pont_1
    global pont_2
    global pont_3
    global pont_4
    pont_4 = request.args.get('pont_4')

    if pont_1 == '1':#!FR  
        if pont_2 == '1': #!FR  #!INSCRIPTION
            if pont_3 == '1': #!FR  #!INSCRIPTION #!BTS
                if pont_4 == '1': #!FR  #!INSCRIPTION #!BTS #!TERTIAIRES
                    return fr_filiere_tertiare_bts 
                elif pont_4 == '2': #!FR  #!INSCRIPTION #!BTS #!TECCHNOLIGIES
                    return fr_filiere_tech_bts
                return erreur
            elif pont_3 =='2': #!FR  #!INSCRIPTION #!LPJ
                if pont_4 == '1': #!FR  #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    return fr_file_filiere_st_lpj
                if pont_4 == '2': #!FR  #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    return fr_file_filiere_shs_lpj
                if pont_4 == '3': #!FR  #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIE GESTION
                    return fr_file_filiere_seg_lpj
                return erreur
            elif pont_3 == '3': #!FR  #!INSCRIPTION #!LPS
                if pont_4 == '1': #!FR  #!INSCRIPTION #!LPS #!TERTIAIRES
                    return fr_file_filiere_tertiare_lps
                elif pont_4 == '2': #!FR  #!INSCRIPTION #!LPS #!TECCHNOLIGIES
                    return fr_file_filiere_tech_lps
                return erreur
            return erreur
        elif pont_2 == '2':  #!FR  #!RENSEIGNEMENTS 
            if pont_3 == '1' or pont_3 == '2' or pont_3 == '3': #!FR  #!RENSEIGNEMENTS #! 
                return fr_bye #!----------------------------FIN
            return erreur
        return erreur
    elif pont_1 == '2':#!ENG  
        if pont_2 == '1': #!ENG  #!INSCRIPTION
            if pont_3 == '1': #!ENG  #!INSCRIPTION #!BTS
                if pont_4 == '1': #!ENG  #!INSCRIPTION #!BTS #!TERTIAIRES
                    return eng_filiere_tertiare_bts
                elif pont_4 == '2': #!ENG  #!INSCRIPTION #!BTS #!TECCHNOLIGIES
                    return eng_filiere_tech_bts
                return erreur
            elif pont_3 =='2': #!ENG  #!INSCRIPTION #!LPJ
                if pont_4 == '1': #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    return eng_file_filiere_st_lpj
                if pont_4 == '2': #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    return eng_file_filiere_shs_lpj
                if pont_4 == '3': #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIE GESTION
                    return eng_file_filiere_seg_lpj
                return erreur
            elif pont_3 == '3': #!ENG  #!INSCRIPTION #!LPS
                if pont_4 == '1': #!ENG  #!INSCRIPTION #!LPS #!TERTIAIRES
                    return eng_file_filiere_tertiare_lps
                elif pont_4 == '2': #!ENG  #!INSCRIPTION #!LPS #!TECCHNOLIGIES
                    return eng_file_filiere_tech_lps
                return erreur
            return erreur
        elif pont_2 == '2':  #!ENG  #!RENSEIGNEMENTS 
            if pont_3 == '1' or pont_3 == '2' or pont_3 == '3': #!ENG  #!RENSEIGNEMENTS #! 
                return eng_bye #!----------------------------FIN
            return erreur
        return erreur
    return erreur

#?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#

@app.route('/pont5')
def choixFiliere():
    global pont_1
    global pont_2
    global pont_3
    global pont_4
    global pont_5
    pont_5 = request.args.get('pont_5')

    if pont_1 == '1':#!FR  
        if pont_2 == '1': #!FR  #!INSCRIPTION
            if pont_3 == '1': #!FR  #!INSCRIPTION #!BTS
                if pont_4 == '1': #!FR  #!INSCRIPTION #!BTS #!TERTIAIRES
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3' or pont_5 == '4' or pont_5 == '5' or pont_5 == '6' or pont_5 == '7' or pont_5 == '8' or pont_5 == '9' :
                        return fr_file_frais_date_bts
                    return erreur
                elif pont_4 == '2':  #!FR  #!INSCRIPTION #!BTS #!TECHNOLOGIE
                    if pont_5 == '1'or pont_5 == '2'or pont_5 == '3'or pont_5 == '4':
                        return fr_file_frais_date_bts
                    return erreur
            elif pont_3 == '2': #!FR  #!INSCRIPTION #!LPJ
                if pont_4 == '1':  #!FR  #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    if pont_5 == '1' or pont_5 == '2': 
                        return fr_file_faris_date_lps
                    return erreur
                elif pont_4 == '2': #!FR  #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    if pont_5 == '1' : 
                        return fr_file_faris_date_lps
                    return erreur
                elif pont_4 == '3': #!FR  #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIEQUES GESTIONS
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3':
                        return fr_file_faris_date_lps
                    return erreur
                return erreur
            elif pont_3 == '3': #!FR  #!INSCRIPTION #!LPS 
                if pont_4 == '1': #!FR  #!INSCRIPTION #!LPS #!TERTIAIRES
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3' or pont_5 == '4':
                        return fr_file_faris_date_lps
                    return ''
                elif pont_4 == '2': #!FR  #!INSCRIPTION #!LPS #!TECH
                    if pont_5 == '1' or pont_5 == '2':
                        return fr_file_faris_date_lps
                    return erreur
                return erreur
            return erreur
        return erreur
    elif pont_1 == '2': #!ENG 
        if pont_2 == '1': #!ENG  #!INSCRIPTION
            if pont_3 == '1': #!ENG  #!INSCRIPTION #!BTS
                if pont_4 == '1': #!ENG  #!INSCRIPTION #!BTS #!TERTIAIRES
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3' or pont_5 == '4' or pont_5 == '5' or pont_5 == '6' or pont_5 == '7' or pont_5 == '8' or pont_5 == '9' :
                        return eng_file_frais_date_bts
                    return erreur
                elif pont_4 == '2':  #!ENG  #!INSCRIPTION #!BTS #!TECHNOLOGIE
                    if pont_5 == '1'or pont_5 == '2'or pont_5 == '3'or pont_5 == '4':
                        return eng_file_frais_date_bts
                    return erreur
            elif pont_3 == '2': #!ENG  #!INSCRIPTION #!LPJ
                if pont_4 == '1':  #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    if pont_5 == '1' or pont_5 == '2': 
                        return eng_file_frais_date_lpj
                    return erreur
                elif pont_4 == '2': #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    if pont_5 == '1' : 
                        return eng_file_frais_date_lpj
                    return erreur
                elif pont_4 == '3': #!ENG  #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIEQUES GESTIONS
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3':
                        return eng_file_frais_date_lpj
                    return erreur
                return erreur
            elif pont_3 == '3': #!ENG  #!INSCRIPTION #!LPS 
                if pont_4 == '1': #!ENG  #!INSCRIPTION #!LPS #!TERTIAIRES
                    if pont_5 == '1' or pont_5 == '2' or pont_5 == '3' or pont_5 == '4':
                        return eng_file_faris_date_lps
                    return erreur
                elif pont_4 == '2': #!ENG  #!INSCRIPTION #!LPS #!TECH
                    if pont_5 == '1' or pont_5 == '2':
                        return eng_file_faris_date_lps
                    return erreur
                return erreur
            return erreur
        return erreur
    return erreur

    #! FIN DE LA FONCTION 

#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#

#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES MODALITES DE PAIEMENT+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES MODALITES DE PAIEMENT+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES MODALITES DE PAIEMENT+++++++++++++++++++++++---------------------?#

@app.route('/pont6')
def modalite_paie():
    global pont_1
    global pont_2
    if pont_1 == '1':#!FR
        if pont_2 == '1':#!FR  #!INSCRIPTION 
            return fr_file_mode_paie
        return erreur
    elif pont_1 =='2': #!ENG
        if pont_2 == '1': #!ENG #!INSCRIPTION
            return eng_file_mode_paie
        return erreur
    return erreur
    #! FIN DE LA FONCTION

#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES DOSSIERS D'ADMISSIONS+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES DOSSIERS D'ADMISSIONS+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR LES DOSSIERS D'ADMISSIONS+++++++++++++++++++++++---------------------?#

@app.route('/pont7')
def dossiers_admissions():
    global pont_1
    global pont_2
    global pont_6
    pont_6 = request.args.get('pont_6')
    if pont_1 == '1': #!FR
        if pont_2 == '1': #!FR  #!INSCRIPTION
            return fr_file_admission
        return erreur
    elif pont_1 == '2' :#!ENG
        if pont_2 == '1': #!ENG #!INSCRIPTION
            return eng_file_admission
        return erreur
    return erreur


#?-----------------------------+++++++++++++++++++++++++RECUPERATION DE TEMPS DE L'APPEL+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++RECUPERATION DU NUMERO DE L'APPELANT+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++RECUPERATION DE TEMPS DE L'APPEL+++++++++++++++++++++++---------------------?#

@app.route('/time')
def pont_temps():
    global dateCall
    global time_call
    global heur
    global callerNum
    callerNum = request.args.get('callNum')
    time_call = request.args.get('tim')
    dateCall = request.args.get('dat')
    heur = request.args.get('heureD')
    print(callerNum)
    print(time_call)
    print(dateCall)
    print(heur)
    def convert_to_minutes_seconds(seconds):
        try:
            seconds = int(seconds)  # Convertir en nombre entier si c'est une chaîne
            minutes = seconds // 60
            seconds %= 60
            formatted_time = f"{minutes:02d}:{seconds:02d}"
            return formatted_time
        except ValueError:
            return "Erreur de conversion"

    # Exemple d'utilisation
    input_seconds = time_call
    formatted_time = convert_to_minutes_seconds(input_seconds)
    time_call = convert_to_minutes_seconds(input_seconds)
    print(f"Temps formaté : {formatted_time}")
    print(f"Temps formaté : {time_call}")
    return 'GOOD'
    

#?-----------------------------+++++++++++++++++++++++++RECUPERATION DES DONNEES POUR LA DB+++++++++++++++++++++++---------------------?#
    #?-----------------------------+++++++++++++++++++++++++RECUPERATION DES DONNEES POUR LA DB+++++++++++++++++++++++---------------------?#
        #?-----------------------------+++++++++++++++++++++++++RECUPERATION DES DONNEES POUR LA DB+++++++++++++++++++++++---------------------?#

@app.route('/db')
def add_db():
    global pont_1
    global pont_2
    global pont_3
    global pont_4
    global pont_5
    global pont_6
    global callerNum
    global time_call
    global dateCall
    global heur
    
    if pont_1 == '1': #!FR
        db_lang = "Français"
        if pont_2 =='1': #!FR #!INSCRIPTION
            db_choix = "Inscription"
            if pont_3 == '1': #!FR #!INSCRIPTION #!BTS
                db_parcours = "BTS"
                if pont_4 == '1': #!FR #!INSCRIPTION #!BTS #!TERTAIRES
                    db_domaine = "Tertiaires"
                    if pont_5 == '1': 
                        db_filiere = "BTS Sécrétaire de Direction"
                        if pont_6 == '1':
                            db_modalite ="AZERTY"
                        elif pont_6 == '2':
                            db_modalite ="AZERTY"
                    elif pont_5 == '2':
                        db_filiere = "BTS Assistant de gestion PME-PMI"
                    elif pont_5 == '3':
                        db_filiere = "BTS Action Commerciale et force de Vente"
                    elif pont_5 == '4':
                        db_filiere = "BTS Communication des Entreprises"
                    elif pont_5 == '5':
                        db_filiere = "BTS Commerce International"
                    elif pont_5 == '6':
                        db_filiere = "BTS Finance Banque"
                    elif pont_5 == '7':
                        db_filiere = "BTS Comptabilité et Gestion des Entreprises"
                    elif pont_5 == '8':
                        db_filiere = "BTS Gestion des Ressources Humaines"
                    elif pont_5 == '9':
                        db_filiere = "BTS Transport Logistique et Transit"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!FR #!INSCRIPTION #!BTS #!TECHNOLOGIQUES
                    db_domaine= "Technologiques"
                    if pont_5 == '1':
                        db_filiere = "BTS Adminstrateur de Réseaux Locaux"
                    elif pont_5 == '2':
                        db_filiere = "BTS Développeur d'Applications"
                    elif pont_5 == '3':
                        db_filiere = "BTS Télécommunications et Réseaux"
                    elif pont_5 == '4':
                        db_filiere = "BTS Maintenance Informaique et Réseaux"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
            elif pont_3 == '2': #!FR #!INSCRIPTION #!LPJ 
                db_parcours = "Licence Professionelle"
                if pont_4 == '1': #!FR #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    db_domaine = "Sciences et Technologies"
                    if pont_5 == '1':
                        db_filiere = "Génie Logiciel"
                    elif pont_5 == '2':
                        db_filiere = "Systèmes et Réseaux"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!FR #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    db_domaine = "Sciences de l'Homme et de la societé"
                    if pont_5 == '1':
                        db_filiere = "Communication des Organisations"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '3': #!FR #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIQUES GESTIONS
                    db_domaine = "Sciences Economiques et de Gestions"
                    if pont_5 == '1':
                        db_filiere = "Comptabilité et Finances"
                    elif pont_5 == '2':
                        db_filiere = "Gestions Commerciale"
                    elif pont_5 == '3':
                        db_filiere = "Managements des Resources Humaines"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
            elif pont_3 == '3' : #!FR #!INSCRIPTION #!LPS 
                db_parcours = "Licence du Soir"
                if pont_4 == '1': #!FR #!INSCRIPTION #!LPS #!TERTIAIRE
                    db_domaine = "Tertiaires"
                    if pont_5 == '1':
                        db_filiere = "Management des Ressources"
                    elif pont_5 == '2':
                        db_filiere = "Management International"
                    elif pont_5 == '3':
                        db_filiere = "Communication et Relation Publique"
                    elif pont_5 == '4':
                        db_filiere = "Audit et Contrôle de Gestion"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!FR #!INSCRIPTION #!LPS #!TECHNOLOGIQUE
                    db_domaine = "Technologique"
                    if pont_5 == '1':
                        db_filiere = "Réseaux et Télécomunication option Administration et Sécurité des Réseaux d'entreprises"
                    elif pont_5 == '2':
                        db_filiere = "Génie Lociel"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
    elif pont_1 == '2': #!ENG
        db_lang = "English"
        if pont_2 =='1': #!ENG #!INSCRIPTION
            db_choix = "Registration"
            if pont_3 == '1': #!ENG #!INSCRIPTION #!BTS
                db_parcours = "BTS"
                if pont_4 == '1': #!ENG #!INSCRIPTION #!BTS #!TERTAIRES
                    db_domaine = "Tertiary"
                    if pont_5 == '1': 
                        db_filiere = "BTS Executive Secretary"
                    elif pont_5 == '2':
                        db_filiere = "BTS Assistant of SME-SMI management"
                    elif pont_5 == '3':
                        db_filiere = "BTS Commercial Action and Sales Force"
                    elif pont_5 == '4':
                        db_filiere = "BTS Business Communication"
                    elif pont_5 == '5':
                        db_filiere = "BTS International Trade"
                    elif pont_5 == '6':
                        db_filiere = "BTS Finance Bank"
                    elif pont_5 == '7':
                        db_filiere = "BTS Accounting and Business Management"
                    elif pont_5 == '8':
                        db_filiere = "BTS Human Resources Management"
                    elif pont_5 == '9':
                        db_filiere = "BTS Transport Logistics and Transit"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!ENG #!INSCRIPTION #!BTS #!TECHNOLOGIQUES
                    db_domaine= "Technological"
                    if pont_5 == '1':
                        db_filiere = "BTS Local Network Administrator"
                    elif pont_5 == '2':
                        db_filiere = "BTS Application Developer"
                    elif pont_5 == '3':
                        db_filiere = "BTS Telecommunications and Networks"
                    elif pont_5 == '4':
                        db_filiere = "BTS Computer Maintenance and Networks"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
            elif pont_3 == '2': #!ENG #!INSCRIPTION #!LPJ 
                db_parcours = "Professional License"
                if pont_4 == '1': #!ENG #!INSCRIPTION #!LPJ #!SCIENCE TECH
                    db_domaine = "Science and Technology"
                    if pont_5 == '1':
                        db_filiere = "Software Engineering"
                    elif pont_5 == '2':
                        db_filiere = "Systems and Networks"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!ENG #!INSCRIPTION #!LPJ #!SCIENCE HOMME SOCIETE
                    db_domaine = "Human and social sciences"
                    if pont_5 == '1':
                        db_filiere = "Communication of Organizations"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '3': #!ENG #!INSCRIPTION #!LPJ #!SCIENCE ECONOMIQUES GESTIONS
                    db_domaine = "Economic and Management Sciences"
                    if pont_5 == '1':
                        db_filiere = "Accounting and Finance"
                    elif pont_5 == '2':
                        db_filiere = "Commercial Management"
                    elif pont_5 == '3':
                        db_filiere = "Human Resources Management"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
            elif pont_3 == '3' : #!ENG #!INSCRIPTION #!LPS 
                db_parcours = "Evening License"
                if pont_4 == '1': #!ENG #!INSCRIPTION #!LPS #!TERTIAIRE
                    db_domaine = "Tertiary"
                    if pont_5 == '1':
                        db_filiere = "Resource Management"
                    elif pont_5 == '2':
                        db_filiere = "Management International"
                    elif pont_5 == '3':
                        db_filiere = "Communication and Public Relations"
                    elif pont_5 == '4':
                        db_filiere = "Audit and Management Control"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
                elif pont_4 == '2': #!ENG #!INSCRIPTION #!LPS #!TECHNOLOGIQUE
                    db_domaine = "Technological"
                    if pont_5 == '1':
                        db_filiere = "Networks and Telecommunications option Administration and Security of Corporate Networks"
                    elif pont_5 == '2':
                        db_filiere = "Social Engineering"
                        if pont_6 == '1':
                            db_modalite ="Annuelle"
                        elif pont_6 == '2':
                            db_modalite ="Trimestielle"
                        elif pont_6 == '3':
                            db_modalite = "Mensuelle"
    print(callerNum)
    print(callerNum)
    print(callerNum)
    print(callerNum)
    print(callerNum)
    print(callerNum)
    print(db_filiere)
    print(db_modalite)
    print(db_filiere)
    with app.app_context():
        #db.drop_all() choix = db_choix,
        db.create_all()
        add1 = Inscription(callerId = callerNum, lang = db_lang, parcour = db_parcours, domaine = db_domaine, filiere = db_filiere, modalite = db_modalite, date = dateCall, hour = heur, temps = time_call)
        db.session.add(add1)
        db.session.commit()
    if pont_1 == '1':
        dbinfo = f"Bonjour Madame/Monsieur, vous venez de reserver une place à l'INSTITUT POLYTECHNIQUE DEFITECH dans le parcours {db_parcours}, domaine {db_domaine} filière {db_filiere} et votre mode de paiement des frais scolaire sera {db_modalite}\nMerci de votre confiance\nAvec DEFITECH votre reusite notre priorité"
    elif pont_1 == '2':
        dbinfo = f"Hello Madam / Sir, you have just booked a place at the POLYTECHNIC INSTITUTE DEFITECH in the course {db_parcours}, domain {db_domaine} sector {db_filiere} and your method of payment for school fees will be {db_modalite}\nThank you for your trust\nWith DEFITECH your success is our priority"
    print(dbinfo)
    return "OK"


#?---WEB--?#

app_routes.dashboard()
app_routes.stats()
app_routes.data()
app_routes.profile()
app_routes.contact()
app_routes.login()
app_routes.erreur()





















if (__name__ == '__main__'):
    app.run(debug=True, port=5555, host='0.0.0.0')
