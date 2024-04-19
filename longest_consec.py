def longest_consec(_buf, _step):
    if _buf == [] or _step <= 0 or len(_buf) < _step: return ''
    _arr = [_buf[_i:_i+_step] for _i in range(len(_buf)-_step+1)]
    return [''.join(_i) for _i in _arr if sum([len(_j) for _j in _i]) == max([sum([len(_j) for _j in _i]) for _i in _arr])][0]

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))
print(longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 0))