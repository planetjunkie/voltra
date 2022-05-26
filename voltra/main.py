import argparse
import os
from venv import create
import time


def main():
    parser = argparse.ArgumentParser(description='Voltra: A tool made to help you create a new project structure.')
    parser.add_argument('-v', '--version', action='version', version='Voltra 0.5 Public RC')
    parser.add_argument("-C", "--create", help="Create a new project structure.", action="store_true")
    args = parser.parse_args()

    if args.create:
        create_file()
    else:
        print("Please use the -C flag to create a new project structure.")

def create_file():
    print("Create a new project structure.")
    language = input("What Language would you like to use? (Supported: Python, C/C++) > ")
    proname = input("What is the name of your project? (e.g. MyProject) > ")
    saveloc = input("Where would you like to create your project? (e.g. /home/user/Desktop/MyProject) > ")
    ## The loading is intentional to show the user that the program is working.
    
    def py():
        print("Creating project structure...")
        print("Loading ......")
        time.sleep(1)
        print("Loading |.....")
        time.sleep(1)
        print("Loading ||....")
        time.sleep(1)
        print("Loading |||...")
        time.sleep(1)
        print("Loading ||||..")
        time.sleep(1)
        print("Loading |||||.")
        time.sleep(1)
        print("Loading ||||||")
        time.sleep(1)


        os.mkdir(saveloc + "/" + proname)
        os.mkdir(saveloc + "/" + proname + "/" + proname)
        os.mkdir(saveloc + "/" + proname + "/" + "test")

    def C_lang():
        print("Creating project structure...")
        print("Loading ......")
        time.sleep(1)
        print("Loading |.....")
        time.sleep(1)
        print("Loading ||....")
        time.sleep(1)
        print("Loading |||...")
        time.sleep(1)
        print("Loading ||||..")
        time.sleep(1)
        print("Loading |||||.")
        time.sleep(1)
        print("Loading ||||||")
        time.sleep(1)

        ##this is a mess :3
        os.mkdir(saveloc + "/" + proname)
        os.mkdir(saveloc + "/" + proname     + "/" + "src")
        os.mkdir(saveloc + "/" + proname + "/" + "test")
        os.mkdir(saveloc + "/" + proname + "/" + "tools")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug" + "/" + "lib")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release" + "/" + "lib")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug" + "/" + "include")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release" + "/" + "include")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug" + "/" + "src")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release" + "/" + "src")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug" + "/" + "test")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release" + "/" + "test")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "debug" + "/" + "test" + "/" + "src")
        os.mkdir(saveloc + "/" + proname + "/" + "tools" + "/" + "build" + "/" + "linux" + "/" + "x64" + "/" + "release" + "/" + "test" + "/" + "src")
        
    if language == "Python" or language == "python" or language == "PYTHON" or language == "Python3" or language == "python3" or language == "PYTHON3" or language == "py" or language == "Py" or language == "PY":
        print("Python Language Template coming in!")
        time.sleep(0.1)
        py()
    elif language == "C" or language == "c" or language == "C++" or language == "c++":
        print("C/C++ Language Template coming in!")
        time.sleep(0.1)
        C_lang()
    else:
        print("Sorry, that language is not supported yet.")
        time.sleep(2)
        os.system("clear")
        create_file()   





main()

