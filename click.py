import os
import time
import random
import ctypes
import threading
from colorama import Fore, Back, Style, init
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
from libraries.definitions import update_title
from libraries.variables import project, color, description, version, author, devmode, verbose, running, min_cps, max_cps

init()
update_title(max_cps, min_cps, running)

print(f"""
    {color}{project} {Fore.LIGHTWHITE_EX}{version}
    {description} {Fore.LIGHTWHITE_EX}by {color}@{author}
""")


if devmode is False:
    print(f"     {color}Min CPS {Fore.LIGHTWHITE_EX}(MAX: 50){color}: ", end='')
    min_cps = float(input())
    update_title(max_cps, min_cps, running)
else:
    min_cps = 20
    print(f"     {color}Min CPS {Fore.LIGHTWHITE_EX}(MAX: 50){color}: {min_cps}")
    update_title(max_cps, min_cps, running)

if devmode is False:
    print(f"     {color}Max CPS {Fore.LIGHTWHITE_EX}(MAX: 70){color}: ", end='')
    max_cps = float(input())
    update_title(max_cps, min_cps, running)
else:
    max_cps = 50
    print(f"     {color}Max CPS {Fore.LIGHTWHITE_EX}(MAX: 70){color}: {max_cps}")
    update_title(max_cps, min_cps, running)

print("")

if devmode is False:
    print(f"     {color}Start/Stop button  (Recommended: 'r'): ", end='')
    start_stop = input()
else:
    start_stop = "r"

if devmode is False:
    print(f"     {color}Exit button  (Recommended: 'f'): ", end='')
    exit_button = input()
else:
    print(f"     {color}Exit button  (Recommended: 'f'): ")
    exit_button = "f"

print("")
print(f"   {color}Keybind to start/stop clicker: {Fore.LIGHTWHITE_EX}'" + start_stop + "'")
print(f"   {color}Keybind to exit clicker: {Fore.LIGHTWHITE_EX}'" + exit_button + "'")
print("")

button = Button.left
start_stop_key = KeyCode(char=start_stop)
exit_key = KeyCode(char=exit_button)

class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = 1/random.uniform(min_cps, max_cps)
        self.button = button
        self.running = False
        self.program_running = True
        
    def start_clicking(self):
        self.running = True
        running = True
        update_title(max_cps, min_cps, running)

    def stop_clicking(self):
        self.running = False
        running = False
        update_title(max_cps, min_cps, running)

    def exit(self):
        self.stop_clicking()
        print("")
        print(f"{Fore.LIGHTRED_EX}[EXITED]")
        print("")
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                if verbose is True:
                    print(f"{Fore.WHITE}[ VERBOSE ] {Fore.LIGHTWHITE_EX}" + str(1/random.uniform(min_cps, max_cps)))
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

mouse = Controller()
click_thread = ClickMouse(1/random.uniform(min_cps, max_cps), button)
click_thread.start()

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            print(f"{Fore.LIGHTWHITE_EX}Clicking is now {Fore.LIGHTRED_EX}Disabled")
            running = False
            update_title(max_cps, min_cps, running)
            click_thread.stop_clicking()
        else:
            print(f"{Fore.LIGHTWHITE_EX}Clicking is now {Fore.GREEN}Enabled")
            running = True
            update_title(max_cps, min_cps, running)
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()
