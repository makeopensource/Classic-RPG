import yaml


class Ask:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

    def __enter__(self):
        while True:
            choice_list = [f"{i + 1}] {x['title']}" for i, x in enumerate(self.choices)]
            print("\n".join(choice_list))
            item = input(self.question + ": ")

            try:
                idx = int(item) - 1
                self.choice = self.choices[idx]
                return self

            except (ValueError,TypeError,IndexError):
                print("Invalid input")

    def get_choice(self):
        return self.choice

    def __exit__(self, type, value, traceback):
        pass

class Hero:
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.xp = 0

    def __str__(self):
        return f"""{self.name}
                gold: {self.gold}
                xp: {self.xp}
                """


def get_titles(obj):
    return [x["title"] for x in obj]


game = yaml.safe_load(open("actions.yml", 'r'))
hero = Hero(game["hero"])

with Ask("choose a location", game["locations"]) as location_question:
    location = location_question.get_choice()

    while True:
        with Ask("choose an event", location["events"]) as event_question:
            event = event_question.get_choice()

            with Ask("choose an action", event["actions"]) as action_question:
                action = action_question.get_choice()
                hero.gold += action["gold"]
                hero.xp += action["xp"]
                print("you chose to " + action["title"])
                print(hero)
