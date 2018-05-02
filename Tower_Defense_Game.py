# Tower_Defense_Game.py
# By Cory Brubaker, Nate Harnish, Kyle Markel, Tj Quntilian

from graphics import

def main():
    # Creates a graphics window and draws the map
    win = GraphWin("TD_Game", 1280, 736)
    win.setBackground("white")
    win.setCoords(0, 0, 1280, 736)
    woodTexture = Image(Point(640, 368), "map.png")
    woodTexture.draw(win)
