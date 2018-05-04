# cory.py
# Cory Brubaker

from graphics import *

def incScore(oneSec, money, moneyTextVal, score, scoreTextVal, win):
    
    if oneSec == True:
        money = money + 1
        score = score + 10

    if win.checkKey() == "dollar":
        money = money + 500

    moneyTextVal.setText(money)
    scoreTextVal.setText(score)

    return money, score

def placeTower(money, win):

    tower1 = Image(Point(15, 21), "tower_basic.png")
    tower2 = Image(Point(18, 21), "tower_sniper.png")
    tower3 = Image(Point(21, 21), "tower_spread.png")
    tower4 = Image(Point(24, 21), "tower_gatling.png")
    tower1n = Image(Point(15, 21), "tower_basic_n.png")
    tower2n = Image(Point(18, 21), "tower_sniper_n.png")
    tower3n = Image(Point(21, 21), "tower_spread_n.png")
    tower4n = Image(Point(24, 21), "tower_gatling_n.png")

    t1Select = Rectangle(Point(14.25, 20.25), Point(15.75, 21.75))
    t1Select.setFill("green")
    t1Select.undraw()
    #t2Select
    #t3Select

    m = win.checkMouse()
    mx = my = 99
    
    if m != None:
        mx = m.getX()
        my = m.getY()

    if money >= 50:
        tower1.draw(win)
        
        if my >= 19.5 and my <= 21.5 and my != 99 and mx != 99:
            
            if mx >= 14.5 and mx <= 15.5:
                t1Select.draw(win)
    else:
        tower1n.draw(win)

    if money >= 100:
        tower2.draw(win)
    else:
        tower2n.draw(win)

    if money >= 200:
        tower3.draw(win)
    else:
        tower3n.draw(win)

    if money >= 1000:
        tower4.draw(win)
    else:
        tower4n.draw(win)

    # if click is on a specific tower, select it
    # place tower where user clicks

    

    
            

    if m != None:
        money = money - 10

    t1 = False
    t2 = False
    t3 = False
    t4 = False

    return t1, t2, t3, t4, money

