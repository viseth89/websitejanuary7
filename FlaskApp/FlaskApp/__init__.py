import csv
import os
from flask import Flask, render_template, url_for, request
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import Form
from wtforms import FileField
from werkzeug.utils import secure_filename
import bullstats as b
import grizzlies1996 as g
from finals2016 import *

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST']= 'static/img'
configure_uploads(app,photos)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return filename
    return render_template('upload.html')


@app.route("/")
def index():
    title = 'this is the title'
    body = 'this is the body text'
    home_score = []
    away_score = []

    return render_template('index.html', title=title, body=body, home_score=home_score, away_score=away_score)
"""
    with open('bulls1996.csv') as filename:
        chart_data = csv.DictReader(filename)
        for row in chart_data:
            home_score.append(int(row['Tm']))
            away_score.append(int(row['Opp']))

"""



@app.route("/bulls")
def bulls():
    title = 'The Champion 1996 Chicago Bulls'
    body = 'The first of second 3peat'
    home_score = []
    away_score = []
    reboundsa = len(b.trebounds_won)
    reboundsb = len(b.trebounds_loss)
    oreboundsa = len(b.orebounds_won)
    oreboundsb = len(b.orebounds_loss)
    assista = len(b.assist_won)
    assistb = len(b.assist_loss)
    edgea = len(b.astrebw)
    edgeb = len(b.astreb)
    turnovera = len(b.turnover_w)
    turnoverb = len(b.turnover_l)
    steala = len(b.steal_won)
    stealb = len(b.steal_loss)
    blocksa = len(b.blocks_won)
    blocksb = len(b.blocks_loss)

    return render_template('charts.html',
    title=title,
    body=body,
    home_score=home_score,
    away_score=away_score,
    edgea=edgea, edgeb=edgeb,
    steala=steala, stealb=stealb,
    turnovera=turnovera, turnoverb=turnoverb,
    blocksa=blocksa,blocksb=blocksb,
    oreboundsa=oreboundsa,oreboundsb=oreboundsb,
    reboundsa=reboundsa,reboundsb=reboundsb,
    assista = assista, assistb=assistb
    )


@app.route("/finals2016")
def finals2016():
    title = 'Looking at the 2016 Championship Round'
    body = 'this is the body text'

    return render_template('charts.html',
    title=title,
    body=body,
    home_score=b.bulls_score,
    away_score=b.other_score,
    edgea=len(b.astrebw), edgeb=len(b.astreb),
    steala=len(b.steal_won), stealb=len(b.steal_loss),
    turnovera = len(b.turnover_w), turnoverb = len(b.turnover_l),
    blocksa = len(b.blocks_won),blocksb = len(b.blocks_loss),
    oreboundsa=len(b.orebounds_won),oreboundsb=len(b.orebounds_loss),
    reboundsa=len(b.trebounds_won),reboundsb=len(b.trebounds_loss),
    assista = len(b.assist_won), assistb=len(b.assist_loss)
    )

@app.route("/grizzlies")
def grizzlies():
    title = 'Looking at the Worse 1996 NBA Team'
    body = 'Mean But True'

    return render_template('charts.html',
    title=title,
    body=body,
    home_score=g.bulls_score,
    away_score=g.other_score,
    edgea=len(g.astrebw), edgeb=len(g.astreb),
    steala=len(g.steal_won), stealb=len(g.steal_loss),
    turnovera = len(g.turnover_w), turnoverb = len(g.turnover_l),
    blocksa = len(g.blocks_won),blocksb = len(g.blocks_loss),
    oreboundsa=len(g.orebounds_won),oreboundsb=len(g.orebounds_loss),
    reboundsa=len(g.trebounds_won),reboundsb=len(g.trebounds_loss),
    assista = len(g.assist_won), assistb=len(g.assist_loss)
    )

if __name__ == "__main__":
    app.debug=True
    app.run()
