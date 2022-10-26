from email.policy import default
from importlib.resources import path
from operator import le
from operator import mul
import os
import textwrap
import click
from pyfiglet import Figlet
from crgp import generate
from functools import reduce
from os.path import exists

GAME_LIBRARY = "game_library"

#Allows adding specifications when starting program; at the moment, only add the ability to specify exact file path or folder for .dl
@click.command()
@click.option("--path", default= None, help="Provide file path to a .dl file not located under /game_library")
@click.option("--folder", default=None, help="Provide folder to list of .dl files, --path Take priority")
def start(path, folder):
    #Checks if user specified a .dl file or folder and access it, otherwise gives default game options
    if((folder == None) and (path == None)):
        runDefault()

    elif( (path != None) ):
        letUserSelectFile(path)

    elif(folder != None ):
        letUserSelectFolder(folder)
    
def letUserSelectFile(path):
    defaultChosen=False
    while((not exists(path)) and (not defaultChosen)):
        print("Could not locate file, either try again(0) or run default(1)")
        userIn = getUserInput(2,"Could not locate file, either try again(0) or run default(1)")
        if(userIn == "1"):
            defaultChosen=True
        else:
            print("Enter file Path")
            path = str(input())    

    if(exists(path)):
        game = generate(path)
        game.start()
    else:
        runDefault()

def letUserSelectFolder(folder):
    defaultChosen=False
    while((not exists(folder)) and (not defaultChosen)):
        print("Could not locate folder, either try again(0) or run default(1)")
        userIn = getUserInput(2,"Could not locate folder, either try again(0) or run default(1)")
        if(userIn == "1"):
            defaultChosen=True
        else:
            print("Enter folder Path")
            folder = str(input())    

    if(exists(folder)):
        game = generate(selectDL(folder))
        game.start()
    else:
        runDefault()

def runDefault():
    game = generate(selectDL(GAME_LIBRARY))
    game.start()

#Prints all files in given path, and passes user selected file path back
def selectDL(path):
    bannerPrinter()
    dir_list = os.listdir(path)
    count = 0
    options = "(0) - Exit\n"
    for dl in dir_list:
        count = count + 1
        options += "(" +str(count)+ ") - " + dl +"\n"
    print("Please choose from the following options\n"+'_'*45)
    print(options)
    userIn = getUserInput(count , options)
    if(int(userIn) == 0):
        exit(0)
    else :
        return path + "/" +dir_list[int(userIn)-1]

#Prints Intro Banner - a bit messy
def bannerPrinter():
        print("*" * 100)
        f = Figlet(font = "roman")
        print(f.renderText("Classic RGP"),end=' ')
        print("by".center(100))
        print("MakeOpenSource".center(100))
        print("University at Buffalo".center(100))
        print("GPL-3.0 license".center(100))
        print("*" * 100 + "\n")
        
#check user input is valid        
def inputCheck(value , length):
    if(value.isnumeric()):
        return not ((-1 < int(value) ) and (int(value)<length+1))
    else:
        return True
#Handles accepting user input and checking it is valid
def getUserInput(length , options):
    userIn = str(input())
    while inputCheck(userIn , length):
        print("Please choose from the following options\n"+'_'*45)
        print(options)
        userIn = str(input())
    return userIn

#Set up for Python Click
if __name__ == '__main__':
    start()