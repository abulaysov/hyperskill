from flask import Flask, render_template, request, get_flashed_messages, redirect, flash
import sys
import requests
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SECRET_KEY'] = os.urandom(24)


class Weather(db.Model):
    __tablename__ = 'City'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)


@app.route('/', methods=['POST', 'GET'])
def index():
    appid = 'c9430ab9659192f1970c4334ff927cc6'
    if request.method == 'GET':
        if bool(Weather.query.all()):
            li = []
            for i in Weather.query.all():
                r = requests.get("http://api.openweathermap.org/data/2.5/find",
                                 params={'q': i.name, 'type': 'like', 'units': 'metric', 'APPID': appid})
                data = r.json()
                li.append({'description': data['list'][0]['weather'][0]['main'],
                           'name': data['list'][0]['name'],
                           'temp': data['list'][0]['main']['temp'],
                           'id': i.id})

            return render_template('index.html', li=li)

        return render_template('index.html')
    if request.method == 'POST':
        city_name = request.form.get('city_name')

        r = requests.get("http://api.openweathermap.org/data/2.5/find",
                     params={'q': city_name, 'type': 'like', 'units': 'metric', 'APPID': appid})

        data = r.json()
        if not len(data['list']):
            flash("The city doesn't exist!")
            return redirect('/')

        if any(data['list']) and any(Weather.query.filter(Weather.name == data['list'][0]['name']).all()):
            flash("The city has already been added to the list!")
            return redirect('/')

        name = data['list'][0]['name']
        db.session.add(Weather(name=name))
        db.session.commit()
        li = []
        for i in Weather.query.all():
            r = requests.get("http://api.openweathermap.org/data/2.5/find",
                             params={'q': i.name, 'type': 'like', 'units': 'metric', 'APPID': appid})
            data = r.json()
            li.append({'description': data['list'][0]['weather'][0]['main'],
                       'name': data['list'][0]['name'],
                       'temp': data['list'][0]['main']['temp']})
        return render_template('index.html', li=li)


@app.route('/delete/<int:city_id>', methods=['POST'])
def main(city_id):
    city_name = Weather.query.filter(Weather.id == city_id).one()
    db.session.delete(city_name)
    db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
