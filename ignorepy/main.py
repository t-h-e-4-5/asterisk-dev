from app import app
from config import db
from flask import jsonify, request


@app.route('/')
def default():
    return "/var/lib/asterisk/sounds/custom/BienvenueAS"

global lang     # Variable globale pour stocker la valeur de lang
global option   # Variable globale pour stocker la valeur de option
global service   # Variable globale pour stocker la valeur de service

@app.route('/langue')
def autreRoute():
    global lang
    lang = request.args.get('lang') # Utilisation de la variable globale lang
    if lang == '1':
        return "/var/lib/asterisk/sounds/custom/Etape1-fr"
    elif lang == '2':
        return "/var/lib/asterisk/sounds/custom/Etape1-en"
    return 'hello-world'



#?-------------------CHOIX DES OPTION


@app.route('/option')
def autre():
    global lang
    global option
    option = request.args.get('option')
    print('------------------------')
    print(lang)
    print('------------------------')
    print(option)
    print('------------------------')
    #?------------FRANCAIS---------------
    #?------------FRANCAIS---------------
    #?------------FRANCAIS---------------
    #?------------FRANCAIS---------------

    if lang == '1':
        if option == '1': #! Rendez-vous
            #return ""
            return "/var/lib/asterisk/sounds/custom/Etape1-en"
        elif option == '2': #! Heures de travail
            return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        elif option == '3': #! Accident
            return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        elif option == '4': #! Conseils
            return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        elif option == '5': #! Maladie
            return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        return "/var/lib/asterisk/sounds/custom/Etape1-fr"
#?------------ENGLISH---------------
#?------------ENGLISH---------------
#?------------ENGLISH---------------
#?------------ENGLISH---------------
    elif lang == '2':
        if option == '1': #! Rendez-vous
            return " /var/lib/asterisk/sounds/custom/eng/bienvenu"
            #return "/var/lib/asterisk/sounds/custom/Etape1-en"
        elif option == '2': #! Heures de travail
            return " /var/lib/asterisk/sounds/custom/eng/bye"
            #return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        elif option == '3': #! Accident
            #return "/var/lib/asterisk/sounds/custom/BienvenueAS"
            return " /var/lib/asterisk/sounds/custom/eng/categorie"
        elif option == '4': #! Conseils
            #return "/var/lib/asterisk/sounds/custom/BienvenueAS"
            return " /var/lib/asterisk/sounds/custom/eng/diarh"
        elif option == '5': #! Maladie
            return " /var/lib/asterisk/sounds/custom/eng/humain"
            #return "/var/lib/asterisk/sounds/custom/BienvenueAS"
        #return "/var/lib/asterisk/sounds/custom/Etape1-fr"
        return "/var/lib/asterisk/sounds/custom/eng/portrait"
    return 'hello-world'

@app.route('/service')
def servicet():
    global lang
    global option
    global service
    service =request.args.get('service')
    print('------------------------')
    print(lang)
    print('------------------------')
    print(option)
    print('------------------------')
    print(service)
    print(service)
    print('------------------------')
    if lang == '1':
        if option == '1':
            if service == '1':
                return "/var/lib/asterisk/sounds/custom/fr/profil" #! lang = fr(1), option = rendez-vous(1), service = cardiologie(1)
            elif service =='2': 
                return "/var/lib/asterisk/sounds/custom/fr/fever" #! lang = fr(1), option = rendez-vous(1), service = Pédiatrie(2)
            elif service =='3': 
                return "/var/lib/asterisk/sounds/custom/fr/vomi" #! lang = fr(1), option = rendez-vous(1), service = Neurologie(3)
            #elif service =='4': 
                #return "" #! lang = fr(1), option = rendez-vous(1), service = Urologie(4)
            #elif service =='5': 
                #return "" #! lang = fr(1), option = rendez-vous(1), service = Généralité(5)
        elif option == '3':
            return "/var/lib/asterisk/sounds/custom/eng/portrait" #! lang = fr(1), option = Accident(1), service = Généralité(5)
    elif lang == '2':
        if option == '1':
            if service == '1':
                return '/var/lib/asterisk/sounds/custom/eng/portrait'
            elif service == '2':
                return '/var/lib/asterisk/sounds/custom/eng/portrait'
        elif option == '3':
            if service == '1':
                return '/var/lib/asterisk/sounds/custom/eng/portrait'
            elif service == '2':
                return '/var/lib/asterisk/sounds/custom/eng/portrait'
        return '/var/lib/asterisk/sounds/custom/eng/portrait'
    return '/var/lib/asterisk/sounds/custom/eng/old.agri_fr'


if (__name__ == '__main__'):
    app.run(debug=True, port=6060, host='0.0.0.0')
