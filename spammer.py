import os
import time
import sys
from colored import  fg, attr
from colorama import Fore, init, Style
from easygui import fileopenbox
import ctypes
from dhooks import Webhook

ctypes.windll.kernel32.SetConsoleTitleW("Webhooker - Vertixx")
os.system('cls')

logo = f'''{Fore.RED} __    __     _                       _             
/ / /\ \ \___| |__   /\  /\___   ___ | | _____ _ __ 
\ \/  \/ / _ \ '_ \ / /_/ / _ \ / _ \| |/ / _ \ '__|
 \  /\  /  __/ |_) / __  / (_) | (_) |   <  __/ |   
  \/  \/ \___|_.__/\/ /_/ \___/ \___/|_|\_\___|_|   
    '''

main = f'''{Fore.RED} __    __     _                       _             
/ / /\ \ \___| |__   /\  /\___   ___ | | _____ _ __ 
\ \/  \/ / _ \ '_ \ / /_/ / _ \ / _ \| |/ / _ \ '__|
 \  /\  /  __/ |_) / __  / (_) | (_) |   <  __/ |   
  \/  \/ \___|_.__/\/ /_/ \___/ \___/|_|\_\___|_|   
                                                    
 {Fore.WHITE}[{Fore.LIGHTBLACK_EX}{Fore.RED}1{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}{Fore.WHITE}- {Fore.LIGHTBLACK_EX}{Fore.WHITE}Spammer
 {Fore.WHITE}[{Fore.LIGHTBLACK_EX}{Fore.RED}3{Fore.WHITE}{Fore.WHITE}] {Fore.LIGHTBLACK_EX}{Fore.WHITE}- {Fore.LIGHTBLACK_EX}{Fore.WHITE}Exit
    '''
print(main)
mainmenu = input('%s >> %s' % (fg(9), attr(0)))

if mainmenu == '1':
    os.system('cls')
    print(logo)
    url = input(f'{Fore.WHITE}Your Webhook URL: ')
    os.system('cls')
    print(logo)
    text = input(f'{Fore.WHITE}Your Text: ')
    os.system('cls')
    print(logo)
    number = int(input(f'{Fore.WHITE}Number Of Messages: '))
    os.system('cls')
    print(logo)

    hook = Webhook(url)
    for x in range(number): 
        hook.send(f'{text}')
    else:
        print("Finished Spamming")
