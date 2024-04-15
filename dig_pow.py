def dig_pow(n, p):
    sum = 0
    for num in str(n):
        sum += int(num)**p
        p += 1
    if sum % n == 0: return sum / n
    return -1

print(dig_pow(89, 1))