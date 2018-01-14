import csv
import os
import pandas as pd
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from wtforms import FileField
from werkzeug.utils import secure_filename
from ReadGame import ReadGame, GameInfo

app = Flask(__name__)

@app.route("/")
def index():
    header = 'Welcome to NBA Analytics with Python'
    title = 'Welcome to NBA Analytics via Python'
    body = 'Thinkers of the Game'
    return render_template('index.html', header=header, title=title, body=body)

@app.route("/bulls")
def bulls():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/bulls1996.csv')
    gg = GameInfo(g, 'Looking at The Championship 1996 NBA Team')

    return render_template('charts.html', color1='#FF6384', color2='grey', color3='red',cteam='Bulls', **gg)

@app.route("/warriors")
def warriors():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/warriors2016.csv')
    gg = GameInfo(g, 'Looking at The Best 2016 NBA Team')

    return render_template('wcharts.html', color1='orange', color2='grey', color3='purple',cteam='Warriors', **gg)

### Currently trying to find a way to upload the image here so i can delete the 4 chart templates and just use one
@app.route("/phil")
def phil():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/76ers.csv')
    gg = GameInfo(g, 'Looking at The Worst 2016 NBA Team')

    return render_template('pcharts.html', color1='blue', color2='grey', color3='red',cteam='76ers', **gg)

@app.route("/grizzlies")
def grizzlies():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/grizzlies1996.csv')
    gg = GameInfo(g, 'The Worst Team in 1996')
    pic = '/var/www/FlaskApp/FlaskApp/static/grizzlies.jpg'
    return render_template('gcharts.html', color1='green', color2='grey', color3='brown', cteam='Grizzlies', pic = pic, **gg)

@app.route('/guide')
def guide():
    title = 'How to make your own site'
    body = 'I will show you how'

    return render_template('siteguide.html')

@app.route('/google')
def google():
    p = ReadGame('/var/www/FlaskApp/FlaskApp/static/76ers.csv')
    return render_template('google.html', assista=len(p.assist_won), assistb=len(p.assist_loss))


# Upload #1 Priority is to get upload file working
# Barkley is our test for the player
# Finals 2016 will be our test for the 7 game finals
# we are also trying to upload the images from jinja vs individual html pages

"""
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        form.file.data.save('uploads/' + filename)
        return redirect('index.html')

    return render_template('upload.html', form=form)

"""
if __name__ == "__main__":
    app.debug = True
    app.run()
