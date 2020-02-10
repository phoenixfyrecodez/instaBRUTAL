import sys, time
from colorama import Fore, Style
def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.YELLOW + 'Starting............\n')
brnslo('Press Ctrl + C to Stop/Save session..........')
