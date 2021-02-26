import ctypes
import os
from libraries.variables import project, color, description, version, author, devmode, verbose, running, min_cps, max_cps

def update_title(max_cps, min_cps, running):
    ctypes.windll.kernel32.SetConsoleTitleW(f"Mercy | Min: {min_cps} | Max: {max_cps} | Clicking: {running}")

def clear():
    os.system("cls")
