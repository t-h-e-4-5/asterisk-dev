from config import db
#from datetime import date 
#from flask_security import Security, SQLAlchemyUserDatastore
from app import app

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
"""
roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role_id')))



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable = False)
    active = db.Column(db.Boolean)
    confirme_at = db.Column(db.DateTime)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
"""