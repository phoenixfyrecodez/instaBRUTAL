import sys, time
from colorama import Fore

def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.RED + "you are not the user ROOT!! Please login as user ROOT and try again!!")
