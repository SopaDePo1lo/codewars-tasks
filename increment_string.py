def increment_string(_str):
    if [i for i in _str if i.isdigit()] == []: return f'{_str}1'
    num = int(''.join([i for i in _str if i.isdigit()]))
    _str = _str[:-len(str(num))]
    if len(str(num+1)) == len(str(num)) and len([i for i in _str if i.isdigit()]) != len(str(num)): return _str+str(num+1)
    return _str[:-1]+str(num+1)

print(increment_string("foobar99"))