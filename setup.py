def start():
    while True:
        print("Greetings traveller, what is your name?")
        name = input("> ")

        print("Are you ready to begin your quest? (Y/n)")
        ready = input("> ")
        if ready.lower() == "y" or ready.lower() == "yes":
            return name


