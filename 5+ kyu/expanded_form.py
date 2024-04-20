def expanded_form(num):
    arr, _s = [], []
    for _n in range(len(str(num))):
        arr.append(num%10)
        num = int(num/10)
    for i, _i in enumerate(arr[::-1]):
        if _i == 0:
            pass
        else:
            _s.append(f'{_i*(10**(len(arr) - i- 1))}')
        pass
    return ' + '.join(_s)

print(expanded_form(70304))