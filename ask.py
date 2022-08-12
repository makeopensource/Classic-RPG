import yaml


def repeat(func):
    def helper(*args, **kwargs):
        while True:
            try:
                func(*args, **kwargs)
            except ValueError:
                break
 
    return helper


class Ask:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

    def __enter__(self):

        if len(self.choices) <= 0:
            return self

        while True:
            choice_list = [f"{i + 1}] {x['title']}" for i, x in enumerate(self.choices)]
            print("\n".join(choice_list))
            try:
                item = input(self.question + ": ")
                idx = int(item) - 1
                self.choice = self.choices[idx]
                return self

            except (ValueError,TypeError,IndexError):
                print("Invalid input")

            except (EOFError,KeyboardInterrupt):
                print("\nThanks for playing!")
                exit(0)


    def get_choice(self):
        return self.choice

    def __exit__(self, type, value, traceback):
        pass

class Hero:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.xp = 0
        self.hp = 100

    def add_stats(self, gold = 0, xp = 10, hp = 0):
        gold, xp = int(gold), int(xp)
        self.gold = max(self.gold + gold, 0)
        self.xp = max(self.xp + xp, 0)
        self.hp = min(max(self.hp + hp, 0), 100)

    def __str__(self):
        return f"""
{self.name}
gold: {self.gold}
xp: {self.xp}
hp: {self.hp}
        """


def init_game(filename):
    game = yaml.safe_load(open(filename, 'r'))
    hero = Hero(game["hero"])
    ask_location(game, hero)


def ask_action(event, hero):
    with Ask("choose an action", event["actions"]) as action_question:
        action = action_question.get_choice()
        hero.add_stats(action["gold"], action["xp"], action["hp"])

        if hero.hp == 0:
            print("THE HERO HAS DIED IN BATTLE")
            exit(0)

        print("you chose to " + action["title"])
        print(hero)


@repeat
def ask_event(location, hero):
    with Ask("choose an event", location["events"]) as event_question:
        if len(event_question.choices) == 0:
            raise ValueError("all events completed")

        event = event_question.get_choice()
        ask_action(event, hero)


@repeat
def ask_location(game, hero):
    with Ask("choose a location", game["locations"]) as location_question:
        location = location_question.get_choice()
        ask_event(location, hero)


init_game("actions.yml")

