import csv
import os
from flask import Flask, render_template, url_for, request, flash, redirect
from flask.ext.uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import Form
from wtforms import FileField
from werkzeug.utils import secure_filename
from finals2016 import *
from Read_Game import Read_Game

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST']= 'static/img'
configure_uploads(app,photos)

file_dir = ''

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=g.user.id)
        rec.store()
        flash("Photo saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('upload.html')

@app.route('/photo/<id>')
def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)


@app.route("/")
def index():
    title = 'NBA Analytics with Python'
    header = 'Welcome To NBA Analytics with Python'
    body = 'Thinkers of The Game'


    return render_template('index.html', header=header, title=title, body=body)

@app.route("/bulls")
def bulls():

    b = Read_Game('/var/www/FlaskApp/FlaskApp/static/bulls1996.csv')
    title = 'The Champion 1996 Chicago Bulls'
    body = 'The first of second 3peat'
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

    #Will be removing extra lines of code soon, left only to display previous way of doing compared to newer, evolved ways below

    return render_template('charts.html',
    title=title,
    body=body,
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

    g = Read_Game('/var/www/FlaskApp/FlaskApp/static/grizzlies1996.csv')
    title = 'Looking at the Worse 1996 NBA Team'
    body = 'Mean But True'

    return render_template('gcharts.html',
    title=title,
    body=body,
    edgea=len(g.astrebw), edgeb=len(g.astreb),
    steala=len(g.steal_won), stealb=len(g.steal_loss),
    turnovera = len(g.turnover_w), turnoverb = len(g.turnover_l),
    blocksa = len(g.blocks_won),blocksb = len(g.blocks_loss),
    oreboundsa=len(g.orebounds_won),oreboundsb=len(g.orebounds_loss),
    reboundsa=len(g.trebounds_won),reboundsb=len(g.trebounds_loss),
    assista = len(g.assist_won), assistb=len(g.assist_loss)
    )

@app.route("/warriors")
def warriors():

    w = Read_Game('/var/www/FlaskApp/FlaskApp/static/warriors2016.csv')
    title = 'Looking at the Best 2016 NBA Team'
    body = 'Record Breaking'

    return render_template('wcharts.html',
    title=title,
    body=body,
    edgea=len(w.astrebw), edgeb=len(w.astreb),
    steala=len(w.steal_won), stealb=len(w.steal_loss),
    turnovera = len(w.turnover_w), turnoverb = len(w.turnover_l),
    blocksa = len(w.blocks_won),blocksb = len(w.blocks_loss),
    oreboundsa=len(w.orebounds_won),oreboundsb=len(w.orebounds_loss),
    reboundsa=len(w.trebounds_won),reboundsb=len(w.trebounds_loss),
    assista = len(w.assist_won), assistb=len(w.assist_loss)
    )

@app.route("/phil")
def phil():

    p = Read_Game('/var/www/FlaskApp/FlaskApp/static/76ers.csv')
    title = 'Looking at the Worse 2016 NBA Team'
    body = 'Tear Dropping 10 - 72 :( '

    return render_template('pcharts.html',
    title=title,
    body=body,
    edgea=len(p.astrebw), edgeb=len(p.astreb),
    steala=len(p.steal_won), stealb=len(p.steal_loss),
    turnovera = len(p.turnover_w), turnoverb = len(p.turnover_l),
    blocksa = len(p.blocks_won),blocksb = len(p.blocks_loss),
    oreboundsa=len(p.orebounds_won),oreboundsb=len(p.orebounds_loss),
    reboundsa=len(p.trebounds_won),reboundsb=len(p.trebounds_loss),
    assista = len(p.assist_won), assistb=len(p.assist_loss)
    )

#Barkley is our test

@app.route("/barkley")
def barkley():
    title = 'Charles Barkley'
    body = 'Round Mound '

    return render_template('player.html',

    )

if __name__ == "__main__":
    app.debug=True
    app.run()
