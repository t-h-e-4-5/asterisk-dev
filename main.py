from app import app
from config import db
from flask import jsonify, request

@app.route('/api/v1/')
def index():
    
    return 'Goodbye'

if (__name__ == '__main__'):
    app.run(debug=True, port=6060, host='0.0.0.0')