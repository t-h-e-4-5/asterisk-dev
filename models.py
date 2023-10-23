from config import db
#from datetime import date 

class Inscription(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    callerId = db.Column(db.String(100), nullable = False)
    lang = db.Column(db.String(100), nullable = False)
    parcour = db.Column(db.String(100), nullable = False)
    domaine = db.Column(db.String(100), nullable = False)
    filiere = db.Column(db.String(100), nullable = False)
    modalite = db.Column(db.String(100), nullable = False)
    # Format 16:08:23 jj:mm:AA || jj=jour mm=mois AA=année(2)
    date = db.Column(db.String(255), nullable = False)
    # Format 10:50:41 hh:mm:ss || hh=heure mm=minute ss=seconde
    hour = db.Column(db.String(255), nullable = False)
    # Format 72s en 1:02 
    temps = db.Column(db.String(255), nullable = False) 