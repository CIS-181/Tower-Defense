# Tower_Defense_Game.py
# By Cory Brubaker, Nate Harnish, Kyle Markel, Tj Quntilian

from graphics import *
import time
import cory

win = GraphWin("TD_Game", 1280, 736)

def drawTowerSlots():
        box1 = Rectangle(Point(14.5, 20.5), Point(15.5, 21.5))
        box1.setFill("Black")
        box1.draw(win)

        box2 = box1.clone()
        box2.move(3, 0)
        box2.draw(win)

        box3 = box2.clone()
        box3.move(3, 0)
        box3.draw(win)

        box4 = box3.clone()
        box4.move(3, 0)
        box4.draw(win)

def drawWin():
    # Creates a graphics window and draws the map
    win.setCoords(-.5, -.5, 39.5, 22.5)
    terrain = Image(Point(19.5, 11), "map.png")
    terrain.draw(win)

    moneyText = Text(Point(2, 21.5), "Money: ")
    moneyText.setTextColor("white")
    moneyText.draw(win)

    moneyTextVal = Text(Point(4.5, 21.5), 0)
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
    money = 0
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
