#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:09:49 2016

@author: visethsen
"""
import pandas as pd
import csv

cc1 = csv.DictReader('static/cc1.csv')
gs1 = csv.DictReader('static/gs1.csv')
cc2 = csv.DictReader('static/cc2.csv')
gs2 = csv.DictReader('static/gs2.csv')
cc3 = csv.DictReader('static/cc3.csv')
gs3 = csv.DictReader('static/gs3.csv')
cc4 = csv.DictReader('static/cc4.csv')
gs4 = csv.DictReader('static/gs4.csv')
cc5 = csv.DictReader('static/cc5.csv')
gs5 = csv.DictReader('static/gs5.csv')
cc6 = csv.DictReader('static/cc6.csv')
gs6 = csv.DictReader('static/gs6.csv')
cc7 = csv.DictReader('static/cc7.csv')
gs7 = csv.DictReader('static/gs7.csv')

#Creating a list to hold the games with empty variables to store the stats
cavs = [cc1,cc2,cc3,cc4,cc5,cc6,cc7]
cpts = []
crbs = []
cast = []
cstl = []
corbs = []

vs = []
vt = []
count=[]

#Creating a list to hold the games with empty variables to store the stats
wars = [gs2,gs2,gs3,gs4,gs5,gs6,gs7]

warriors = {
    'points' : [],
    'rebounds' : [],
    'assists' : [],
    'steals': [],
    'orebounds': []


          }

wpts = []
wrbs = []
wast = []
wstl = []
worbs = []

bulls_score = []
other_score=[]
with open('static/bulls1996.csv') as filename:
    chart_data = csv.DictReader(filename)
    for row in chart_data:
        bulls_score.append(int(row['Tm']))
        other_score.append(int(row['Opp']))


for game in cavs:
    cast.append(game.iloc[-1,-7])
    cstl.append(game.iloc[-1,-6])
    crbs.append(game.iloc[-1,-8])
    corbs.append(game.iloc[-1,-10])
    cpts.append(game.iloc[-1,-2])
    vs.append(game.tail(1)['PTS'])
    vt.append(game.tail(1)['AST'])

for game in wars:
    warriors['points'].append(int(game.iloc[-1,-8]))
    warriors['rebounds'].append(int(game.iloc[-1,-2]))
    warriors['assists'].append(int(game.iloc[-1,-7]))
    warriors['orebounds'].append(int(game.iloc[-1,-10]))
    warriors['steals'].append(int(game.iloc[-1,-6]))
    wast.append(game.iloc[-1,-7])
    wstl.append(int(game.iloc[-1,-6]))
    wrbs.append(game.iloc[-1,-8])
    worbs.append(game.iloc[-1,-10])
    wpts.append(game.iloc[-1,-2])
    


