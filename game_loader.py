from operator import le
import os
import textwrap
from pyfiglet import Figlet


#Read all dl files located in GameLibary, lists them to user, and return level chosen by user to game generate
def selectDL():
    bannerPrinter()
    path = "game_libary"
    dir_list = os.listdir(path)
    count = 0
    options = "(0) - Exit\n"
    for dl in dir_list:
        count = count + 1
        options += "(" +str(count)+ ") - " + dl +"\n"
    print("Please choose from the following options\n"+'_'*45)
    print(options)
    userIn = str(input())
    while inputCheck(userIn , count):
        print("Please choose from the following options\n"+'_'*45)
        print(options)
        userIn = str(input())
    if(int(userIn) == 0):
        return -1
    else :
        return dir_list[int(userIn)-1]

#Prints Intro Banner - a bit messy
def bannerPrinter():
        print("*" * 100)
        f = Figlet(font = "roman")
        print(f.renderText("Classic RPG"),end=' ')
        print("by".center(100))
        print("MakeOpenSource".center(100))
        print("University at Buffalo".center(100))
        print("GPL-3.0 license".center(100))
        print("*" * 100 + "\n")
        
#check user input is valid        
def inputCheck(value , lenght):
    if(value.isnumeric()):
        return not ((-1 < int(value) ) and (int(value)<lenght+1))
    else:
        return True
    
 
