import sys

from colorama import Fore, init

init(autoreset=True)

print(Fore.GREEN + "Virtual Environment active and working")
print(Fore.CYAN + f" Current pyhton interpreter path:\n{sys.executable}")
