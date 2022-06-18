import curses
from curses import wrapper
from termcolor import cprint
from modules.wpmfinder import *
from modules.file_mng_auto import *
import time

def menu(title, classes, color='white'):
  def character(stdscr,):
    
    activities = {
        '0': start_overlay,
        '1': auto_file_main,
    }
    attributes = {}
    colourdict = {
      1:'red',
      2:'green',
      3:'yellow',
      4:'blue',
      5:'magenta',
      6:'cyan',
      7:'white'
    }
    backgroundcol = curses.COLOR_BLACK

    # make the 'normal' format
    curses.init_pair(1, 7, backgroundcol) #the number of the color-pair to be changed, the foreground color number, and the background color number
    attributes['normal'] = curses.color_pair(1)


    # make the 'highlighted' format
    curses.init_pair(2, 2, backgroundcol)
    attributes['highlighted'] = curses.color_pair(2)


    # handle the menu
    count = 0
    option = 0
    stop = True
    while count != 10:

        stdscr.erase() # clear the screen (you can erase this if you want)

        # add the title
        for c in range(0,len(title)): 
            til = [char for char in title]
            stdscr.addstr(f"{str(til[c])}", curses.color_pair(1) | curses.A_BOLD) #bitwise OR operator to pipe in 2 attributes
            if stop:
                time.sleep(0.05)
            stdscr.refresh()
        stdscr.addstr(f"\n") #new line
        stop = False #fixes a glitch where "Choose an option is painfully printed again and again after arrow press [find better fix for this]"

        for i in range(len(classes)):
            # handle the attributes
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # add the options
            stdscr.addstr(f'--> ', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)
        count = stdscr.getch()

        # arrow keys
        if count == curses.KEY_UP and option > 0:
            option -= 1
        elif count == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1
    activities[str(option)](stdscr)
    return option
  return curses.wrapper(character)
