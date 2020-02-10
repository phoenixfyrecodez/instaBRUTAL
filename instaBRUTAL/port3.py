import sys, time
from colorama import Fore

def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.GREEN + "\n[*] Starting Tor connection on port 9053........")

