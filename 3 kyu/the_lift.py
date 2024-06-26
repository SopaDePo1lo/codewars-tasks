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
        self.in_lift = []
        self.current_floor = 0
        self.path = [0]
        pass


    def __check_if_full(self) -> bool:
        return len(self.in_lift) == self.capacity


    def filter_path(self):
        [self.path.pop(_i) for _i in range(len(self.path)-2) if self.path[_i]==self.path[_i+1]]


    def move_to_floor(self, _index):
        self.current_floor = _index
        self.path.append(_index)
        pass


    def get_status(self):
        print(f'path = {self.path}\nin lift = {self.in_lift}\n\ncurrent floor = {self.current_floor}\ncurrent queue = {self.queues}\n')
        pass


    def check_if_queues_empty(self) -> bool:
        for floor in self.queues:
            if len(self.queues[floor]) > 0:
                return False
        return True


    def check_passing_floors(self, floor):
        if floor in self.in_lift:
            self.move_to_floor(floor)
            self.unload_passengers(floor)


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

## need to work on this, so if doesnt pick up all the passangers at once :)))
    def pickup(self): 
        for floor in self.queues:
            self.check_passing_floors(floor)
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
        while (not self.check_if_queues_empty()) or len(self.in_lift) != 0:
            self.move()
            # self.get_status()
        self.move_to_floor(0)
        self.filter_path()
        return self.path

# queue = ( (),   (),    (5,5,5, 3, 3, 4), (),   (),    (),    () ) #,     [0, 2, 5, 0]
# queue = ( (),   (),    (5,5,5), (),   (),    (),    () ) 
# queue = ( (),   (3,),  (4,),    (),   (5,),  (),    () ) # [0, 1, 2, 3, 4, 5, 0]
# queue = ( (),   (),    (1,1),   (),   (),    (),    () ) # [0, 2, 1, 0]
# queue = ( (),   (0,),  (),      (),   (2,),  (3,),  () ) # [0, 5, 4, 3, 2, 1, 0]

lift = Dinglemouse(queue, 5)

lift.theLift()#

lift.get_status()
# 