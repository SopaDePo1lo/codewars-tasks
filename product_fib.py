# def product_fib1(_prod):
#     i = 0
#     while True:
#         _sum = fibonacci(i) * fibonacci(i+1)
#         if _sum == _prod:
#             return [fibonacci(i), fibonacci(i+1), True]
#         elif _sum > _prod:
#             return [fibonacci(i), fibonacci(i+1), False]
        # i += 1
# def fibonacci_map(_num, _arr) -> tuple[int, list[int]]:
#     if _num == 0:
#         return (0, [])
#     if _num in [1, 2]:
#         return (1, [])
#     sum = fibonacci_map(_num - 1, _arr) + fibonacci_map(_num - 2, _arr)
#     _arr.append(sum)
#     return (sum, _arr)

# def fibonacci_map(_num, _arr) -> list[int]:
#     if _num == 0:
#         return []
#     if _num in [1, 2]:
#         return []
#     sum = fibonacci_map(_num - 1, _arr) + fibonacci_map(_num - 2, _arr)
#     _arr.append(sum)
#     return (_arr)

# def product_fib(_prod):
#     arr, arr_i = [0, 1, 1], []
#     arr_i = sorted(set(fibonacci_map(10, arr_i)))
#     print(arr_i)
#     # arr.extend(arr_i)
#     return arr

# def product_fib(_prod):
#     sequence = map_fibonacci(31)
#     for i in range(len(sequence)):
#         if sequence[i] * sequence[i+1] == _prod:
#             return [sequence[i], sequence[i+1], True]
#         if sequence[i] * sequence[i+1] > _prod:
#             return [sequence[i], sequence[i+1], False]

# def product_fib(_prod):
#     arr_i, sequence = [], [0, 1, 1]
#     _, arr_i = fibonacci_array(50, arr_i)
#     sequence.extend(list(sorted(set(arr_i))))
#     for i in range(len(sequence)):
#         if sequence[i] * sequence[i+1] == _prod:
#             return [sequence[i], sequence[i+1], True]
#         if sequence[i] * sequence[i+1] > _prod:
#             return [sequence[i], sequence[i+1], False]

def create_fib_arr(_len : int) -> list[int]:
    sequence = [0, 1, 1]
    for i in range(_len):
        sequence.append(sequence[i+1]+sequence[i+2])
    return sequence

print(create_fib_arr(50))
# def fibonacci(_num):
#     if _num == 0:
#         return 0
#     if _num in [1, 2]:
#         return 1
#     return fibonacci(_num - 1) + fibonacci(_num - 2)

# def fibonacci_array(_num, _arr) -> tuple[int, list[int]]:
#     if _num in [1, 2]:
#         return (1, [])
#     uno, _ = fibonacci_array(_num - 1, _arr)
#     dos, _ =  fibonacci_array(_num - 2, _arr)
#     _arr.append(uno + dos)
#     return (uno + dos, _arr)

# arr = []
# _, arr = fibonacci_array(35, arr)
# print(sorted(set(arr)))
# def map_fibonacci(_end) -> list[int]:
#     arr = []
#     for i in range(_end):
#         arr.append(fibonacci(i))
#     return arr

# arr = [0, 1, 1]
# fibonacci_map(30, arr)
# print(map_fibonacci(35))
# print(sorted(set(arr)))
# print(product_fib(5368645897256770099340125860024713582762991612575666884636965203281404))