import sys, time
from colorama import Fore

def brnslo(str):
     for char in str:
            time.sleep(.075)
            sys.stdout.write(char)
            sys.stdout.flush()

brnslo(Fore.RED + "InstaBRUTAL requires all Tor connections to be active in order to contine! Exiting........")

