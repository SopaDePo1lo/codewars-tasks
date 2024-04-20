#after seeing the other ways people solved this... i might just get depression at this point
def sum_of_intervals(intervals) -> int:
    intervals = sorted(intervals)
    sum : int = 0
    found = True
    while found!=False:
        if len(intervals) == 1: return intervals[0][1] - intervals[0][0]
        for _i in range(len(intervals)-1):
            _overlapping, arr = check_for_overlapping(intervals[_i], intervals[_i+1])
            if _overlapping:
                found = True
                del intervals[_i]
                intervals[_i] = arr
                break
            else:
                found = False

    for interval in intervals:
        _start, _end = interval
        sum += _end-_start
    return sum

def check_for_overlapping(_buf1: tuple[int, int], _buf2: tuple[int, int]) -> tuple[bool, tuple]:
    _start1, _end1 = _buf1
    _start2, _end2 = _buf2
    if max(_start1,_start2) <= min(_end1,_end1):
        return True, (min(_start1, _start2), max(_end1, _end2))
    return False, ()


for x, y in ([(0, 20), (-100_000_000, 10), (30, 40)]):
    print(f'{x} - {y}')

# print(check_for_overlapping((1, 5), (1, 5)))
print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))
print(sum_of_intervals([(1, 5), (1, 5)]))
print(sum_of_intervals([(1, 5)]))