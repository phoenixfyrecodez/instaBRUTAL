import sys, time
from colorama import Fore

def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.GREEN + "Filename of wordlist (Press enter to choose default list)")
