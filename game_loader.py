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

#Allows adding specifications when starting program; at the moment, only add the ability to specify exact file path for .dl
@click.command()
@click.option("--path", default="game_library", help="Provide file path to a .dl file not located under /game_library")
def start(path):
    #Possible could be more elegant, checks if user specified path; if path exist runs it
    if(path == "game_library"):
        dl = selectDL(path)
    else:
        defaultChosen=False
        while((not exists(path)) and (not defaultChosen)):
            print("Could not locate file, either try again(0) or run default(1)")
            userIn = getUserInput(2)
            if(userIn == "1"):
                defaultChosen=True
            else:
                print("Enter file Path")
                path = str(input())    
        if(defaultChosen):
            path = "game_library"
            dl = selectDL(path)
        else:
            dl = path

    if( str(dl) != "-1"):
        game = generate(dl)
        game.start()
    else:
        print("Exiting")
        exit(0)

#Read all dl files located in GameLibrary, lists them to user, and return level chosen by user to game generate

#Prints all files in given path, and passes selected file path
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
    userIn = getUserInput(count)
    if(int(userIn) == 0):
        return -1
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
def getUserInput( length):
    userIn = str(input())
    while inputCheck(userIn , length):
        print("Please choose from the following options\n"+'_'*45)
        print(options)
        userIn = str(input())
    return userIn

#Set up for Python Click
if __name__ == '__main__':
    start()