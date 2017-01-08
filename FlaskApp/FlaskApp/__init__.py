import csv
import os
from flask import Flask, render_template, url_for
from flask_wtf import Form
from wtforms import FileField
from bullstats import *

app = Flask(__name__)

class UploadForm(Form):
    file = FileField()


@app.route("/")
def index():
    title = 'this is the title'
    body = 'this is the body text'
    home_score = []
    away_score = []
    rebow = len(trebounds_won)


    with open('bulls1996.csv') as filename:
        chart_data = csv.DictReader(filename)
        for row in chart_data:
            home_score.append(int(row['Tm']))
            away_score.append(int(row['Opp']))



    return render_template('index.html', title=title, body=body, home_score=rebow, away_score=away_score)






@app.route('/upload', methods=['GET','POST'])
def upload(request):
    form = UploadForm(request.POST)
    if form.file.data:
        file_data = request.FILES[form.file.name].read()
        print(file_data)

    return render_template('upload.html', form=form)







@app.route("/bulls")
def bulls():
    title = 'this is the title'
    body = 'this is the body text'
    home_score = []
    away_score = []
    reboundsa = len(trebounds_won)
    reboundsb = len(trebounds_loss)
    oreboundsa = len(orebounds_won)
    oreboundsb = len(orebounds_loss)
    assista = len(assist_won)
    assistb = len(assist_loss)
    edgea = len(astrebw)
    edgeb = len(astreb)
    turnovera = len(turnover_w)
    turnoverb = len(turnover_l)
    steala = len(steal_won)
    stealb = len(steal_loss)
    blocksa = len(blocks_won)
    blocksb = len(blocks_loss)

    print (len(astreb))
    print (home_score)

    with open('bulls1996.csv') as filename:
        chart_data = csv.DictReader(filename)
        for row in chart_data:
            home_score.append(int(row['Tm']))
            away_score.append(int(row['Opp']))


    return render_template('charts.html', title=title, body=body, home_score=home_score, away_score=away_score, edgea=edgea, edgeb=edgeb, steala=steala, stealb=stealb, turnovera=turnovera, turnoverb=turnoverb, blocksa=blocksa,blocksb=blocksb, oreboundsa=oreboundsa,oreboundsb=oreboundsb,
    reboundsa=reboundsa,reboundsb=reboundsb,
    assista = assista, assistb=assistb)



if __name__ == "__main__":
    app.debug=True
    app.run()
