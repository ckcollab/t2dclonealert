import colorama
import psutil
import pyttsx3

from colorama import Fore
from textwrap import dedent
from time import sleep


INITIAL_ADDRESSES = []


def get_process_by_name(name):
    for proc in psutil.process_iter():
        if proc.name() == name:
            return proc


def get_d2_ips():
    for c in get_process_by_name("D2R.exe").connections():
        try:
            ip, port = c.raddr
            yield ip
        except ValueError:
            pass


def set_initial_addresses():
    for ip in get_d2_ips():
        # print(f"Seen initial address: {ip}")
        INITIAL_ADDRESSES.append(ip)


def get_current_ip_from_d2():
    for ip in get_d2_ips():
        if ip not in INITIAL_ADDRESSES:
            return ip


if __name__ == '__main__':
    # For coloring console
    colorama.init(autoreset=True)

    print(dedent(f"""
    
     _   _____     _      _                  _                 _            
    | | / __  \   | |    | |                | |               | |           
    | |_`' / /' __| | ___| | ___  _ __   ___| |__  _   _ _ __ | |_ ___ _ __ 
    | __| / /  / _` |/ __| |/ _ \| '_ \ / _ \ '_ \| | | | '_ \| __/ _ \ '__|
    | |_./ /__| (_| | (__| | (_) | | | |  __/ | | | |_| | | | | ||  __/ |   
     \__\_____/\__,_|\___|_|\___/|_| |_|\___|_| |_|\__,_|_| |_|\__\___|_|   
     
    ***
    
    {Fore.RED}PLEASE START FROM LOBBY AREA, OUT OF GAME!
    """))

    sleep(1.5)

    input("Press enter when you are in lobby..\n")

    # What connections do we currently have? the game must be any new connections
    set_initial_addresses()

    # Set target ip, required
    while not (target_ip := input("What is your target IP, exactly? i.e. 35.233.255.233: ")):
        print("\n\nTarget IP is required, please enter one...\n\n")
    target_ip = target_ip.strip()  # remove whitespace, just in case it's in the copy + paste or something

    # Loop and look for the thing!
    while True:
        current_ip = get_current_ip_from_d2()
        print(f"Looking for IP: {target_ip}, current IP: {current_ip}")

        if current_ip == target_ip:
            print("@@@@@@@@@@@@@@@@@@@@ PLAY SOUND!")

            engine = pyttsx3.init()
            engine.say('We found the thing!!')
            engine.say('We found the thing!!')
            engine.say('We found the thing!!')
            engine.runAndWait()

            input("Press enter to exit..")
            exit(0)
        sleep(1)
