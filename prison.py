from person import Guard, Prisoner
import room
from random import randint


def populate_workable_rooms():
    for r in ROOM_LIST:
        if type(r) in [room.Kitchen, room.Laundry_Room, room.Delivery_Bay]:
            WORKABLE_ROOMS.append(r)


ROOM_LIST = [room.Gymnasium(), room.Cafeteria(), room.Kitchen(), room.Laundry_Room(),
             room.Medical(), room.Solitary(), room.Yard(), room.Cell_Area(), room.Delivery_Bay(), room.Cell()]
WORKABLE_ROOMS = []
populate_workable_rooms()
STARTING_PRISONER_COUNT = randint(35, 65)
# Starting guard count will be between 2/3 of the rooms and all of the rooms
STARTING_GUARD_COUNT = randint(round(2/3 * len(ROOM_LIST)), len(ROOM_LIST))


class Prison():
    rooms = list()
    guards = list()
    prisoners = list()

    def __init__(self):
        # Populating necessary lists
        for room in ROOM_LIST:
            self.add_room(room)

        for _ in range(0, STARTING_PRISONER_COUNT):
            self.add_prisoner(Prisoner())

        for _ in range(0, STARTING_GUARD_COUNT):
            self.add_guard(Guard())

        self.remove_duplicates()
        self.assign_nightguards()
        self.assign_schedules()

    def assign_nightguards(self):
        # 1/3 of guards are set to be nightguards.
        for i in range(0, round(len(self.guards) / 3)):
            self.guards[i].is_dayguard = False

    def pick_guard_room(self, guard):
        # Returns a room (that isn't the cell or cafeteria) for a guard to patrol
        picked = ROOM_LIST[randint(0, len(ROOM_LIST) - 1)]
        if guard.is_dayguard:
            while type(picked) in [room.Cafeteria, room.Cell]:
                picked = ROOM_LIST[randint(0, len(ROOM_LIST) - 1)]
        else:
            while type(picked) not in [room.Cell_Area, room.Yard, room.Solitary]:
                picked = ROOM_LIST[randint(0, len(ROOM_LIST) - 1)]
        return picked

    def assign_schedules(self):
        # Assigns schedules to all persons on a 24 hour scale.
        for i, person in enumerate(self.guards):
            self.guards[i].schedule = []
            if person.is_dayguard:
                breakfast_time = randint(6, 8)
                lunch_time = randint(11, 14)
                dinner_time = randint(17, 22)

                for hour in range(0, 24):
                    if hour < 6 or hour == 23:
                        # Sleep from 12:00pm - 6:00am
                        self.guards[i].schedule.append(None)
                    elif hour in [breakfast_time, lunch_time, dinner_time]:
                        # Guards are in cafeteria during these times
                        cafeteria = next(
                            (x for x in ROOM_LIST if type(x) == room.Cafeteria), None)
                        self.guards[i].schedule.append(cafeteria)
                    else:
                        # Guards patrol a randomized room
                        self.guards[i].schedule.append(
                            self.pick_guard_room(self.guards[i]))
            else:
                # Night guards
                for hour in range(0, 24):
                    if hour < 6 or hour == 23:
                        self.guards[i].schedule.append(
                            self.pick_guard_room(self.guards[i]))
                    else:
                        self.guards[i].schedule.append(None)

        for i, person in enumerate(self.prisoners):
            self.prisoners[i].schedule = []
            for hour in range(0, 24):
                if hour < 6 or hour == 23:
                    # Prisoners sleep from 0-6 and 23
                    cell = next(
                        (x for x in ROOM_LIST if type(x) == room.Cell), None)
                    self.prisoners[i].schedule.append(cell)
                elif hour in [6, 11, 17]:
                    # Prisoners are in cafeteria for food
                    cafeteria = next(
                        (x for x in ROOM_LIST if type(x) == room.Cafeteria), None)
                    self.prisoners[i].schedule.append(cafeteria)
                elif hour in [14, 15, 16]:
                    # Prisoner free time, can go anywhere
                    self.prisoners[i].schedule.append(
                        ROOM_LIST[randint(0, len(ROOM_LIST) - 1)])
                elif hour in [18, 19, 20]:
                    # For both morale activities and cell area free time
                    cell_area = next(
                        (x for x in ROOM_LIST if type(x) == room.Cell_Area), None)
                    self.prisoners[i].schedule.append(cell_area)
                else:
                    # Prisoners working at their job
                    job_area = next(
                        (x for x in ROOM_LIST if type(x) == self.prisoners[i].job), None)
                    self.prisoners[i].schedule.append(job_area)

    def add_room(self, room):
        # Adds a given room to the rooms list
        self.rooms.append(room)

    def add_prisoner(self, prisoner):
        # Adds a given prisoner to the prisoners list
        for p in self.prisoners:
            # Checks if prisoner of same name is already in the prison.
            if prisoner == p:
                break
        prisoner.job = type(
            WORKABLE_ROOMS[randint(0, len(WORKABLE_ROOMS) - 1)])
        self.prisoners.append(prisoner)

    def add_guard(self, guard):
        # Adds a given guard to the guards list
        for g in self.guards:
            # Checks if guard of same name is already in the prison.
            if guard == g:
                break
        self.guards.append(guard)

    def remove_duplicates(self):
        # If a name is both a prisoner and a guard, it is removed from both lists
        for p in self.prisoners:
            for g in self.guards:
                if p == g:
                    self.prisoners.remove(p)
                    self.guards.remove(g)

    def info(self):
        # Easy way to view current prison information
        prisoner_names = list()
        guard_names = list()
        for prisoner in self.prisoners:
            prisoner_names.append(prisoner.full_name)
        for guard in self.guards:
            guard_names.append(guard.full_name)
