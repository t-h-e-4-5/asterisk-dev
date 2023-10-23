#-----------------------------+++++++++++++++++++++++++D . E . B . U . T+++++++++++++++++++++++---------------------?#

#?-----------------------------+++++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++IMPORTATIONS+++++++++++++++++++++++---------------------?#
from app import app
from config import db
from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
from models import Inscription
from datetime import date
import matplotlib.pyplot as plt
import io
import base64
import functions


app.app_context().push()
#db.drop_all()
#db.create_all()
#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++DECLARATIONS DES VARIABLE GLOBALES+++++++++++++++++++++++---------------------?#


global lang                   # Variable globale pour stocker le choix de la langue
global parcours               # Variable globale pour stocker le choix du parcours
global domaine                # Variable globale pour stocker le choix du domaine
#global LpDomaine              # Variable globale pour stocker le choix du domaine de la Licence Professionnelle
#global LSoirDomaine           # Variable globale pour stocker le choix du domaine de la Licence du soir
global btsFiliere             # Variable globale pour stocker le choix de la filière au BTS
global LpFiliere              # Variable globale pour stocker le choix de la filière de la Licence Professionnelle 
global LSoirFiliere           # Variable globale pour stocker le choix de la filière de la Licence du soir
global callerID               # Variable globale pour stocker le numéro de l'appellant 
global dateCall               # Variable globale pour stocker la date de l'appel 
global duree                  # Variable globale pour stocker la durée de l'appel 
global heur                  # Variable globale pour stocker l'heure de l'appel 

#global filièreBts             # Variable globale pour stocker le choix des filières de BTS
#global filièreLicencePro      # Variable globale pour stocker le choix des filières de Licence Professionnelle 
#global filièreLicenceSoir     # Variable globale pour stocker le choix des filières de Licence du Soir


#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++ B . I . E . N . V . E . N . U . E +++++++++++++++++++++++---------------------?#

@app.route('/')
def welcome():
    #fr = "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Acceuil-fr"
    #eng = "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Acceuil-eng"
    acc = "/var/lib/asterisk/sounds/custom/Audio/acceuil-eng-fr"
    return acc
    #return fr,eng
    #return f"French Audio: {fr}\nEnglish Audio: {eng}"



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

#?-----------------------------+++++++++++++++++++++++++CHOIX DE PARCOURS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE PARCOURS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE PARCOURS+++++++++++++++++++++++---------------------?#

@app.route('/parcours')
def choixParcours():
    global lang
    global parcours
    parcours = request.args.get('parcour')

    if lang == '1':
        if parcours == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
        elif parcours == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-LPro-fr"
        elif parcours == '3':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Domaine-Bts-fr"
        return "CHOIX DE PARCOURS NON PRISE EN CHARGE"
    elif lang == '2':
        if parcours == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
        elif parcours == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-LPro-eng"
        elif parcours == '3':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Domaine-Bts-LSoir-eng"
        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"
    return "CHOIX DE LANGUE NON PRISE EN COMPTE"


#?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE DOMAINE+++++++++++++++++++++++---------------------?#

@app.route('/domaines')
def choixDomaine():
    global lang
    global parcours
    global domaine
    domaine = request.args.get('domain')

    if lang == '1':
        if parcours == '1':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Tertiaire-Bts-fr"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Technologique-Bts-fr"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '2':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Sciences-Technologie-LPro-fr"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Science-homme-LPro-fr"
            elif domaine == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Science-Economique-LPro-fr"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '3':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Tertiaire-LSoir-fr"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Technologiques-LSoir-fr"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"
    elif lang == '2':
        if parcours == '1':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Tertiaire-Bts-eng"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Technologique-Bts-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '2':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Sciences-Technologie-LPro-en"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Science-homme-LPro-eng"
            elif domaine == '3':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Science-Economique-LPro-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '3':
            if domaine == '1':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Tertiaire-LSoir-eng"
            elif domaine == '2':
                return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Technologiques-LSoir-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"
    return 'CHOIX DE LANGUE NON PRISE EN COMPTE'


#?-----------------------------+++++++++++++++++++++++++CHOIX DE FILIERE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE FILIERE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DE FILIERE+++++++++++++++++++++++---------------------?#

