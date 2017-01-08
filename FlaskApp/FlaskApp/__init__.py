import csv
import os
from flask import Flask, render_template
from flask_wtf import Form
from wtforms import FileField
app = Flask(__name__)

class UploadForm(Form):
    file = FileField()


@app.route("/")
def index():
    title = 'this is the title'
    body = 'this is the body text'
    home_score = []
    away_score = []

    with open('/var/www/FlaskApp/FlaskApp/static/bulls1996.csv') as filename:
        chart_data = csv.DictReader(filename)
        for row in chart_data:
            home_score.append(int(row['Tm']))
            away_score.append(int(row['Opp']))


    return render_template('index.html', title=title, body=body, home_score=home_score, away_score=away_score)






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

    with open('/var/www/FlaskApp/FlaskApp/static/bulls1996.csv') as filename:
        chart_data = csv.DictReader(filename)
        for row in chart_data:
            home_score.append(int(row['Tm']))
            away_score.append(int(row['Opp']))


    return render_template('charts.html', title=title, body=body, home_score=home_score, away_score=away_score)



if __name__ == "__main__":
    app.debug=True
    app.run()
