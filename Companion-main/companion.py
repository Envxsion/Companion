#COMPANION
version= '0.0.1'

#import all modules
from modules.optionhandler import *
from termcolor import cprint
import time

def splash():
	cprint(f"""


░█████╗░░█████╗░███╗░░░███╗██████╗░░█████╗░███╗░░██╗██╗░█████╗░███╗░░██╗
██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔══██╗████╗░██║██║██╔══██╗████╗░██║
██║░░╚═╝██║░░██║██╔████╔██║██████╔╝███████║██╔██╗██║██║██║░░██║██╔██╗██║
██║░░██╗██║░░██║██║╚██╔╝██║██╔═══╝░██╔══██║██║╚████║██║██║░░██║██║╚████║
╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░░░░░██║░░██║██║░╚███║██║╚█████╔╝██║░╚███║
░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░░╚══╝         
				
                                > Multipurpose tool
				> Created by Envxsion
                                > v{version}

                    """, 'cyan', attrs=['bold'])

def companion():
    splash()
    cprint("WARNING: Remember to change the file locations in the source code of the auto file manager or this will not work for you!\n",'red')
    cprint("NOTE: Auto file manager automatically detects if something has been downloadedd, deleted and moved and sorts everything into specified folders.\n",'red')
if __name__ == '__main__':
    try:
        companion()
        time.sleep(4)
        print(f"Chosen Selection: ", menu('Choose an option - ', ['WPM Test','Auto File Manager','Another option'], 'blue'))
    except KeyboardInterrupt:
        cprint("\nKeyboard Interrupt received! Aborted!", 'red')
