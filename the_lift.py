class Dinglemouse(object):

    path = [0]
    queues = {}

    in_lift: list[int] = [] 
    current_floor: int

    capacity: int
    start: tuple[int, int] = (0, 0)

    def __init__(self, queues, capacity):
        self.capacity = capacity
        self.get_waiting_queues(queues)
        self.current_floor = 0
        pass


    def __check_if_full(self) -> bool:
        return len(self.in_lift) == self.capacity


    def move_to_floor(self, _index):
        self.current_floor = _index
        self.path.append(_index)
        pass


    def get_status(self):
        print(f'path = {self.path}\nin lift = {self.in_lift}\ncurrent queue = {self.queues}\n')
        pass


    def check_if_queues_empty(self) -> bool:
        for floor in self.queues:
            if len(self.queues[floor]) > 0:
                return False
        return True


    def get_waiting_queues(self, _queues):
        for _i, level in enumerate(_queues):
            self.queues[_i] = list(level)
        pass


    def unload_passengers(self, _floor: int):
        unload = []
        [unload.append(passenger) for passenger in self.in_lift if passenger==_floor]
        [self.in_lift.remove(_floor) for _i in unload]
        self.in_lift = sorted(self.in_lift)
        pass


    def pickup(self):
        for floor in self.queues:
            added = []
            if len(self.queues[floor]) > 0:
                self.move_to_floor(floor)
                self.in_lift.extend([_i for _i in self.queues[floor] if len(self.in_lift) < 5])
                self.queues[floor] = [_i for _i in self.queues[floor] if _i not in self.in_lift]

        self.in_lift = sorted(self.in_lift)
        pass


    def move(self):
        if len(self.in_lift) != 0:
            closest_floor: int = self.in_lift[0]
            self.move_to_floor(closest_floor)
            self.unload_passengers(closest_floor)
        else:
            self.pickup()
        pass


    def theLift(self):
        return []

# queue = ( (),   (),    (5,5,5, 3, 3, 4), (),   (),    (),    () ) #,     [0, 2, 5, 0]
queue = ( (),   (),    (5,5,5), (),   (),    (),    () ) 
# queue = ( (),   (3,),  (4,),    (),   (5,),  (),    () ) # [0, 1, 2, 3, 4, 5, 0]
# queue = ( (),   (),    (1,1),   (),   (),    (),    () ) # [0, 2, 1, 0]
# queue = ( (),   (0,),  (),      (),   (2,),  (3,),  () ) # [0, 5, 4, 3, 2, 1, 0]

lift = Dinglemouse(queue, 5)

while (not lift.check_if_queues_empty()) or len(lift.in_lift) != 0:
    lift.move()
    lift.get_status()

lift.move_to_floor(0)
lift.get_status()
