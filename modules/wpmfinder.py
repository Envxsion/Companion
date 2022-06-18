import curses
from curses import wrapper 
import time 
#curses overlays a screen on top of the terminal's standard output, making it do some very fancy stuff

def start_overlay(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!\n")
    stdscr.addstr("Press any key to start.\n")
    stdscr.refresh() 
    stdscr.getkey()
    wpm_test(stdscr)

def display_txt(stdscr,target, current,wpm=0,cpm=0): #wpm is options, not calulated yet
    stdscr.addstr(target)
    stdscr.addstr(1,1,f"WPM: {wpm}")
    stdscr.addstr(1,20,f"CPM: {cpm}")
    
    for i, char in enumerate(current): #i references the index (starts from 0), whereas char represents the actual character
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
    
def wpm_test(stdscr): 
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
    col = {v: k for k, v in colourdict.items()} #format start_color colors to key
    backgroundcol = curses.COLOR_BLACK
    
    curses.init_pair(1, 2, backgroundcol)
    attributes['valid'] = curses.color_pair(1)
    
    curses.init_pair(2, 4, backgroundcol)
    attributes['invalid'] = curses.color_pair(2)
    
    target_text = "The quick brown fox jumps over the lazy dog" #make this random using a RELIABLE api
    current_text = []       
    wpm = 0
    start_time = time.time()
    
    while True: 
        time_ela = max(time.time() - start_time, 1) #elapsed time, used max to avoid the "0 division error" in the cpm and wpm
        cpm = round(len(current_text)/(time_ela/60))
        wpm = round(cpm/5) #assuming average word have 5 chracters (4.7 on google, rounded for simplicity)
        stdscr.nodelay(True)#let's other events happen and doesn't stop the whole program just to wait for an input (so wpm and cpm can update in real time)
        
        stdscr.clear()
        display_txt(stdscr,target_text,current_text,wpm,cpm)
        stdscr.refresh()
        
        if "".join(current_text) == target_text: 
            stdscr.nodelay(False) #stop cpm/wpm timer
            end_screen(stdscr,wpm,cpm)
        
        try: #preventing a total crash, handling stdscr.nodelay 
            key = stdscr.getkey() 
        except:
            continue
        if ord(key) == 27: #ascii code for "esc"
            break
        
        if key in ("KEY_BACKSPACE", "\b", "\x7f"): #backspace for diff operating systems
            if len(current_text) > 0:
                current_text.pop()
                continue #this saved my life and like 30 mins holy shit
        elif len(current_text) < len(target_text):
                current_text.append(key)
                              
def end_screen(stdscr,wpm,cpm): 
    stdscr.addstr(3,3,f"You completed the test! Your wpm is: {wpm} and cpm is: {cpm}. Thank you for playing, press the escape key to exit... ")
            
