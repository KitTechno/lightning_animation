import turtle

class init():
    # sets up variables for window size
    screenwidth = 2560
    screenheigth = 1440
    windowwidth = screenwidth/2
    windowheight = screenheigth/2

    # initialises the window 
    night = turtle.Screen()
    night.setup(windowwidth, windowheight, None, None)
    night.colormode(255)
    night.bgcolor(10,10,30)
    night.listen()

    # initalises the flash
    flash = turtle.Turtle()
    flash.hideturtle()
    flash.color(230,230,255)
    flash.width(5)
    flash.speed(10)
    flash.penup()

    xzero = 0
    yzero = (windowheight/2)
    