@app.route('/filieres')
def choixFiliere():
    global lang
    global parcours
    global domaine
    global filiere
    filiere = request.args.get('filier')

    if lang == '1':
        if parcours == '1':
            if domaine == '1':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4' or filiere == '5' or filiere == '6' or filiere == '7' or filiere == '8' or filiere == '9':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-Bts-fr"
                return ""
            elif domaine == '2':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-Bts-fr"
                return ""
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '2':
            if domaine == '1':
                if filiere == '1'or filiere == '2':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-LPro-fr"
                return ""
            elif domaine == '2':
                if filiere == '1':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-LPro-fr"
                return ""
            elif domaine == '3':
                if filiere == '1'or filiere == '2' or filiere == '3':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-LPro-fr"
                return ""
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '3':
            if domaine == '1':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-LSoir-fr"
                return ""
            elif domaine == '2':
                if filiere == '1'or filiere == '2':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Frais-Date-LSoir-fr"
                return ""
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"

        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"

    elif lang == '2':
        if parcours == '1':
            if domaine == '1':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4' or filiere == '5' or filiere == '6' or filiere == '7' or filiere == '8' or filiere == '9':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-Bts-eng"
            elif domaine == '2':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-Bts-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '2':
            if domaine == '1':
                if filiere == '1'or filiere == '2':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-LPro-eng"
            elif domaine == '2':
                if filiere == '1':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-LPro-eng"
            elif domaine == '3':
                if filiere == '1'or filiere == '2' or filiere == '3':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-LPro-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"
        elif parcours == '3':
            if domaine == '1':
                if filiere == '1'or filiere == '2' or filiere == '3' or filiere == '4':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-LSoir-eng"
            elif domaine == '2':
                if filiere == '1'or filiere == '2':
                    return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Frais-Date-LSoir-eng"
            return "CHOIX DE DOMAINE NON PRISE EN COMPTE"

        return "CHOIX DE PARCOURS NON PRISE EN COMPTE"
        
    return 'CHOIX DE LANGUE NON PRISE EN COMPTE'



#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++LES INFORMATIONS SUR FRAIS, TENUE, DATE DE RENTRÉE+++++++++++++++++++++++---------------------?#

@app.route('/information')
def informati():
    global lang
    global parcours
    if lang == '1':
        if parcours == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Dossiers-fr" 
        if parcours == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Dossiers-fr"
        if parcours == '3':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-fr/Dossiers-fr"
    elif lang == '2':
        if parcours == '1':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Dossiers-eng"
        if parcours == '2':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Dossiers-eng"
        if parcours == '3':
            return "/var/lib/asterisk/sounds/custom/Audio/gsm-eng/Dossiers-eng"
    return 'Choix de langue non prise en compte'


#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU NUMERO D'APPELANT+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU NUMERO D'APPELANT+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU NUMERO D'APPELANT+++++++++++++++++++++++---------------------?#



#@app.route('/caller')
#def NumID():
    #global callerID 
    #callerID = request.args.get('callerNum')
    #print(callerID)
    #return 'GOOD'

#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU TEMPS ET CONVERSION EN MINUTE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU TEMPS ET CONVERSION EN MINUTE+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++RECUPERATION DU TEMPS ET CONVERSION EN MINUTE+++++++++++++++++++++++---------------------?#

@app.route('/time')
def dateTime():
    global dateCall
    global duree
    global heur
    global callerID 
    callerID = request.args.get('callerNum')
    duree = request.args.get('tim')
    dateCall = request.args.get('dat')
    heur = request.args.get('heureD')
    print(duree)
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
    input_seconds = duree
    formatted_time = convert_to_minutes_seconds(input_seconds)
    duree = convert_to_minutes_seconds(input_seconds)
    print(f"Temps formaté : {formatted_time}")
    print(f"Temps formaté : {duree}")
    return 'GOOD'

#?-----------------------------+++++++++++++++++++++++++INFORMATIONS QUI SERA ENREGISTRÉ DANS LA DB+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++INFORMATIONS QUI SERA ENREGISTRÉ DANS LA DB+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++INFORMATIONS QUI SERA ENREGISTRÉ DANS LA DB+++++++++++++++++++++++---------------------?#




