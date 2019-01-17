# SmashCom 
SmashCom is a custom vocal controller that takes user speech and converts the instructions to pre-set button inputs. Inspired by Super Smash Bros. and games with a deep lexicon, SmashCom can correctly interpret and use modifiers in colloquialisms to string more complex actions together. 

### Modifications and Community
SmashCom is currently designed and actionable for the Nintendo Gamecube, however, can be modified to work with any emulator by development of AddOn controller packs located in the Mods folder. If you want to try creating a NES, SNES, Playstation Dualshock or other controller scheme, or add game-specific language packs, please clone the repository and if it works we'll add it to the project. 

### Example: Smash Bros. Melee
The Smash Bros community has developed a wide list of unique (and borrowed from other fighters) move names that are used to describe gameplay. Terms like waveshine, flutterhush, or thunders describe both moves and combos - a series of buttons to be pressed in a particular order and timing. 

SmashCom will pick out words and then initaite moves/combos that it hears in your instructions, in the order it hears them. For example, "Fox, run right, multishine and jump", will input the sequence: analog stick right-->press down-B jump cancel x3-->press X to jump. It will only pay attention to the smash bros. specific instructions. SmashCom will apply modifiers like "hold", "wait', or "mash" with the specified number of seconds or button presses to create a whole different kind of dynamic gaming experience.  

## Setup

Current build: 1.0.6
OS Supported: Windows 10. 
Requirements: 
Python 3.6+ 
Speech Recognition
Keyboard

