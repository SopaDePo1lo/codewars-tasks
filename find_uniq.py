def find_uniq(arr) -> int:
    _a1, _a2 = arr[0:2]
    arr = list(set(arr))
    if _a1 == _a2:
        arr.remove(_a1)
    return arr[0]


def find_uniq_x(arr: list[int]) -> int:
    return [_i for _i in set(arr) if arr.count(_i) == 1][0]

print(find_uniq([1, 1, 3]))