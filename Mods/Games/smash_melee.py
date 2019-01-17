"""
author: BrendanMoore42
date: Jan 12, 2019

Gamecube Controller Mod

Super Smash Bros. Melee Controller Add-On
"""
# to import controller and key classes
import time
# from ..DirectKeys.directkeys import *
# from ..Controllers.gamecube import GC_Controller

# Super Smash Bros Melee
class AddOn(GC_Controller):

    def __init__(self):
        self.buttons = {'a': ['jab', 'punch', 'slap', 'strike'],
                   'b': ['b', 'special', ],
                   'x': ['x', 'jump', 'colour'],
                   'y': self.buttons['x'],
                   'L': ['L', 'shield', ],
                   'R': self.buttons['L'],
                   'z': ['Z', 'light shield', 'grab'],
                   'up': ['up'],
                   'down': ['down', 'crouch'],
                   'left': ['left', 'walk', 'run'],
                   'right': ['right', 'walk', 'run'],
                   'd_up': ['d-pad up', 'taunt'],
                   'd_down': ['d-pad down'],
                   'd_left': ['d-pad left'],
                   'd_right': ['d-pad right'],
                   'c_up': ['see up', 'up smash'],
                   'c_down': ['see down', 'down smash', ],
                   'c_left': ['see left', 'left smash'],
                   'c_right': ['see right', 'right smash']}

        add_moves = {self.jab: self.buttons['a'], self.crouch: ['down'],
                           'shield': self.shield, 'grab': self.grab,
                           'wait': self.wait}


    #Each function is a macro for a specific move
    def wait(self, wait):
        time.sleep(wait)


    def jump(self):
        PressKey(T)
        time.sleep(0.1)
        ReleaseKey(T)


    def up(self):
        PressKey(UP)
        time.sleep(0.25)
        ReleaseKey(UP)


    def left(self):
        PressKey(LEFT)
        time.sleep(0.1)#To alter timing of presses
        ReleaseKey(LEFT)


    def right(self):
        PressKey(RIGHT)
        time.sleep(0.1)
        ReleaseKey(RIGHT)


    def crouch(self):
        PressKey(DOWN)
        time.sleep(0.1)
        ReleaseKey(DOWN)


    def jab(self):
        PressKey(A)
        time.sleep(0.05)
        ReleaseKey(A)


    def djab(self):
        PressKey(A)
        ReleaseKey(A)
        time.sleep(0.05)
        PressKey(A)
        ReleaseKey(A)


    def shield(self):
        PressKey(R)
        time.sleep(2)
        ReleaseKey(R)


    def grab(self):
        PressKey(Z)
        time.sleep(0.05)
        ReleaseKey(Z)


    def Rsmash(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def Lsmash(self):
        PressKey(LEFT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(LEFT)
        ReleaseKey(A)

    def laser(self):
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(B)

    def shdl(self):
        PressKey(Y)
        PressKey(B)
        ReleaseKey(B)
        PressKey(B)
        ReleaseKey(B)


    def shine(self):
        PressKey(DOWN)
        PressKey(B)
        time.sleep(0.05)
        ReleaseKey(DOWN)
        ReleaseKey(B)


    def wd_left(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(LEFT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(LEFT)


    def wd_right(self):
        PressKey(X)
        time.sleep(0.05)
        PressKey(DOWN), PressKey(RIGHT)
        PressKey(R)
        ReleaseKey(R), ReleaseKey(DOWN), ReleaseKey(RIGHT)



# moves = "hey up smash then hold shield for 4 seconds"
# move = "smash"
# direction = "up" # if not defined will default to last direction called
# modifier = "hold"
# mod_move = "sheild"
# mod_time = 4
#
# player = AddOn(move=move, direction=direction, modifier=modifier, mod_move=mod_move, mod_time=mod_time) # for debugs