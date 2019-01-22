"""
author: BrendanMoore42
date: Jan 12, 2019

Standard button moveset

Can be ported to custom consoles and game-specific packs
"""
import re
import time
import itertools as it
from DirectKeys.directkeys import *
# from Mods.Controllers.gamecube import GC_Controller


# Approved mods: add here to add quick links to the controller
mods = {'gc': {'GC_Controller': {'ssbm': 'Super Smash Bros. Melee', }},
        'nes': {'NES': {'smb': 'Super Mario Bros.'}},
        'pc': {'PC': {'rl': 'Rocket League', }},
        }

class Controller():
    def __init__(self, moves,):
        self.moves = moves.lower() # incoming moveset
        self.new_moves = moves.split(' ') # moves split into list
        self._move = None # primary action to be executed
        self._secondary_move = None # secondary action for combinations
        self._direction = 'Centre' # direction modifier, defaults to last called, else stick is centred
        self._modifier = None # special action that changes the execution of primary move
        self._mod_move = None # extra move if required
        self._mod_value = 0 # can represent number operations for seconds or multiple inputs required
        self.execute = True # debug for testing

        # Add to button/analog list to modify/add inputs
        self.buttons = {'button': ['a_press', 'b_press', 'x', 'y', 'l1', 'l2', 'r1' 'r2', 'z']}
        self.analog = {'analog': ['stick', 'dpad', 'cstick']}

        # Add custom macro/move sequence/function keys here to list of trigger phrases
        self.mod_phrases = {'dpad': ['d-pad', 'd pad', ],
                            'cstick': ['c stick', 'c-stick', 'see stick', 'cystic', ],
                            'a_press': ['a button', ],
                            'b_press': ['b button', 'bee button'],
                            'y': ['why button'],
                            'l1': ['l trigger'],
                            'r1': ['r trigger'],
                            'action_split': ['then', 'than', 'and then', 'and than'],
                            'test_trigram': ['ride the bull', ],
                            'test_QUADGRAM': ['enter the konami code']}

        # Add number values here that mess up in translation
        self.num_to_replace = {'1': ['one', 'once',],# 'half', 'quarter'],
                               '2': ['two', 'twice', 'double', ], '3': ['three', 'thrice'],
                               '4': 'four', '5': 'five', '6': 'six',
                               '7': 'seven', '8': 'eight', '9': 'nine',
                               '10': 'ten', '11': 'eleven'}

        # Translate incoming moves to respective keys and modifier values
        self._replace_numbers()  # Replace numbers with string to integer value: ie, 'seven' to '7'
        self._replace_phrases()  # Replace mod phrases in self.moves with key phrases

        # Example: hold up for four seconds
        self.modifiers = {'inputs': ['wait', 'hold', 'press', 'hit', ],
                          'multiplier': ['times', 'once', 'twice', 'thrice', 'half', 'quarter'], # if half, make 1 and then half as a boolean in function call when hold is called
                          'pointer': ['side', 'smash', 'tilt', 'flick'],
                          'direction': ['up', 'down', 'left', 'right', 'centre', 'center'],
                          'other': ['tap', 'mash', 'half', 'degrees',
                                    'seconds', 'wiggle', 'combine'],
                          'action': ['run', 'go', 'walk'],
                          'buttons': self.buttons['button'],
                          'analog': self.analog['analog'],}

        # add custom functions here with a list of terms
        self.available_moves = {self.button_press: self.buttons['button'],
                                self.analog_input: self.analog['analog'],
                                'modifiers': list(it.chain.from_iterable(self.modifiers.values()))}

        # Link button presses to KEY inputs
        self._direct_buttons = {'a_press': A,'b_press': B, 'x': X,'y': Y, 'l1': L1, 'l2': L2, 'r1': R1 , 'r2': R2,
                                'start': START,}
        self._direct_analog = {'up': UP}

        # Execute moves
        if self.execute:
            # Split moves on the actionable split phrases
            for move in self.moves.split('action_split'):
                self._execute_moves(move.lstrip())



        # # debug for stopping during tests
        # if self.execute:
        #     # look for modifiers first
        #     for move in self.new_moves:
        #
        #
        #         try:
        #             if move in list(it.chain.from_iterable(self.modifiers.values())):
        #                 print(move + '!')
        #                 self._set_modifiers(move=move)

                    # for action, button in self.available_moves.items():
                    #     # move will execute the function, or branch further if modifier present
                    #     if move in button:
                    #         action()
                    #         self._set_modifiers(move=move)
                            # if self._modifier:
                            #     self._execute_moves(move=self.moves, direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time)
                # iterate through each move and look for match in controller/modifier dictionaries
                # except:
                #     print('not a modifier')
            #execute move
            #awesome one liner that won't work --> speech modifiers in the way
            # [i(direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time) for i, x in self.available_moves.items() for move in self.new_moves if move in x]
        else:
            print('First pass next')

    # turn all str int to int
    def _replace_numbers(self):
        """Large numbers will typically be ready to convert to int, but numbers 0-10 sometimes
        translate as strings. Any alphanumeric values are converted to int strings."""
        # Find and replace numbers
        for i, x in self.num_to_replace.items():
            for move in self.new_moves:
                loc = self.new_moves.index(move)
                if move in x:
                    self.new_moves[loc] = i

        # Join new moves into moves list. Moves lists is still checked for modifiers as a whole string.
        self.moves = ' '.join(move for move in self.new_moves)


    def _replace_phrases(self):
        """
        Takes the moves list and replaces phrases with key pair for move execution. Works on any length.
        """

        for key, value in self.mod_phrases.items():
            pattern = re.compile("(%s)" % "|".join(map(re.escape, value)))
            self.moves = re.sub(pattern, key, self.moves)
        self.new_moves = self.moves.split(' ')
        print(self.new_moves)


    def _set_direction(self, direction):
        self._direction = direction


    def _clear_modifiers(self):
        """Reset modifiers if none present"""
        self._direction = 'Centre'
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0


    def _set_modifiers(self, moves, verbose=False):
        """
        Assign values for modified moves and directions.
        If no mods returns None for variables
        :param move: Modifier move to set modifier terms
        :param incoming: Move list coming in from main function
        :return:
        """

        def convert_to_int(action):
            """Converts string values to integers and adds it to the self.mod_value"""
            try:
                if int(action):
                    self._mod_value = int(action)
            except:
                pass

        for mod, mods in self.available_moves.items():
            # clear mod_value for each pass
            self._clear_modifiers()
            for action in moves.split(' '):
                convert_to_int(action)
                if action in mods:
                    try:
                        print(action)
                        if action in self.modifiers['buttons']:
                            self._move = action
                        if action in self.modifiers['analog']:
                            self._move = action
                        if action in self.modifiers['multiplier']:
                            self._mod_move = action
                        if action in self.modifiers['inputs']:
                            self._mod_move = action
                        if action in self.modifiers['pointer']:
                            pass
                        if action in self.modifiers['direction']:
                            self._direction = action
                        if action in self.modifiers['other']:
                            if action == 'seconds':
                                self._modifier = action
                        if action in self.modifiers['action']:
                            pass
                    except:
                        self._clear_modifiers()



        if verbose:
            print(f'\nMove: {self._move}',
                  f'Direction: {self._direction}',
                  f'Modifier: {self._modifier}',
                  f'Mod Move: {self._mod_move}',
                  f'Mod Value: {self._mod_value}',
                  )


    def _execute_moves(self, moves):
        """Set modifiers and moves and times"""
        print('Phrase: ' + moves + '\n')

        # Set move modifiers
        self._set_modifiers(moves, verbose=True)

        # Execute moves, that type error? we can ignore that
        try:
            [i() for i, x in self.available_moves.items() if self._move in x]
        except:
            pass



    def button_press(self):
        """Takes cleaned input phrase and performs button presses"""

        self._move = self._direct_buttons[self._move]

        def press_key(moves, ):

            #Press Direction
            PressKey(self._direction)
            PressKey(self._move)

            # Apply modifier value or default to regular
            time.sleep(self._mod_value)
            #Release Keys
            ReleaseKey(self._direction)
            ReleaseKey(self._move)

        if not self._mod_value:
            self._mod_value = 0.25 # standard button press

        if self._mod_move == 'wait':
            press_key()


    def analog_input(self):
        print('Analog JAM :0')
        pass


    def a_press(self, ):

        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)


    def b_press(self, ):

        PressKey(A)
        time.sleep(0.1)
        ReleaseKey(A)


    def r_press(self):
        PressKey(R)
        time.sleep(2)
        ReleaseKey(R)


    def l_press(self):
        PressKey(L)
        time.sleep(2)
        ReleaseKey(L)


    def z_press(self):
        PressKey(Z)
        time.sleep(0.05)
        ReleaseKey(Z)


    def up(self):
        PressKey(UP)
        time.sleep(0.25)
        ReleaseKey(UP)


    def left(self):
        PressKey(LEFT)
        time.sleep(0.1)#To alter timing of presses self.modifier
        ReleaseKey(LEFT)


    def right(self):
        PressKey(RIGHT)
        time.sleep(0.1)
        ReleaseKey(RIGHT)


    def down(self):
        PressKey(DOWN)
        time.sleep(0.1)
        ReleaseKey(DOWN)


    def up_pad_press(self):
        PressKey(A)
        time.sleep(0.05)
        ReleaseKey(A)


    def down_pad_press(self):
        PressKey(A)
        ReleaseKey(A)
        time.sleep(0.05)
        PressKey(A)
        ReleaseKey(A)


    def c_up_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_down_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_left_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


    def c_right_press(self):
        PressKey(RIGHT)
        PressKey(A)
        time.sleep(0.25)
        ReleaseKey(RIGHT)
        ReleaseKey(A)


moves = "press stick left for ten seconds then d-pad up twice then hold b button for six seconds and then then stick right 45 degrees then like flick c stick down then ride the bull then enter the konami code"
moves1 = "run right and press a button three times"
move = "stick"
direction = "left" # if not defined will default to last direction called
modifier = "press"
mod_move = "shield"
mod_time = 10

player = Controller(moves=moves)