import argparse
import os
from venv import create

## This is a temporary fix excuse me :(

def main():
    parser = argparse.ArgumentParser(description='Voltra: A tool made to help you create a new project structure.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.4 Public RC')
    parser.add_argument("-C", "--create", help="Create a new project structure.", action="store_true")
    args = parser.parse_args()

    if args.create:
        create_file()
    else:
        print("Please use the -C flag to create a new project structure.")

def create_file():
    print("Create a new project structure.")
    lang = input("What Language would you like to use? (Supported: Python) ")

    if lang == "Python" or "python":
        ("Language supported! Answer the following questions")
        proname = input("What is the name of your project? (e.g. MyProject) ")
        saveloc = input("Where would you like to create your project? (e.g. /home/user/Desktop/MyProject) ")

        print("Creating project structure...")
        os.mkdir(saveloc + "/" + proname)
        os.mkdir(saveloc + "/" + proname + "/" + proname)
        os.mkdir(saveloc + "/" + proname + "/" + "test")

    else:
        print("UhOh! Language not supported! Please try again. (Tip: run voltra -C To try again")





main()

