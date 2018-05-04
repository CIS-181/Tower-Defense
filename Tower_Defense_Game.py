# Tower_Defense_Game.py
# By Cory Brubaker, Nate Harnish, Kyle Markel, Tj Quntilian

from graphics import *
import time
import cory

win = GraphWin("TD_Game", 1280, 736)

def drawTowerSlots():
    # draws the towers with prices
    tower1n = Image(Point(15, 21), "tower_basic_n.png")
    tower1n.draw(win)

    tower2n = Image(Point(18, 21), "tower_sniper_n.png")
    tower2n.draw(win)

    tower3n = Image(Point(21, 21), "tower_spread_n.png")
    tower3n.draw(win)

    tower4n = Image(Point(24, 21), "tower_gatling_n.png")
    tower4n.draw(win)

    tower1Price = Text(Point(16, 21), 50)
    tower1Price.setTextColor("white")
    tower1Price.draw(win)

    tower2Price = Text(Point(19.2, 21), 100)
    tower2Price.setTextColor("white")
    tower2Price.draw(win)

    tower3Price = Text(Point(22.2, 21), 200)
    tower3Price.setTextColor("white")
    tower3Price.draw(win)

    tower4Price = Text(Point(25.35, 21), 1000)
    tower4Price.setTextColor("white")
    tower4Price.draw(win)

def drawWin():
    # creates a graphics window and draws the map
    win.setCoords(-.5, -.5, 39.5, 22.5)
    terrain = Image(Point(19.5, 11), "map.png")
    terrain.draw(win)

    moneyText = Text(Point(2, 21.5), "Money: ")
    moneyText.setTextColor("white")
    moneyText.draw(win)

    moneyTextVal = Text(Point(4.5, 21.5), 50)
    moneyTextVal.setTextColor("white")
    moneyTextVal.draw(win)
    
    scoreText = Text(Point(8, 21.5), "Score: ")
    scoreText.setTextColor("white")
    scoreText.draw(win)

    scoreTextVal = Text(Point(10.5, 21.5), 0)
    scoreTextVal.setTextColor("white")
    scoreTextVal.draw(win)

    towerText = Text(Point(19.5, 22), "Towers")
    towerText.setTextColor("white")
    towerText.draw(win)

    drawTowerSlots()

    return moneyTextVal, scoreTextVal

def main():
    moneyTextVal, scoreTextVal = drawWin()

    stText = Text(Point(10, 17), "Click to Start Game")
    stText.setSize(20)
    stText.setTextColor("White")
    stText.draw(win)
    win.getMouse()
    stText.undraw()

    previousTime = time.time()

    quarterCount = 0
    halfCount = 0
    oneCount = 0
    money = 50
    score = 0
    
    while True: #not gameOver():

        # define variables based on time increments
        currentTime = time.time()
        if currentTime - previousTime >= 0.25:
            quarterSec = True
            previousTime = time.time()
        else:
            stText.undraw()
            quarterSec = False

        if quarterSec == True:
            quarterCount = quarterCount + 1

        if quarterCount == 2:
            quarterCount = 0
            halfSec = True
        else:
            halfSec = False

        if halfSec == True:
            halfCount = halfCount + 1

        if halfCount == 2:
            halfCount = 0
            oneSec = True
        else:
            oneSec = False

        if oneSec == True:
            oneCount = oneCount + 1

        if oneCount == 2:
            oneCount = 0
            twoSec = True
        else:
            twoSec = False

        #tj.enemy()
        
        money, score = cory.incScore(oneSec, money, moneyTextVal, score, scoreTextVal, win)
        t1, t2, t3, t4, money = cory.placeTower(money, win)

        #if t1 == True:
        #    nate.spawnT1()
        #elif t2 == True:
        #    nate.spawnT2()
        #elif t3 == True:
        #    nate.spawnT3()
        #else:
        #    nate.spawnT4()
        
main()
