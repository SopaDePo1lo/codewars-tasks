def next_smaller(n: int) -> int:
    _n : str
    if sorted(list(str(n))) == str(n)[0]:
        _n = str(n)[0] + ''.join(sorted(list(str(n)[1:])))
    elif int(''.join(sorted(list(str(n)[1:])))) < int((str(n)[1:])):
        _n = str(n)[0] + ''.join(sorted(list(str(n)[1:])))
    else:
        _n = ''.join(sorted(list(str(n))))
    if int(_n) == n:
        return -1
    return int(_n)



print(next_smaller(21))