def sort_array(_arr):
    _odd = iter(sorted([_i for _i in _arr if _i%2!=0]))
    return [next(_odd) if el % 2 else el for _i, el in enumerate(_arr)]

print(sort_array([5, 3, 2, 8, 1, 4])) #[1, 3, 2, 8, 5, 4]