def last_digit(lst: list):
    if lst == []: return 1
    _power_arr, _pow = lst[:-1], lst[-1]
    for i in range(len(_power_arr)):
        _pow = _power_arr[-i-1] ** (_pow if _pow < 4 else _pow % 4 + 4) #dont understand why this works
    return _pow % 10

print(last_digit([12, 30, 21]))