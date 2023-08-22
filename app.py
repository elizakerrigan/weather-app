from flask import Flask, render_template 
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route ('/about')
def about():
    return 'This is the About Page'

@app.route ('/dashboard')
def dashboard():
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=-27.4679&longitude=153.0281&daily=temperature_2m_max,temperature_2m_min&timezone=Australia%2FSydney')
    myData = response.json()
    print(myData)
    return render_template('dashboard.html', data=myData)

if __name__ == '__main__':
    app.run(debug=True)
