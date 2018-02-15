from directkeys import *
import time


# dash = 1
# hold = dash * time
#

#Each function is a macro for a specific move
def jump():
    PressKey(T)
    time.sleep(0.1)
    ReleaseKey(T)

def up():
    PressKey(UP)
    time.sleep(0.25)
    ReleaseKey(UP)

def left():
    PressKey(LEFT)
    time.sleep(0.1)#To alter timing of presses
    ReleaseKey(LEFT)

def right():
    PressKey(RIGHT)
    time.sleep(0.1)
    ReleaseKey(RIGHT)

def crouch():
    PressKey(DOWN)
    time.sleep(0.1)
    ReleaseKey(DOWN)

def jab():
    PressKey(A)
    time.sleep(0.05)
    ReleaseKey(A)

def djab():
    PressKey(A)
    ReleaseKey(A)
    time.sleep(0.05)
    PressKey(A)
    ReleaseKey(A)

def shield():
    PressKey(R)
    time.sleep(2)
    ReleaseKey(R)

def grab():
    PressKey(Z)
    time.sleep(0.05)
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
    time.sleep(0.05)
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
    time.sleep(0.05)
    ReleaseKey(DOWN)
    ReleaseKey(B)

def wd_left():
    PressKey(X)
    time.sleep(0.05)
    PressKey(DOWN), PressKey(LEFT)
    PressKey(R)
    ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(LEFT)