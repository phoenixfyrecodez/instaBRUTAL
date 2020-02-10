import sys, time
from colorama import Fore, Style
def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.RED + "	a phoenixfyre code \n")
