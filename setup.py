import random
from pyfiglet import Figlet

fonts = ["6x9", "banner", "big", "block", "bubble", "chartr", "chartri", "cour", "digital", "helv", "ivrit", "lean",
         "mini", "mnemonic", "sbook", "script", "shadow", "slant", "small", "smscript", "smshadow", "smslant",
         "standard", "term", "times", "xchartr"]


def start():
    font_idx = random.randint(0, len(fonts) - 1)
    f = Figlet(font=fonts[font_idx])
    print(f.renderText('Classic RPG'))

    while True:
        print("Greetings traveller, what is your name?")
        name = input("> ")

        print("Are you ready to begin your quest? (Y/n)")
        ready = input("> ")
        if ready.lower() == "y" or ready.lower() == "yes":
            return name