@app.route('/db')
def add_db():
    global lang                   # Variable globale pour stocker le choix de la langue    
    global parcours               # Variable globale pour stocker le choix du parcours    
    global domaine                # Variable globale pour stocker le choix du domaine    
    global btsFiliere             # Variable globale pour stocker le choix de la filière au BTS    
    global LpFiliere              # Variable globale pour stocker le choix de la filière de la Licence Professionnelle     
    global LSoirFiliere           # Variable globale pour stocker le choix de la filière de la Licence du soir    
    global callerID               # Variable globale pour stocker le numéro de l'appellant 
    global dateCall               # Variable globale pour stocker la date de l'appel 
    global duree                  # Variable globale pour stocker la durée de l'appel

    if lang == '1':
        dbLang = 'Français'
        if parcours == '1':
            dbParcours = "BTS"
            if domaine == '1':
                dbDomaine= "Tertaire"
                if filiere == '1':
                    dbFiliere = "BTS Sécrétaire de Direction"
                elif filiere == '2':
                    dbFiliere = "BTS Assistant de gestion PME-PMI"
                elif filiere == '3':
                    dbFiliere = "BTS Action Commerciale et force de Vente"
                elif filiere == '4':
                    dbFiliere = "BTS Communication des Entreprises"
                elif filiere == '5':
                    dbFiliere = "BTS Commerce International"
                elif filiere == '6':
                    dbFiliere = "BTS Finance Banque"
                elif filiere == '7': 
                    dbFiliere = "BTS Comptabilité et Gestion des Entreprises"
                elif filiere == '8':
                    dbFiliere = "BTS Gestion des Ressources Humaines"
                elif filiere == '9':
                    dbFiliere = "BTS Transport Logistique et Transit"
            elif domaine == '2':
                dbDomaine= "Technologique"
                if filiere == '1':
                    dbFiliere = "BTS Adminstrateur de Réseaux Locaux"
                elif filiere == '2':
                    dbFiliere = "BTS Développeur d'Applications"
                elif filiere == '3':
                    dbFiliere = "BTS Télécommunications et Réseaux"
                elif filiere == '4':
                    dbFiliere = "BTS Maintenance Informaique et Réseaux"
        elif parcours == '2':
            dbParcours = "Licence Professionelle"
            if domaine == '1':
                dbDomaine= "Sciences et Technologies"
                if filiere == '1':
                    dbFiliere = "Génie Logiciel"
                elif filiere == '2':
                    dbFiliere = "Systèmes et Réseaux"
            if domaine == '2':
                dbDomaine= "Sciences de l'Homme et de la societé"
                if filiere == '1':
                    dbFiliere = "Communication des Organisations"
            if domaine == '3':
                dbDomaine= "Sciences Economiques et de Gestions"
                if filiere == '1':
                    dbFiliere = "Comptabilité et Finances"
                elif filiere == '2':
                    dbFiliere = "Gestions Commerciale"
                elif filiere == '3':
                    dbFiliere = "Managements des Resources Humaines"
        elif parcours == '3':
            dbParcours = "Licence du Soir"
            if domaine == '1':
                dbDomaine= "Tertaire"
                if filiere == '1':
                    dbFiliere = "Management des Ressources"
                elif filiere == '2':
                    dbFiliere = "Management International"
                elif filiere == '3':
                    dbFiliere = "Communication et Relation Publique"
                elif filiere == '4':
                    dbFiliere = "Audit et Contrôle de Gestion"
            elif domaine == '2':
                dbDomaine= "Technologique"
                if filiere == '1':
                    dbFiliere = "Réseaux et Télécomunication option Administration et Sécurité des Réseaux d'entreprises"
                elif filiere == '2':
                    dbFiliere = "Génie Lociel"
    elif lang == '2':
        dbLang = 'Anglais'
        if parcours == '1':
            dbParcours = "BTS"
            if domaine == '1':
                dbDomaine= "Tertaire"
                if filiere == '1':
                    dbFiliere = "BTS Sécrétaire de Direction"
                elif filiere == '2':
                    dbFiliere = "BTS Assistant de gestion PME-PMI"
                elif filiere == '3':
                    dbFiliere = "BTS Action Commerciale et force de Vente"
                elif filiere == '4':
                    dbFiliere = "BTS Communication des Entreprises"
                elif filiere == '5':
                    dbFiliere = "BTS Commerce International"
                elif filiere == '6':
                    dbFiliere = "BTS Finance Banque"
                elif filiere == '7': 
                    dbFiliere = "BTS Comptabilité et Gestion des Entreprises"
                elif filiere == '8':
                    dbFiliere = "BTS Gestion des Ressources Humaines"
                elif filiere == '9':
                    dbFiliere = "BTS Transport Logistique et Transit"
            elif domaine == '2':
                dbDomaine= "Technologique"
                if filiere == '1':
                    dbFiliere = "BTS Adminstrateur de Réseaux Locaux"
                elif filiere == '2':
                    dbFiliere = "BTS Développeur d'Applications"
                elif filiere == '3':
                    dbFiliere = "BTS Télécommunications et Réseaux"
                elif filiere == '4':
                    dbFiliere = "BTS Maintenance Informaique et Réseaux"
        elif parcours == '2':
            dbParcours = "Licence Professionelle"
            if domaine == '1':
                dbDomaine= "Sciences et Technologies"
                if filiere == '1':
                    dbFiliere = "Génie Logiciel"
                elif filiere == '2':
                    dbFiliere = "Systèmes et Réseaux"
            if domaine == '2':
                dbDomaine= "Sciences de l'Homme et de la societé"
                if filiere == '1':
                    dbFiliere = "Communication des Organisations"
            if domaine == '3':
                dbDomaine= "Sciences Economiques et de Gestions"
                if filiere == '1':
                    dbFiliere = "Comptabilité et Finances"
                elif filiere == '2':
                    dbFiliere = "Gestions Commerciale"
                elif filiere == '3':
                    dbFiliere = "Managements des Resources Humaines"
        elif parcours == '3':
            dbParcours = "Licence du Soir"
            if domaine == '1':
                dbDomaine= "Tertaires"
                if filiere == '1':
                    dbFiliere = "Management des Ressources"
                elif filiere == '2':
                    dbFiliere = "Management International"
                elif filiere == '3':
                    dbFiliere = "Communication et Relation Publique"
                elif filiere == '4':
                    dbFiliere = "Audit et Contrôle de Gestion"
            elif domaine == '2':
                dbDomaine= "Technologique"
                if filiere == '1':
                    dbFiliere = "Réseaux et Télécomunication option Administration et Sécurité des Réseaux d'entreprises"
                elif filiere == '2':
                    dbFiliere = "Génie Lociel"


