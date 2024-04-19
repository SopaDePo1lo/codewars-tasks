def array_diff(a:list[int] , b:list[int]) -> list[int]:
    return [_i for _i in a if _i not in b]

array_diff([1,2,3], [1, 2])