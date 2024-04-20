def perimeter(n):
    sum, i, x, y = (0, 0, 0, 1);
    while i <= n:
        x, y = y, x+y
        sum += x
        i+= 1
    return sum*4

print(perimeter(7))