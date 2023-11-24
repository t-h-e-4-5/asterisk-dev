from app import app
from flask_sqlalchemy import SQLAlchemy


#from models import User, Role

app.config['SECRET_KEY'] ='azertypically'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://theo:Password*4500@localhost/asteriskAPI"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
#user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#security = Security(app, user_datastore)






