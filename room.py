from person import Guard
from person import Prisoner


class Room():
    occupants = list()
    # The lower the number, the easier the escape 0...5
    ease_of_escape = 0

    def define_ease_of_escape(self):
        # Based off guard count, number of prisoner count. Returns a number representing ease of escape
        num = 0
        for person in self.occupants:
            if type(person) is Guard:
                num += 0.5
            else:
                num -= 0.05
        return num

    def __init__(self, modifier):
        new_ease = modifier + self.define_ease_of_escape()
        self.ease_of_escape = 5 if new_ease > 5 else new_ease


class Yard(Room):
    def __init__(self):
        super(Yard, self).__init__(4)


class Gymnasium(Room):
    def __init__(self):
        super(Gymnasium, self).__init__(3)


class Cafeteria(Room):
    def __init__(self):
        super(Cafeteria, self).__init__(1.25)


class Cell_Area(Room):
    def __init__(self):
        super(Cell_Area, self).__init__(4.5)


class Cell(Room):
    def __init__(self):
        super(Cell, self).__init__(3.25)


class Laundry_Room(Room):
    def __init__(self):
        super(Laundry_Room, self).__init__(0)


class Solitary(Room):
    def __init__(self):
        super(Solitary, self).__init__(5)


class Kitchen(Room):
    def __init__(self):
        super(Kitchen, self).__init__(0.25)


class Medical(Room):
    def __init__(self):
        super(Medical, self).__init__(3.5)


class Delivery_Bay(Room):
    def __init__(self):
        super(Delivery_Bay, self).__init__(0.15)
