import argparse
from json.tool import main

## Define a few things


def create_project():
    print("Create a new project structure.")
    lang = input("What Language would you like to use? (Supported: Python) ")

    if lang == "Python" or "python":
        ("Language supported! Answer the following questions")
        proname = input("What is the name of your project? (e.g. MyProject) ")
        saveloc = input("Where would you like to create your project? (e.g. /home/user/Desktop/MyProject) ")
    else:
        print("UhOh! Language not supported! Please try again. (Tip: run voltra -C To try again")



parser = argparse.ArgumentParser(description='Voltra: A tool for analyzing and visualizing the output of Voltra.')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1 Public RC')
parser.add_argument('-c', '--create', action= create_project(), help='Create a new project structure.')




args = parser.parse_args()

