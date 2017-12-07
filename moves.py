from directkeys import *
import time


# dash = 1
# hold = dash * time
#


def jump():
    PressKey(X)
    ReleaseKey(X)

def up():
    PressKey(UP)
    ReleaseKey(UP)

def left():
    PressKey(LEFT)
    time.sleep(0.5)
    ReleaseKey(LEFT)

def right():
    PressKey(RIGHT)
    time.sleep(0.5)
    ReleaseKey(RIGHT)

def crouch():
    PressKey(DOWN)
    time.sleep(0.5)
    ReleaseKey(DOWN)

def jab():
    PressKey(A)
    ReleaseKey(A)

def djab():
    PressKey(A)
    ReleaseKey(A)
    PressKey(A)
    ReleaseKey(A)

def shield():
    PressKey(R)
    time.sleep(2)
    ReleaseKey(R)

def grab():
    PressKey(Z)
    ReleaseKey(Z)

def Rsmash():
    PressKey(RIGHT)
    PressKey(A)
    time.sleep(0.25)
    ReleaseKey(RIGHT)
    ReleaseKey(A)

def Lsmash():
    PressKey(LEFT)
    PressKey(A)
    time.sleep(0.25)
    ReleaseKey(LEFT)
    ReleaseKey(A)

def laser():
    PressKey(B)
    ReleaseKey(B)

def shdl():
    PressKey(Y)
    PressKey(B)
    ReleaseKey(B)
    PressKey(B)
    ReleaseKey(B)

def shine():
    PressKey(DOWN)
    PressKey(B)
    time.sleep(0.5)
    ReleaseKey(DOWN)
    ReleaseKey(B)