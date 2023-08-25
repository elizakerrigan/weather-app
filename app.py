from flask import Flask, render_template 
import requests
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route ('/about')
def about():
    return 'This is the About Page'

@app.route ('/dashboard')
def dashboard():
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=f35d9a3424a448acb3874227232208&q=Brisbane&aqi=no')
    myData = response.json()    
    #print(myData)
    feels_like = myData['current']['feelslike_c']
    direction = myData['current']['wind_dir']

    match direction: 
        case "N":
            direction = "North"
        case "NE":
            direction = "North East"
        case "NNE":
            direction = "North North East"
        case "E": 
            direction = "East"
        case "SE":
            direction = "South East"
        case "SSE": 
            direction = "South South East"
        case "S": 
            direction = "South"
        case "SW":
            direction = "South West"
        case "SSW":
            direction = "South South West"
        case "W":
            direction = "West"
        case "NW":
            direction = "North West"
        case "NNW":
            direction = "North North West"
        case _:
            direction = direction
    return render_template('dashboard.html', data=myData, feels_like=feels_like, direction=direction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
