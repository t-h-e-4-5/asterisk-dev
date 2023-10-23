from app import app
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
