import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

### Player setup ###

class player:
  def __init__(self):
    self.name = ''
    self.hp = 0
    self.mp = 0
    self.status_effects = []
    self.location = 'start'
    
myPlayer = player()

#### Title Screen ####

def title_screen_selections():
  option = input("> ")
  if option.lower() == ("play"):
    start_game() #placeholder
  elif option.lower() == ("help"):
    help.menu()
  elif option.lower() == ("quit"):
    sys.exit()
    
  while option.lower() not in ('play', 'help', 'quit'):
    print("Please enter a valid command.")
    option = input("> ")
    if option.lower() == ("play"):
      start_game() #placeholder
    elif option.lower() == ("help"):
      help.menu()
    elif option.lower() == ("quit"):
      sys.exit()
      
def title_screen():
  os.system('clear')
  print("##################################")
  print(" Welcome to the Text RPG!!!!")
  print("##################################")
  print("         Play          ")
  print("         Help          ")
  print("         Quit          ")
  title_screen_selections()
  
def help_menu():
  print("##################################")
  print("           Help Menu              ")
  print("##################################")
  print(" Use up, down, left, right to move")
  print(" Type your commands to do them    ")
  print(" Use [look] to inspect something  ")
  print("    Good luck and have fun!       ")
  title_screen_selections()
  
### game functionality
def start_game():
  
  

#### MAP ######
# player starts at b2

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
                }

zonemap = {
  'a1': {
    ZONENAME: "Town Market",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = '',
    DOWN = 'b1'
    LEFT = ''
    RIGHT = 'a2'
  },
  'a2': {
    ZONENAME: "Town Entrance",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = ''
    DOWN = 'b2'
    LEFT = 'a1'
    RIGHT = 'a3'
  },
  'a3': {
    ZONENAME: "Town Square",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = ''
    DOWN = 'b3'
    LEFT = 'a2'
    RIGHT = 'a4'
  },
  'a4': {
    ZONENAME: "Town Hall",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = ''
    DOWN = 'b4'
    LEFT = 'a3'
    RIGHT = ''
  },
  'b1': {
    ZONENAME: "Level B1",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = 'a1'
    DOWN = ''
    LEFT = ''
    RIGHT = 'b2'
  },
  'b2': {
    ZONENAME: "Home",
    DESCRIPTION = 'This is your home!'
    EXAMINATION = 'Your home looks the same - nothing has changed'
    SOLVED = False
    UP = 'a2',
    DOWN = 'c2',
    LEFT = 'b1',
    RIGHT = 'b3',
  },
  'b3': {
    ZONENAME: "Level b3",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = 'a3'
    DOWN = ''
    LEFT = 'b2'
    RIGHT = 'b4'
  },
  'b4': {
    ZONENAME: "Level B4",
    DESCRIPTION = 'description'
    EXAMINATION = 'examine'
    SOLVED = False
    UP = 'a4'
    DOWN = ''
    LEFT = 'b3'
    RIGHT = ''
  }
}
