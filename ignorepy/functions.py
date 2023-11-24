from app import app
from config import db
from models import Inscription
from flask import redirect, render_template, jsonify, request

@app.route('/findd', methods=['GET', 'POST'])
def get_all():
    try:
        call_all = Inscription.query.all()
        data = [{"id": call_all.id, "caller ID": call_all.callerId, 
                 "Langue": call_all.lang,"Parcour": call_all.parcours, 
                 "Domaine": call_all.domaine, "Filière": call_all.filiere, 
                 "Date": call_all.date, "Heure": call_all.hour, "Tepms":call_all.temps}]
        
        
        response = jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()
    
@app.route('/finddd', methods=['GET', 'POST'])
def get_count():
    try:
        call_all = Inscription.query.all()
        data = [{"id": call_all.id, "caller ID": call_all.callerId, 
                 "Langue": call_all.lang,"Parcour": call_all.parcours, 
                 "Domaine": call_all.domaine, "Filière": call_all.filiere, 
                 "Date": call_all.date, "Heure": call_all.hour, "Tepms":call_all.temps}]
        
        #num_count =  
        lang_count = ['Français', 'Anglais']
        nob_lang = Inscription.query(Inscription).fliter(Inscription.lang.in_(lang_count)).count()
        print("x_x_x_x_x_x_x_x_x_x : ", nob_lang)
        parcours_count = ['BTS', 'Licence Professionelle' , 'Licence du Soir' ]
        domaine_count = ['Tertaire', 'Technologique' , 
                         'Sciences et Technologies' , 'Sciences de l\'Homme et de la societé',
                         'Sciences Economiques et de Gestions']  
        #filiere_count = ['', '' , '' ]  
        #date_count =  
        #hour_count = 
        #temps_count =  
        response = jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/find/<int:id>', methods=['GET', 'POST'])
def get_by_id():
    try:
        idCall = Inscription.querry.filter_by(id = id).first()
        data = {"id": idCall.id, "caller ID": idCall.callerId, "Langue": idCall.lang,
                 "Parcour": idCall.parcours, "Domaine": idCall.domaine, 
                 "Filière": idCall.filiere, "Date": idCall.date, 
                 "Heure": idCall.hour, "Tepms":idCall.temps}
        response =jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()
