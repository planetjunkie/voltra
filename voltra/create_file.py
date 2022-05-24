import os


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





