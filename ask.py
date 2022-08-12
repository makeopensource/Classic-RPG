import yaml


class Ask:
    def __init__(self, question, choices):
        self.question = question
        self.choices = choices

    def __enter__(self):
        while True:
            choice_list = [f"{i + 1}] {x}" for i, x in enumerate(self.choices)]
            print("\n".join(choice_list))
            item = input(self.question + ": ")

            try:
                self.choice_idx = int(item) - 1
                self.choice = self.choices[self.choice_idx]
                return self

            except (ValueError,TypeError,IndexError):
                print("Invalid input")

    def get_location(self, game):
        return game["locations"][self.choice_idx]

    def get_event(self, location):
        return location["events"][self.choice_idx]

    def get_action(self, event):
        event = self.get_event(location)
        return event["actions"][self.choice_idx]


def ask(question, choices):
    choice_list = [f"{i + 1}] {x}" for i, x in enumerate(choices)]
    print("\n".join(choice_list))
    item = input(question + ": ")

    try:
        choice_idx = int(item) - 1
        retval = choices[choice_idx]
        return choice_idx, retval

    except (ValueError,TypeError,IndexError):
        raise ValueError("Invalid input")


def get_titles(obj):
    return [x["title"] for x in obj]


game = yaml.safe_load(open("actions.yml", 'r'))



while True:
    try:
        locations = game["locations"]
        idx, location = ask("choose a location", get_titles(locations))

        events = locations[idx]["events"]
        idx, event = ask("choose an event", get_titles(events))

        actions = events[idx]["actions"]
        idx, action = ask("choose an action", get_titles(actions))

        print(actions[idx])
        print("you have chosen to " + action)

    except ValueError as e:
        print(e)
