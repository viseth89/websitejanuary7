import pandas as pd
import csv

class ReadGame:
    def __init__(self, file):

        df = pd.read_csv(file)

        self.dff = df
        self.wins = df[df['W/L']=='W']
        self.loss = df[df['W/L']=='L']
        self.orebounds_won= df[df['ORB']>df['ORB.1']]
        self.orebounds_loss= df[df['ORB']<df['ORB.1']]
        self.trebounds_won= df[df['TRB']>df['TRB.1']]
        self.trebounds_loss= df[df['TRB']<df['TRB.1']]
        self.assist_won= df[df['AST']>df['AST.1']]
        self.assist_loss= df[df['AST']<df['AST.1']]
        self.turnover_w= df[df['TOV']>df['TOV.1']]
        self.turnover_l= df[df['TOV']<df['TOV.1']]
        self.steal_won= df[df['STL']>df['STL.1']]
        self.steal_loss= df[df['STL']<df['STL.1']]
        self.assist_won= df[df['AST']>df['AST.1']]
        self.assist_loss= df[df['AST']<df['AST.1']]
        self.blocks_won= df[df['BLK']>df['BLK.1']]
        self.blocks_loss= df[df['BLK']<df['BLK.1']]

        self.wrebounds_won=df[(df['TRB']>df['TRB.1']) & (df['W/L']=='W')]
        self.wassist_won=df[(df['AST']>df['AST.1']) & (df['W/L']=='W')]
        self.astreb = df[(df['AST']>df['AST.1']) & (df['TRB']>df['TRB.1'])]
        self.astrebw = df[(df['AST']>df['AST.1']) & (df['TRB']>df['TRB.1']) & (df['W/L']=='W')]

        self.wpct = (len(self.wrebounds_won)) / (len(self.trebounds_won))
        self.wwpct = (len(self.wassist_won)) / (len(self.assist_won))
        self.wwwpct = len(self.astrebw)/len(self.astreb)
