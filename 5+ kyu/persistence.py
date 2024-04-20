def persistence(n: int) -> int:
    _i = 0
    while len(str(n)) != 1:
        _i += 1
        _arr = [int(_n) for _n in str(n)]
        n = get_mult_of_arr(_arr)
    return _i

def get_mult_of_arr(_buf: list[int]) -> int:
    res = 1
    for _i in _buf:
        res *= _i
    return res

print(persistence(39))
