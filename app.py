import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'

db = SQLAlchemy(app)

class City(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  

@app.route('/')
def index():
  cities = City.query.all()
  
  url = 'api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b3cb766639dc5ea608f6017ede1df5f6'
  
  weather_data = []
  
  for city in cities:
    
    r = requests.get(url.format(city)).json()
    print(r)

    weather = {
      'city': city,
      'temperature': r['main']['temp'],
      'description': r['weather'][0]['description'],
      'icon': r['weather'][0]['icon'],
    }
    
    weather_data.append(weather)
  
  return render_template('weather.html' weather=weather)
