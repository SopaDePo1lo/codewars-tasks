def make_readable(seconds):

    pass

def product_fib_x(_prod):
    sum, i = 0, 0;
    x, y = 0, 1
    while i <= _prod:
        x, y = y, x+y
        sum += x
        i+= 1
    return sum*4

print(product_fib_x(5))