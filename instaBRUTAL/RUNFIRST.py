import sys, time
from colorama import Fore, Style
def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.MAGENTA + "run this program to properly read instructions\n")
brnslo("before running instaBRUTAL install all prerequisite programs using 'bash install.sh\n'")
brnslo("this will also install the required python libraries for colorama\n")
brnslo("to run instaBRUTAL use the command 'bash instabrutal.sh' and watch the magick happen")

