from config import db
from datetime import date 

class Inscription(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    callerId = db.Column(db.String(100), nullable = False)
    lang = db.Column(db.String(100), nullable = False)
    parcour = db.Column(db.String(100), nullable = False)
    domaine = db.Column(db.String(100), nullable = False)
    filiere = db.Column(db.String(100), nullable = False)
    #modalite = db.Column(db.Integer, nullable = False)
    #date = db.Column(db.Date, nullable = False)