from app import app
from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] ='azertypically'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Password*4500@localhost/asteriskAPI"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)