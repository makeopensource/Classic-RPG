from operator import le
import os

#Read all dl files located in GameLibary, lists them to user, and return level chosen by user to game generate
def selectDL():
    bannerPrinter()
    path = "GameLibary"
    dir_list = os.listdir(path)
    count = 0
    options = "(0) - Exit\n"
    for dl in dir_list:
        count = count + 1
        options += "(" +str(count)+ ") - " + dl +"\n"
    print(options)
    print("Please choose from the following options")
    print("_________________________________________")
    userIn = str(input())
    while inputCheck(userIn , count):
        print("Please choose from the following options")
        print("_________________________________________")
        print(options)
        userIn = str(input())
    if(int(userIn) == 0):
        return -1
    else :
        return dir_list[int(userIn)-1]

#Prints contents in bannerIntro.txt
def bannerPrinter():
    with open ("GameAssets/bannerIntro.txt" , 'r') as title:
        for line in title:
            print(line , end = ' ')
        print("\n")
        
#check user input is valid        
def inputCheck(value , lenght):
    if(value.isnumeric()):
        return not ((-1 < int(value) ) and (int(value)<lenght+1))
    else:
        return True
    
 
