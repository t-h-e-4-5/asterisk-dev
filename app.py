from flask import Flask 
from flask_cors import CORS
#from flask_security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
CORS(app)
