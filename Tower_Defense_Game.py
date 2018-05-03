# Tower_Defense_Game.py
# By Cory Brubaker, Nate Harnish, Kyle Markel, Tj Quntilian

from graphics import *
import time
#import cory.py

win = GraphWin("TD_Game", 1280, 736)

def drawWin():
    # Creates a graphics window and draws the map
    win.setCoords(-.5, -.5, 39.5, 22.5)
    terrain = Image(Point(19.5, 11), "map.png")
    terrain.draw(win)

#def drawTowerSlots():
    #add code here to draw black boxes

def main():
    drawWin()

    stText = Text(Point(10, 17), "Click to Start Game")
    stText.setSize(20)
    stText.setTextColor("White")
    stText.draw(win)
    win.getMouse()
    stText.undraw()

    #drawTowerSlots()

    previousTime = time.time()

    quarterCount = 0
    halfCount = 0
    oneCount = 0

    c = Circle(Point(39, 18), .5)
    c.draw(win)
    
    while False: #not gameOver():

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
        
        #money = cory.incScore(time)
        #t1, t2, t3, t4 = cory.placeTower(money)

        #if t1 == True:
        #    nate.spawnT1()
        #elif t2 == True:
        #    nate.spawnT2()
        #elif t3 == True:
        #    nate.spawnT3()
        #else:
        #    nate.spawnT4()
        
main()
