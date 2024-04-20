def product_fib(_prod):
    sequence = create_fib_arr(31)
    for i in range(len(sequence)):
        if sequence[i] * sequence[i+1] == _prod:
            return [sequence[i], sequence[i+1], True]
        if sequence[i] * sequence[i+1] > _prod:
            return [sequence[i], sequence[i+1], False]


def create_fib_arr(_len : int) -> list[int]:
    sequence = [0, 1, 1]
    for i in range(_len):
        sequence.append(sequence[i+1]+sequence[i+2])
    return sequence

print(create_fib_arr(50))

def product_fib_x(_prod):
    x, y = 0, 1
    while x*y <= _prod:
        x, y = y, x+y
    return [x, y, x*y==_prod]