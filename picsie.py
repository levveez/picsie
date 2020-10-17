import os
from decoration import *
from sys import platform


def clear():
    if platform == 'linux' or 'linux2':
        os.system('clear')
    elif platform == 'darwin':
        pass 
    elif platform == 'win32':
        os.system('cls')
    else:
        pass


print(banner)

filename = input(f"{red}Enter file{pink}name >>{res} ")
picname = input(f"{red}Enter pi{pink}c name >>{res} ")

try:
    os.system(f'copy /b {picname} + {filename} output.png')
except Exception as e:
    print(e)



