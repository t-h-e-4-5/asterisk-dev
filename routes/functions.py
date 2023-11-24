from app import app
from config import db
from models import Inscription
from flask import render_template, redirect, request, jsonify

@app.route('/all')
def get_all():
    try:
        inscrit = Inscription.query.all()
        data = [{"id": inscrit.id, "caller ID": inscrit.callerId, 
                 "Langue": inscrit.lang,"Parcour": inscrit.parcour, 
                 "Domaine": inscrit.domaine, "Filière": inscrit.filiere, 
                 "Date": inscrit.date, "Heure": inscrit.hour, "Tepms":inscrit.temps} for inscrit in inscritl]
        resultat = jsonify(data)
        return resultat
    except Exception as e:
        print(e)
        #return render_template('erreur.html')
        return redirect('/erreur')
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/update', methods = ['POST'])
def update():
    try:
        data = request.form
        id = data["id"]
        calllerId = data["calllerId"]
        lang = data["lang"]
        parcour = data["parcour"]
        domaine = data["domaine"]
        filiere = data["filiere"]
        modalite = data["modalite"]
        insscrit_id = Inscription.query.filter_by(id=id).first()
        if id and lang and parcour and domaine and filiere and modalite and request.method == 'POST':
            insscrit_id.lang = lang
            insscrit_id.parcour = parcour
            insscrit_id.domaine = domaine
            insscrit_id.filiere = filiere
            insscrit_id.modalite = modalite
            db.session.commit()
            return redirect('/dashboard')
    except Exception as e:
        print(e)
        #return render_template ('erreur.html')
        return redirect ('/erreur')
    finally:
        db.session.rollback()
        db.session.close()

@app.route('/delete')
def delete():
    try:
        data = request.form
        id = data['id']
        inscrit_id = Inscription.query.filter_by(id=id).first()
        db.session.delete(inscrit_id)
        db.session.commit()
        resultat = jsonify("Succes")
        return redirect('/dashboard')
    except Exception as e:
        print(e)
        #return render_template('erreur.html')
        return redirect('/erreur')
    finally:
        db.session.rollback()
        db.session.close()



@app.route('/ok', methods=['GET', 'POST'])
def get_count():
    try:
        # Compter les inscriptions en Licence Professionnelle par date
        count_by_date = (
            db.session.query(func.count(Inscription.id).label('nombre_inscriptions'), func.date(Inscription.date).label('date'))
            .filter(Inscription.filiere == 'Licence Professionnelle')
            .group_by(func.date(Inscription.date))
            .all()
        )

        # Construire la réponse JSON
        data = []
        for row in count_by_date:
            data.append({
                "date": row.date.strftime("%Y-%m-%d"),
                "nombre_inscriptions": row.nombre_inscriptions
            })

        response = jsonify(data)
        return response
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()