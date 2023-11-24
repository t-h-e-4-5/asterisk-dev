from app import app
from flask import render_template

@app.route('/dashbord')
def index():
    return render_template('index.html')

