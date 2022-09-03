import random
crpg = [
    """
    Welcome to

            ,o888888o.    8 888888888o.   8 888888888o       ,o888888o.    
           8888     `88.  8 8888    `88.  8 8888    `88.    8888     `88.  
        ,8 8888       `8. 8 8888     `88  8 8888     `88 ,8 8888       `8. 
        88 8888           8 8888     ,88  8 8888     ,88 88 8888           
        88 8888           8 8888.   ,88'  8 8888.   ,88' 88 8888           
        88 8888           8 888888888P'   8 888888888P'  88 8888           
        88 8888           8 8888`8b       8 8888         88 8888   8888888 
        `8 8888       .8' 8 8888 `8b.     8 8888         `8 8888       .8' 
           8888     ,88'  8 8888   `8b.   8 8888            8888     ,88'  
            `8888888P'    8 8888     `88. 8 8888             `8888888P'

    """,
    """
      .,-:::::      :::::::..       ::::::::::.       .,-:::::/  
    ,;;;``````      ;;;;``;;;;       `;;;```.;;;    ,;;-``````   
    [[[              [[[,/[[[`        `]]nnn]]`     [[[   [[[[[[/
    $$$              $$$$$$c           $$$``        `$$c.    `$$ 
    `88bo,__,o,      888b `88bo,       888o          `Y8bo,,,o88o
      `YUMMMMMP`     MMMM   `W`        YMMMb           ``YMUP`YMM
    """
]

def start():
    print(crpg[random.randint(0, len(crpg) - 1)])
    while True:
        print("Greetings traveller, what is your name?")
        name = input("> ")

        print("Are you ready to begin your quest? (Y/n)")
        ready = input("> ")
        if ready.lower() == "y" or ready.lower() == "yes":
            return name


