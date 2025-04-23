# import random_functions as ranfun
import random
import init
# from playsound import playsound

screenheight = init.init.screenheigth
screenwidth = init.init.screenwidth
# flashbreak = screenheight
# flashlengthmin = screenheight // 20
# flashlengthmax = screenheight // 5

def flashscreen(night):
        # time.sleep(0.05)
        night.clear()
        # time.sleep(0.05)
        night.colormode(255)
        # night.bgcolor(10,10,30)

def drawstrike(night,flash,xzero,yzero):
        # playsound("lightning sound effect.wav")
        flash.penup()
        ranxzero = random.randint(-screenwidth//5,screenwidth//5)
        returnhome(flash,ranxzero,yzero)
        for i in range(20):
                night.bgcolor(255-(11*i)-20,255-(11*i)-20,255-(11*i))
                flash.setheading(random.randint(270-60,270+60))
                flashlenght = random.randint(10, 100)
                flash.pendown()
                flash.forward(flashlenght)

def returnhome(flash,xzero,yzero):
        flash.penup()
        flash.goto(xzero,yzero)

