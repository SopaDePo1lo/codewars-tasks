import itertools
def findpos(_num, _lst):
    _step = 1
    _j = 0
    while True:
        for pair in itertools.product(_lst, repeat=_step):
            _j += 1
            print(int(''.join([str(_i) for _i in pair])))
            if _num == int(''.join([str(_i) for _i in pair])):
                return _j
        _step += 1




print(findpos(1337,  {1, 3, 7}))