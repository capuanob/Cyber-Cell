from random import randint

# Populates a list of names from prisoner-names.txt
possible_names = list()
file = open("prisoner-names.txt", 'r')
for line in file:
    possible_names.append(line.rstrip())


class Person():
    full_name = ""
    schedule = list()

    def __eq__(self, other):
        # Check if two prisoners have the same data
        return self.full_name == other.full_name

    def info(self):
        # used for debugging, prints Person's information
        print(self.full_name)
        print(f"SCHEDULE IS: {self.schedule}")

    def _range_factory(self):
        # Returns a random integer between 15 and 75
        return randint(15, 75)

    def _name_factory(self, list):
        # Returns a full name in which the first name != last name
        first_name = list[randint(0, len(list) - 1)]
        last_name = list[randint(0, len(list) - 1)]
        while first_name == last_name:
            last_name = list[randint(0, len(list) - 1)]

        return f"{first_name} {last_name}"

    def __init__(self):
        self.full_name = self._name_factory(possible_names)


class Prisoner(Person):
    morale = 0
    job = None

    def __init__(self):
        # Sets name and morale
        super(Prisoner, self).__init__()
        self.morale = self._range_factory()


class Guard(Person):
    skill = 0
    is_dayguard = True

    def __init__(self):
        # Sets name and skill
        super(Guard, self).__init__()
        self.skill = self._range_factory()
