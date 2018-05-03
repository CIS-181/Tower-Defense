# cory.py
# Cory Brubaker

from graphics import *

def incScore(oneSec, money, moneyTextVal, score, scoreTextVal, win):
    
    if oneSec == True:
        money = money + 1
        score = score + 1

    moneyTextVal.setText(money)
    scoreTextVal.setText(score)

    return money, score

def placeTower(money, win):

    m = win.checkMouse()

    if m != None:
        money = money - 10
    
    # if score is enough draw each tower, else draw black box
    # if click is on a specific tower, select it
    # place tower where user clicks

    t1 = False
    t2 = False
    t3 = False
    t4 = False

    return t1, t2, t3, t4, money

