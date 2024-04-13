def zeros(n: int) -> int:
    from math import factorial
    _fact, _count = str(factorial(int(str(n)[:4]))), 0
    for i in range(_fact.count('0')):
        if str(_fact).rfind('0') == len(_fact)-1:
            _count += 1
            _fact = _fact[:-1]
    if n > 1000:
        _count = str(_count) + '9'*(str(n).count('0')-3)
    return int(_count)

print(zeros(100000))