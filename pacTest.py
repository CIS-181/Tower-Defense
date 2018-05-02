#pacTest.py
#Nathen Feldgus

#We're making Pacman or Tron or something idk
#Prototype of Mr. Dash

from graphics import *
import random
import time

fps = 60
moveSpeed = 10

colDist = 40

def drawWin():
    bg = Image(Point(0,0), "lv1.png")
    xVal = bg.getWidth()
    yVal = bg.getHeight()
    win = GraphWin("ViDeoGAmeS", xVal, yVal)
    bg.draw(win)
    bg.move(xVal/2, yVal/2)
    return win

def dist(a, b):
    l = a.getX() - b.getX()
    h = a.getY() - b.getY()
    return ((l**2)+(h**2))**(1/2)

def col(playerPos, objs):
    trig = False
    for obj in objs:
        n = dist(playerPos, obj.getAnchor())
        if (n <= colDist):
            trig = True
    return trig

def makeThing(win, playerPos, tag):
    #everything is ~100x100, don't want anything offscreen
    thingWidth = colDist
    halfW = thingWidth/2
    #generate random position away from the player
    ranX = playerPos.getX()
    ranY = playerPos.getY()
    xVal = win.getWidth()
    yVal = win.getHeight()
    while (((ranX-playerPos.getX())**2+(ranY-playerPos.getY())**2)**(1/2) < 225): 
        ranX = random.randint(0+halfW,xVal-halfW)
        ranY = random.randint(0+halfW,yVal-halfW)
    #image libs, default to warning sign
    image = "warn.png"
    if (tag == 'mine'):
        image = 'mine.png'
    if (tag == 'fruit'):
        image = "fruit.png"
    if (tag == 'homing'):
        image = "homing.png"
    
    thing = Image(Point(ranX,ranY), image)
    thing.draw(win)
    return thing

def makeThingNoCollide(win, playerPos, mines, tag):
    thing = makeThing(win, playerPos,tag)
    #prevent it from touching a mine
    while (col(thing.getAnchor(), mines) == True):
        thing.undraw()
        thing = makeThing(win, playerPos,tag)
    return thing

def clampMove(x, y, maxX, maxY):
    if (x <= -colDist):
        x = x+maxX+2*colDist
    if (x >= maxX+colDist):
        x = x-(maxX+2*colDist)
    if (y <= -colDist):
        y = y+maxY+2*colDist
    if (y >= maxY+colDist):
        y = y-(maxY+2*colDist)
    return Point(x,y)

def homingMines(playerPos, homingMines):

    moveSpeed = 3.5
    pX = playerPos.getX()
    pY = playerPos.getY()
    for mine in homingMines:
        m = mine.getAnchor()
        mX = m.getX()
        mY = m.getY()
        dX = pX - mX
        dY = pY - mY
        mine.move(moveSpeed * (dX/(abs(dX)+abs(dY))), moveSpeed * (dY/(abs(dX)+abs(dY))))

def gameend(win, score, moveSpeed):
    win.close()
    print("Score: "+str(score))
    print("Speed: "+str(moveSpeed))
    input("Game Over")
        
        
def main():
    #setup stuff
    win = drawWin()
    xVal = win.getWidth()
    yVal = win.getHeight()

    dirs = [["u1.png","u2.png"],["d1.png","d2.png"],["l1.png","l2.png"],["r1.png","r2.png"]]
    pics = ["u1.png","u2.png"]
    curDir = "Up"
    
    #spawn the player
                     
    playerPos = win.getMouse()
    player = Image(playerPos, pics[0])
    i = 0
    
    #makes list of mines
    mines = []
    homing = []

    #makes a set number of mines
    for i in range(4):
        mines.append(makeThingNoCollide(win, playerPos,mines,'mine'))

    #do the same thing for fruit, only making one
    fruits = []
    fruits.append(makeThingNoCollide(win,playerPos,mines,'fruit'))




    score = 0
    #main loop
    while True:
        #set current direction
        key = win.checkKey()
        if (key == "Up"):
            pics = dirs[0]
            curDir = key
        if (key == "Down"):
            pics = dirs[1]
            curDir = key
        if (key == "Left"):
            pics = dirs[2]
            curDir = key
        if (key == "Right"):
            pics = dirs[3]
            curDir = key
        #movement
        moveSpeed = (i/400)+4
        if (curDir == "Up"):
            playerPos = Point(playerPos.getX(), playerPos.getY() - moveSpeed)
        if (curDir == "Down"):
            playerPos = Point(playerPos.getX(), playerPos.getY() + moveSpeed)
        if (curDir == "Left"):
            playerPos = Point(playerPos.getX()-moveSpeed, playerPos.getY())
        if (curDir == "Right"):
            playerPos = Point(playerPos.getX()+moveSpeed, playerPos.getY())

        #clampmovement
        playerPos = clampMove(playerPos.getX(), playerPos.getY(), xVal, yVal)

        #animation
        i = i+1
        
        player.undraw()
        player = Image(playerPos, pics[((i//8)%2)])
        #redraw the player
        player.draw(win)


        #check if player collides with a mine
        collide = col(playerPos, mines)
        if (collide == True):
            gameend(win, score, moveSpeed)

        #check if player collected fruit
        collide = col(playerPos, fruits)
        if (collide == True):
            score = score + 1
            for f in fruits:
                f.undraw()
            fruits = []
            fruits.append(makeThingNoCollide(win,playerPos,mines,'fruit'))

        

        #make a new mine every few frames, making sure to keep it away from the player
        if (i%300 == 1):
            mines.append(makeThingNoCollide(win, playerPos, mines, 'mine'))
        #make a homing mine every once in a while
        if (i%800 == 1):
            hMine = makeThingNoCollide(win, playerPos,mines, 'homing')
            homing.append(hMine)
            mines.append(hMine)
        homingMines(playerPos, homing)


        
        #wait a bit
        time.sleep(1/fps)
 
    win.close()
    
        
main()
