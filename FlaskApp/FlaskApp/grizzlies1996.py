import pandas as pd
import csv
import json

df = pd.read_csv('/var/www/FlaskApp/FlaskApp/static/grizzlies1996.csv')

wins = df[df['W/L']=='W']
loss = df[df['W/L']=='L']
orebounds_won= df[df['ORB']>df['ORB.1']]
orebounds_loss= df[df['ORB']<df['ORB.1']]
trebounds_won= df[df['TRB']>df['TRB.1']]
trebounds_loss= df[df['TRB']<df['TRB.1']]
assist_won= df[df['AST']>df['AST.1']]
assist_loss= df[df['AST']<df['AST.1']]
turnover_w= df[df['TOV']>df['TOV.1']]
turnover_l= df[df['TOV']<df['TOV.1']]
steal_won= df[df['STL']>df['STL.1']]
steal_loss= df[df['STL']<df['STL.1']]
assist_won= df[df['AST']>df['AST.1']]
assist_loss= df[df['AST']<df['AST.1']]
blocks_won= df[df['BLK']>df['BLK.1']]
blocks_loss= df[df['BLK']<df['BLK.1']]

wrebounds_won=trebounds_won[trebounds_won["W/L"] =="W"]
wassist_won=assist_won[assist_won['W/L']=='W']
astreb = assist_won[assist_won['TRB'] > assist_won['TRB.1']]
astrebw = astreb[astreb['W/L']=='W']

wpct = (len(wrebounds_won)) / (len(trebounds_won))
wwpct = (len(wassist_won)) / (len(assist_won))
wwwpct = len(astrebw)/len(astreb)

bulls_score = []
other_score=[]
with open('/var/www/FlaskApp/FlaskApp/static/grizzlies1996.csv') as filename:
    chart_data = csv.DictReader(filename)
    for row in chart_data:
        bulls_score.append(int(row['Tm']))
        other_score.append(int(row['Opp']))
