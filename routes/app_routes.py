"""from app import app
from flask import render_template

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/stats')
def stats():
    return render_template('charts.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/erreur')
def erreur():
    return render_template('erreur.html')
"""
from sqlalchemy import create_engine, func, extract, Column, String, Integer, DateTime
from sqlalchemy.orm import session
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from app import app
from flask import render_template, redirect, url_for ,request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import db
import config 
import models
from models import Inscription
"""@app.route('/dashboard')
def dashboard():
    return render_template('index.html')
    #return render_template('home.html')"""




from datetime import datetime










@app.route('/dashboard')
def dashboard():
    # Effectuez une requête pour récupérer le nombre d'appels distincts dans la colonne callerId
    nombre_appels = Inscription.query.distinct(Inscription.callerId).count()
    nombre_annuelle = Inscription.query.filter(Inscription.modalite == 'Annuelle').count()
    data_parcours = Inscription.query.filter(Inscription.parcour == '')

    #nombre_annuelle = Inscription.query.distinct(Inscription.modalite).count()

    return render_template('index.html', nombre_appels=nombre_appels, nombre_annuelle = nombre_annuelle)


@app.route('/stats')
def stats():
    return render_template('charts.html')

@app.route('/modifier_client/<int:id>', methods=['GET', 'POST'])
def modifier_client(id):
    # Récupérez les informations du client en fonction de son ID
    client = models.Inscription.query.get(id)
    if client is not None:
        # Affichez un formulaire prérempli avec les données du client pour la modification
        return render_template('modifier_client.html', client=client)
    else:
        # Gérez le cas où l'ID du client n'existe pas
        redirect(url_for('erreur'))

@app.route('/enregistrer_modification/<int:id>', methods=['POST'])
def enregistrer_modification(id):
    if request.method == 'POST':
        # Récupérez les données du formulaire
        callerId = request.form['callerId']
        lang = request.form['lang']
        parcour = request.form['parcour']
        domaine = request.form['domaine']
        filiere = request.form['filiere']
        modalite = request.form['modalite']
        date = request.form['date']
        hour = request.form['hour']
        temps = request.form['temps']
        # Récupérez les autres attributs de la table de la même manière

        # Récupérez le client en fonction de son ID
        client = models.Inscription.query.get(id)

        if client is not None:
            # Mettez à jour les données du client avec les nouvelles valeurs
            client.callerId = callerId
            client.lang = lang
            client.parcour = parcour
            client.domaine = domaine
            client.filiere = filiere
            client.modalite= modalite
            client.date = date
            client.hour  = hour
            client.temps = temps
            # Mettez à jour les autres attributs de la table de la même manière

            # Enregistrez les modifications dans la base de données
            config.db.session.commit()

            # Redirigez l'utilisateur vers une page de confirmation ou autre
            return redirect(url_for('data'))
        else:
            # Gérez le cas où l'ID du client n'existe pas
            redirect(url_for('erreur'))

@app.route('/supprimer_client/<int:id>', methods=['GET'])
def supprimer_client(id):
    # Recherchez le client en fonction de l'ID
    client = models.Inscription.query.get(id)

    if client:
        # Supprimez le client de la base de données
        config.db.session.delete(client)
        config.db.session.commit()
        return redirect(url_for('data'))
    else:
        return redirect(url_for('erreur'))
@app.route('/data')
def data():
    data = models.Inscription.query.all()
    return render_template('data.html', data=data)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/erreur')
def erreur():
    return render_template('erreur.html')




"""

from sqlalchemy import func
from flask import render_template
from flask import render_template_string

@app.route('/test', methods=['GET', 'POST'])
def count():
    try:
        license_counts = (
            db.session.query(
                func.count(Inscription.id).label('count'),
                func.date(Inscription.date).label('inscription_date')
            )
            .filter(Inscription.parcour == 'Licence Professionnelle')
            .group_by(func.date(Inscription.date))
            .all()
        )

        data = [
            {'date': count.inscription_date.strftime('%Y-%m-%d'), 'count': count.count}
            for count in license_counts
        ]

        print("Counts by date:", data)

        data_str = str(data).replace("'", '"')  # Convertir en chaîne JSON

        script = f
        var options = {{
            chart: {{
                height: 280,
                type: "area"
            }},
            dataLabels: {{
                enabled: true
            }},
            series: [{{
                name: "Series 1",
                data: {data_str}
            }}],
            fill: {{
                type: "gradient",
                gradient: {{
                    shadeIntensity: 1,
                    opacityFrom: 0.7,
                    opacityTo: 0.9,
                    stops: [0, 90, 100]
                }}
            }},
            xaxis: {{
                categories: {data_str}
                    .map(item => item.date)
                    .map(date => `"${{date}}"`),
            }}
        }};

        var chart = new ApexCharts(document.querySelector("#chart"), options);
        chart.render();
        

        return render_template_string(script)
    except Exception as e:
        print(e)
        return render_template('pages-error-404.html')
    finally:
        db.session.rollback()
        db.session.close()
"""
from flask import jsonify, render_template, request, json
from sqlalchemy import text
@app.route('/test', methods=['GET', 'POST'])
def count():
    try:
        english_count = Inscription.query.filter_by(lang='anglais').count()
        french_count = Inscription.query.filter_by(lang='français').count()

        queryLS = '''
        SELECT COUNT(*) AS NombreAp, MONTH(date) AS Mois
        FROM inscription
        WHERE parcour = 'Licence du Soir'
        GROUP BY MONTH(date);
        '''
        queryLPJ = '''
        SELECT COUNT(*) AS NombreAp, MONTH(date) AS Mois, parcour
        FROM inscription
        WHERE parcour = 'Licence Professionnelle'
        GROUP BY MONTH(date), parcour;
        '''
        queryBTS = '''
        SELECT COUNT(*) AS NombreAp, MONTH(date) AS Mois, parcour
        FROM inscription
        WHERE parcour = 'BTS'
        GROUP BY MONTH(date), parcour;
        '''

        #resultLS = db.session.execute(text(queryLS))
        resultLS = db.session.execute(text(queryBTS))
        #resultLPJ = db.session.execute(text(queryLPJ))
        #resultBTS = db.session.execute(text(queryBTS))

        data = []
        for row in resultLS:
            data.append({'NombreAp': row.NombreAp, 'Mois': row.Mois,})
        """for row in resultLPJ:
            data.append({'NombreAp': row.NombreAp, 'Mois': row.Mois})
        for row in resultBTS:
            data.append({'NombreAp': row.NombreAp, 'Mois': row.Mois})"""

        # Création d'une structure JSON serializable
        json_data = json.dumps(data)

        # Ne pas oublier de renvoyer la réponse JSON
        #return jsonify({'english_count': english_count, 'french_count': french_count, 'data': json_data})
        return jsonify({'data': json_data})

    except Exception as e:
        print(e)
        return render_template('erreur.html')
    finally:
        db.session.rollback()
        db.session.close()
