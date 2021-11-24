import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
  url = 'api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b3cb766639dc5ea608f6017ede1df5f6'
  city = 'Las Vegas'
  
  r = requests.get(url.format(city)).json()
  print(r)
  
  weather = {
    'city': city,
    'temperature': r['main']['temp'],
    'description': r['weather'][0]['description'],
    'icon': r['weather'][0]['icon'],
  }
  
  return render_template('weather.html' weather=weather)
