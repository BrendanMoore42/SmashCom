"""
author: BrendanMoore42
date: Jan 12, 2019

Standard button moveset

Can be ported to custom consoles and game-specific packs
"""
import re
import time
import itertools as it
from pampy import match, _
# from DirectKeys.directkeys import *
# from Mods.Controllers.gamecube import GC_Controller


# Approved mods: add here to add quick links to the controller
mods = {'gc': {'GC_Controller': {'ssbm': 'Super Smash Bros. Melee', }},
        'nes': {'NES': {'smb': 'Super Mario Bros.'}},
        'pc': {'PC': {'rl': 'Rocket League', }},
        }

class Controller():
    def __init__(self, moves,):
        self.moves = moves.lower()
        self.new_moves = moves.split(' ')
        self._direction = None
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0
        self._mod_index = 0
        self.execute = True

        # Add to button/analog list to modify/add inputs
        self.buttons = {'button': ['a_press', 'b_press', 'x', 'y', 'l1', 'l2', 'r1' 'r2', 'z']}
        self.analog = {'analog': ['stick', 'dpad', 'cstick']}

        # Add custom macro/move sequence/function keys here to list of trigger phrases
        self.mod_phrases = {'dpad': ['d-pad', 'd pad', ],
                            'cstick': ['c stick', 'c-stick', 'see stick', 'cystic', ],
                            'a_press': ['a button', ],
                            'b_press': ['b button', 'bee button'],
                            'test_trigram': ['ride the bull', ],
                            'test_QUADGRAM': ['enter the konami code']}

        # Example: hold up for four seconds
        self.modifiers = {'inputs': ['wait', 'hold', 'press', 'hit', ],
                          'multiplier': ['times', 'once', 'twice', 'thrice'],
                          'pointer': ['side', 'smash', 'tilt', 'flick'],
                          'direction': ['up', 'down', 'left', 'right'],
                          'other': ['tap', 'mash', 'half', 'degrees', 'seconds', 'wiggle', 'combine'],
                          'action': ['run', 'go', 'walk'],
                          'buttons': self.buttons['button'],
                          'analog': self.analog['analog']}

        # Add number values here that mess up in translation
        self.num_to_replace = {'1': ['one', 'once', 'half', 'quarter', 'split'], # if half, make 1 and then half as a boolean in function call when hold is called
                          '2': ['two', 'twice', 'double', ], '3': ['three', 'thrice'],
                          '4': 'four', '5': 'five', '6': 'six',
                          '7': 'seven', '8': 'eight', '9': 'nine',
                          '10': 'ten', '11': 'eleven'}

        # add custom functions here with a list of terms
        self.available_moves = {self.button_press: self.buttons['button'],
                                self.analog_input: self.analog['analog'],
                                self._set_modifiers: list(it.chain.from_iterable(self.modifiers.values()))}

        # Translate incoming moves to respective keys and modifier values
        self._replace_numbers()  # Replace numbers with string to integer value: ie, 'seven' to '7'
        print('replacing phrases')
        self._replace_phrases()  # Replace ngrams with key phrases


        # debug for stopping during tests
        if self.execute:
            # look for modifiers first
            for move in self.new_moves:
                try:
                    if move in list(it.chain.from_iterable(self.modifiers.values())):
                        print(move + '!')
                        self._set_modifiers(move=move)

                    # for action, button in self.available_moves.items():
                    #     # move will execute the function, or branch further if modifier present
                    #     if move in button:
                    #         action()
                    #         self._set_modifiers(move=move)
                            # if self._modifier:
                            #     self._execute_moves(move=self.moves, direction=self._direction, mod_move=self.mod_move, mod_time=self.mod_time)
                # iterate through each move and look for match in controller/modifier dictionaries
                except:
                    print('not a modifier')
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
        Takes the moves list and replaces phrases with key pair for move execution
        :param moves: list
        """

        for key, mod in self.mod_phrases.values():
            match(self.moves, mod, key, default=False)
        
        # Create a regular expression  from the dictionary keys
        regex = re.compile("(%s)" % "|".join(map(re.escape, self.mod_phrases.keys())))

        # For each match, look-up corresponding value in dictionary
        toast = regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], self.moves)

        print(toast, '!')

        # # Hold temp values to append to moves after logic
        # temp_gram = []
        # gram_out = []
        #
        # def generate_ngrams(moves, n):
        #     """Generates list of ngrams from moves with n value"""
        #     # Break sentence in the token, remove empty tokens
        #     tokens = [token for token in moves.split(" ") if token != ""]
        #
        #     # Concatentate the tokens into ngrams and return
        #     ngrams = zip(*[tokens[i:] for i in range(n)])
        #     return [" ".join(ngram) for ngram in ngrams]
        #
        #
        # # Sweep through moves from max ngram count to 1, updating the moves with every pass, in reverse
        # for i in reversed(range(1, self.max_ngram+1)):
        #     gram = generate_ngrams(self.moves, i)
        #     print(i, gram)
        #     for mod, mod_list in self.mod_phrases.items():
        #         for phrase in gram:
        #             loc = gram.index(phrase)
        #             if gram[loc] in mod_list: ## ADD LIST OF EVERYTHING YOU NEED TO ONE LIST HERE IF ITS IN ABOVE DICTS
        #                 gram[loc] = mod
        #                 temp_gram.append(mod)
        #             else:
        #                 temp_gram.append(gram[loc].split(' ')[0])
        #                 ## maybe iterate through numbers dict because those aren't in mod phrases
        #                 pass
        #
        #     print(temp_gram)
        #     if i >= 3:
        #         # Apply changes and decrease ngram count
        #         self.moves = ' '.join(word.split(' ')[0] for word in gram)
        #     else:
        #         print('PPMD' + self.moves)


    def _set_direction(self, direction):
        self._direction = direction


    def _clear_modifiers(self):
        """Reset modifiers if none present"""
        self._modifier = None
        self._mod_move = None
        self._mod_value = 0


    def _set_modifiers(self, move):
        """
        Assign values for modified moves and directions.
        If no mods returns None for variables
        :param move: Modifier move to set modifier terms
        :param incoming: Move list coming in from main function
        :return:
        """

        # set modifier for parsing
        self._modifier = move

        # get specified number
        def _fetch_values(mod_type):
            """
            Find the number in the phrase and generate a int value. Mod type will search
            for numbers in different spaces.
            """
            num_to_int = {['one', 'once']: 1, ['two', 'twice']: 2, ['three', 'thrice']: 3,
                          'four': 4, 'five': 5, 'six': 6,
                          'seven': 7, 'eight': 8, 'nine': 9,
                          'ten': 10, 'half': 0.5}

            if mod_type == 'inputs':
                try:
                    # returns int value from text
                    word_index = self.moves.index(self._modifier)
                    # get value for modifier to check where number should be
                    mod_value = [i for i, x in self.modifiers.items() if move in x]
                    # search through the incoming moves to find number to convert
                    modifier_index = self.moves[word_index + mod_value]
                    # return the value to modify move
                    modifier_out = num_to_int[modifier_index]
                except:
                    print('nope')

        try:
            if self._modifier in self.modifiers['inputs']:
                _fetch_values('input')
                pass
            if self._modifier in self.modifiers['pointer']:
                pass
            if self._modifier in self.modifiers['direction']:
                pass
            if self._modifier in self.modifiers['other']:
                pass
            if self._modifier in self.modifiers['action']:
                pass
        except:
            self._clear_modifiers()



    def _execute_moves(self, move):
        pass
        # [i(move, direction) for i, x in self.available_moves.items() if move in x]


    def button_press(self, button, ):
        pass


    def analog_input(self):
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


moves = "press stick left for ten seconds then d-pad up twice and flick c stick down then press l2 and r1 to ride the bull then enter the konami code"
moves1 = "run right and press a button three times"
move = "stick"
direction = "left" # if not defined will default to last direction called
modifier = "press"
mod_move = "shield"
mod_time = 10

player = Controller(moves=moves)