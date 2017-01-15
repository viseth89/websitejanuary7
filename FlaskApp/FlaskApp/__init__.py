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
    title = 'Welcome to NBA Analytics with Python'
    body = 'Thinkers of the Game'
    return render_template('index.html', header=header, title=title, body=body)

### Oldest way of doing things
@app.route("/bulls")
def bulls():
    b = ReadGame('/var/www/FlaskApp/FlaskApp/static/bulls1996.csv')
    title = 'The Champion 1996 Chicago Bulls'
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
    # Will be removing extra lines of code soon, left only to display previous way of doing compared to newer, evolved ways below

    return render_template('charts.html',
                           title=title,
                           edgea=edgea, edgeb=edgeb,
                           steala=steala, stealb=stealb,
                           turnovera=turnovera, turnoverb=turnoverb,
                           blocksa=blocksa, blocksb=blocksb,
                           oreboundsa=oreboundsa, oreboundsb=oreboundsb,
                           reboundsa=reboundsa, reboundsb=reboundsb,
                           assista=assista, assistb=assistb,
                           wins=len(b.wins),
                           loss=len(b.loss)
                           )

### Older way of doing things (before presentation)

@app.route("/warriors")
def warriors():
    w = ReadGame('/var/www/FlaskApp/FlaskApp/static/warriors2016.csv')
    title = 'Looking at the Best 2016 NBA Team'
    body = 'Record Breaking'

    return render_template('wcharts.html',
                           title=title,
                           edgea=len(w.astrebw), edgeb=len(w.astreb),
                           steala=len(w.steal_won), stealb=len(w.steal_loss),
                           turnovera=len(w.turnover_w), turnoverb=len(w.turnover_l),
                           blocksa=len(w.blocks_won), blocksb=len(w.blocks_loss),
                           oreboundsa=len(w.orebounds_won), oreboundsb=len(w.orebounds_loss),
                           reboundsa=len(w.trebounds_won), reboundsb=len(w.trebounds_loss),
                           assista=len(w.assist_won), assistb=len(w.assist_loss),
                           wins=len(w.wins),
                           loss=len(w.loss)
                           )

### After Presentation created function

'''
def GameInfo(read_game, title):
    gamedict = {
    'title':title,
    'edgea':len(read_game.astrebw),
    'edgeb':len(read_game.astreb),
    'steala':len(read_game.steal_won),
    'stealb':len(read_game.steal_loss),
    'turnovera' : len(read_game.turnover_w),
    'turnoverb' : len(read_game.turnover_l),
    'blocksa' : len(read_game.blocks_won),
    'blocksb' : len(read_game.blocks_loss),
    'oreboundsa':len(read_game.orebounds_won),
    'oreboundsb':len(read_game.orebounds_loss),
    'reboundsa':len(read_game.trebounds_won),
    'reboundsb':len(read_game.trebounds_loss),
    'assista' : len(read_game.assist_won),
    'assistb':len(read_game.assist_loss),
    'wins' : len(read_game.wins),
    'loss' : len(read_game.loss)
}
    return gamedict
'''

### Currently trying to find a way to upload the image here so i can delete the 4 chart templates and just use one
@app.route("/phil")
def phil():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/76ers.csv')
    gg = GameInfo(g, 'Looking at The Worst 2016 NBA Team')

    return render_template('pcharts.html', color1='blue', color2='grey', color3='red',cteam='Grizzlies', **gg)

@app.route("/grizzlies")
def grizzlies():
    g = ReadGame('/var/www/FlaskApp/FlaskApp/static/grizzlies1996.csv')
    gg = GameInfo(g, 'The Worst Team in 1996')

    return render_template('gcharts.html',
    color1='green', color2='grey', color3='brown', cteam='Grizzlies', **gg)


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
# creating a dictionary to replace some lines thanks ANish


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