#!-----------------------------+++++++++++++++++++++++++INFORMATIONS QUI SERA ENREGISTRÉ DANS LA DB+++++++++++++++++++++++---------------------?#
    #dbinfo = f"Boonjour Madame/Monsieur vous vous êtes 
     #       inscrit dans l'institut polytechnique DEFITECH 
      #      {dbLang}\n 
       #     - {dbParcours}\n 
        #    - {dbDomaine}\n 
         #   - {dbFiliere}\n"
    with app.app_context():
        #db.drop_all()
        db.create_all()
        add1 = Inscription(callerId = callerID, lang = dbLang, parcour = dbParcours, domaine = dbDomaine, filiere = dbFiliere, date=dateCall, hour=heur, temps=duree)
        db.session.add(add1)
        db.session.commit()
    #dbinfo = f"Bonjour Madame/Monsieur, vous vous êtes inscrit(e) dans l'institut polytechnique DEFITECH\n- {dbLang}\n- {dbParcours}\n- {dbDomaine}\n- {dbFiliere}\n"
    #print (dbinfo)
    #add1 = Inscription(callerId = callerID, lang = dbLang, parcour = dbParcours, domaine = dbDomaine, filiere = dbFiliere)
    #db.session.add(add1)
    #db.session.commit()
    return 'GOOD'

@app.route('/in')
def index():
    #inscriptions = Inscription.query.all()
    #return render_template('index3.html', inscriptions=inscriptions)
    return render_template('index.html')

@app.route('/plot')
def generate_chart():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    counts = [0] * 12

    inscriptions = Inscription.query.all()
    for inscription in inscriptions:
        month_index = int(inscription.date.split(':')[1]) - 1
        counts[month_index] += 1

    plt.bar(months, counts)
    plt.xlabel('Months')
    plt.ylabel('Number of Inscriptions')
    plt.title('Monthly Inscription Statistics')

    # Convert the plot to an image
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_img = base64.b64encode(img.getvalue()).decode()
    return render_template('ch.html', plot_img=plot_img)


#functions.get_all()

@app.route('/find', methods=['GET'])
def get_alld():
    try:
        call_all = Inscription.query.all()
        data = [{"id": call_al.id, "caller ID": call_al.callerId, 
                 "Langue": call_al.lang,"Parcour": call_al.parcour, 
                 "Domaine": call_al.domaine, "Filière": call_al.filiere, 
                 "Date": call_al.date, "Heure": call_al.hour, "Tepms":call_al.temps} for call_al in call_all]
        response = jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()



@app.route('/test', methods=['GET', 'POST'])
def count():
    try:
        english_count = Inscription.query.filter_by(lang='anglais').count()
        french_count = Inscription.query.filter_by(lang='français').count()
        data = [{french_count,english_count}]

        print("x_x_x_x_x_x_x_x_x_x : ", english_count)
        print("x_x_x_x_x_x_x_x_x_x : ", french_count)

        response = jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()




#if (__name__ == '__main__'):
 #   app.run(debug=True, port=5555, host='0.0.0.0')