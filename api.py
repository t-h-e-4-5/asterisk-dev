from app import app
from config import db
from flask import jsonify, request


@app.route('/')
def default():
    return "/var/lib/asterisk/sounds/custom/fr/bienvenu"

global lang              # Variable globale pour stocker la valeur de lang
global profil            # Variable globale pour stocker la valeur de profil
global categorie         # Variable globale pour stocker la valeur de categorie
global humain            # Variable globale pour stocker la valeur de humain
global agriE             # Variable globale pour stocker la valeur de agriE
global environ           # Variable globale pour stocker la valeur de environ
global symptomeFiver     # Variable globale pour stocker la valeur de symptomeFiver
global symptomeVomi      # Variable globale pour stocker la valeur de symptomeVomi
global symptomeDiarh     # Variable globale pour stocker la valeur de symptomeDiarh
global callerID          # Variable globale pour stocker la valeur de callerID

#?-----------------------------+++++++++++++++++++++++++CHOIX DES LANGUES+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DES LANGUES+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DES LANGUES+++++++++++++++++++++++---------------------?#
@app.route('/langues')
def choixLang():
    global lang
    lang = request.args.get('lang') # Utilisation de la variable globale lang
    if lang == '1':
        return "/var/lib/asterisk/sounds/custom/fr/profil"
    elif lang == '2':
        return "/var/lib/asterisk/sounds/custom/eng/profil"
    return 'Choix de langue non prise en compte'

#?-----------------------------+++++++++++++++++++++++++CHOIX DES PROFILS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DES PROFILS+++++++++++++++++++++++---------------------?#
#?-----------------------------+++++++++++++++++++++++++CHOIX DES PROFILS+++++++++++++++++++++++---------------------?#

@app.route('/profils')
def champProfil():
    global lang
    global profil
    profil = request.args.get('profil')

    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3': #! Profil (Agent de santé, Association villageoise, Autres)
            return "/var/lib/asterisk/sounds/custom/fr/categorie"
        return "Choix de profil non prise en copmte"

    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3': #! Profil (Agent de santé, Association villageoise, Autres)
            return "/var/lib/asterisk/sounds/custom/eng/categorie"
        return "Choix de profil non prise en copmte"
    return 'Choix de langue non prise en compte'

@app.route('/categories')
def champCategorie():
    global lang
    global profil
    global categorie
    categorie =request.args.get('categorie')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '1': #! Categorie (Agriculture/Elevage)
                return "/var/lib/asterisk/sounds/custom/fr/agri" #! lang = fr(1), profil = 1.2.3, categorie = Agiculture/Elevage(1)
            elif categorie =='2': #! Categorie Environement
                return "/var/lib/asterisk/sounds/custom/fr/envir" #! lang = fr(1), profil = 1.2.3, categorie = Environement(2)
            elif categorie =='3': #! Humaine
                return "/var/lib/asterisk/sounds/custom/fr/humain" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
        return "Choix de profil non pris en compte" 
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '1': #! Categorie (Agriculture/Elevage)
                return "/var/lib/asterisk/sounds/custom/eng/agri" #! lang = fr(1), profil = 1.2.3, categorie = Agiculture/Elevage(1)
            elif categorie =='2': #! Categorie Environement
                return "/var/lib/asterisk/sounds/custom/eng/envir" #! lang = fr(1), profil = 1.2.3, categorie = Environement(2)
            elif categorie =='3': #! Humaine
                return "/var/lib/asterisk/sounds/custom/eng/humain" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
        return "Choix de profil non pris en compte" 
    return 'Choix de la langue non prise en compte'

@app.route('/agri/elevege')
def champAgriEle():
    global lang
    global profil
    global categorie
    global agriE
    agriE = request.args.get('agriEl')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '1':
                if agriE == '1' or agriE == '2':
                    return '/var/lib/asterisk/sounds/custom/fr/bye'
                return "Choix de agriE non prise en compte"
            return 'Choix de categorie non prise en compte'
        return "Choix de profil non prise en charge"
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '1':
                if agriE == '1' or agriE == '2':
                    return '/var/lib/asterisk/sounds/custom/eng/bye'
                return "Choix de agriE non prise en compte"
            return 'Choix de categorie non prise en compte'
        return "Choix de profil non prise en charge"
    return 'Choix de la langue non prise en compte' 

@app.route('/envir')
def champEnve():
    global lang
    global profil
    global categorie
    global environ
    environ = request.args.get('envi')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '2':
                if environ == '1' or environ == '2' or environ == '3' or environ == '4' or environ == '5':
                    return '/var/lib/asterisk/sounds/custom/fr/bye'
                return "Choix de environ non prise en compte"
            return 'Choix de categorie non prise en compte'
        return "Choix de profil non prise en charge"
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie == '2':
                if environ == '1' or environ == '2' or environ == '3' or environ == '4' or environ == '5':
                    return '/var/lib/asterisk/sounds/custom/eng/bye'
                return "Choix de environ non prise en compte"
            return 'Choix de categorie non prise en compte'
        return "Choix de profil non prise en charge"
    return 'Choix de la langue non prise en compte' 

