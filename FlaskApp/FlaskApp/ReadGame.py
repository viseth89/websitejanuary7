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