@app.route('/humains')
def champHumain():
    global lang
    global profil
    global categorie
    global humain
    humain =request.args.get('humain')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '1' or humain == '4' or humain == '5' or humain == '6' or humain == '7' or humain == '8':
                    return "/var/lib/asterisk/sounds/custom/fr/bye" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                elif humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    return "/var/lib/asterisk/sounds/custom/fr/fever" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '1' or humain == '4' or humain == '5' or humain == '6' or humain == '7' or humain == '8':
                    return "/var/lib/asterisk/sounds/custom/eng/bye" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                elif humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    return "/var/lib/asterisk/sounds/custom/eng/fever" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
            return "Choix de categorie non prise en compte"
        return "Choix de profil non pris en compte"
    return "Choix de langue non prise en compte"

@app.route('/symptomeFiver')
def champSymptomeFiver():
    global lang
    global profil
    global categorie
    global humain
    global symptomeFiver
    symptomeFiver =request.args.get('symptomeFiver')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeFiver == '1' or symptomeFiver =='2':
                        return "/var/lib/asterisk/sounds/custom/fr/vomi" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeFiver non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeFiver == '1' or symptomeFiver =='2':
                        return "/var/lib/asterisk/sounds/custom/eng/vomi" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeFiver non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    return "Choix de langue non prise en compte"
    
@app.route('/symptomeVomi')
def champSymptomeVomi():
    global lang
    global profil
    global categorie
    global humain
    global symptomeVomi
    symptomeVomi =request.args.get('symptomeVomi')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeVomi == '1' or symptomeVomi =='2':
                        return "/var/lib/asterisk/sounds/custom/fr/diarh" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeVomi non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeVomi == '1' or symptomeVomi =='2':
                        return "/var/lib/asterisk/sounds/custom/eng/diarh" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeVomi non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    return "Choix de langue non prise en compte"
    
@app.route('/symptomeDiarh')
def champSymptomeDiarh():
    global lang
    global profil
    global categorie
    global humain
    global symptomeDiarh
    symptomeDiarh =request.args.get('symptomeDiarh')
    if lang == '1':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeDiarh == '1' or symptomeDiarh =='2':
                        return "/var/lib/asterisk/sounds/custom/fr/bye" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeDiarh non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    elif lang == '2':
        if profil == '1'or profil == '2'or profil == '3':
            if categorie =='3': #! Humaine
                if humain == '2' or humain == '3' or humain == '9' or humain == '10':
                    if symptomeDiarh == '1' or symptomeDiarh =='2':
                        return "/var/lib/asterisk/sounds/custom/eng/bye" #! lang = fr(1), profil = 1.2.3, categorie = Humaine(3)
                    return "Choix de symptomeDiarh non prise en compte"
                return "Choix de humain non prise en compte"
            return "Choix de categorie non pris en compte" 
        return "Choix de profil non pris en compte" 
    return "Choix de langue non prise en compte"

@app.route('/caller')
def NumID():
    global callerID 
    callerID = request.args.get('caller_number')
    print(callerID)
    return 'ID'



@app.route('/conca')
def champConcatenation():
    global lang              # Recuperation de la variable 
    global profil            # Recuperation de la variable 
    global categorie         # Recuperation de la variable 
    global humain            # Recuperation de la variable 
    global agriE             # Recuperation de la variable 
    global environ           # Recuperation de la variable 
    global symptomeFiver     # Recuperation de la variable 
    global symptomeVomi      # Recuperation de la variable 
    global symptomeDiarh     # Recuperation de la variable 
    global callerID          # Recuperation de la variable 

    print (' ==>  Champ lang : ',lang, '\n'
        ' ==>  Champ profil : ' ,profil, '\n'
        ' ==>  Champ categorie : ' ,categorie, '\n'
        ' ==>  Champ humain : ' ,humain, '\n'
        ' ==>  Champ Agriculture/Elevage : ' ,agriE, '\n'
        ' ==>  Champ Environement : ' ,environ, '\n'
        ' ==>  Champ Symptome Fièvre : ' ,symptomeFiver, '\n'
        ' ==>  Champ Symptome Vomisement : ' ,symptomeVomi, '\n'
        ' ==>  Champ Symptome Diarrhée : ' ,symptomeDiarh, '\n',
        ' ==>  Caller ID : ' ,callerID, '\n'
        ' ==>  FIN')
    return 'Verry good'


if (__name__ == '__main__'):
    app.run(debug=True,port=8080, host='0.0.0.0')
