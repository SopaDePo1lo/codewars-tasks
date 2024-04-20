def move_zeros(buf):
    for i, element in enumerate(buf):
        if element == 0:
            del buf[i]
            buf.append(0)
    return buf

def move_zeros2(buf):
    amount = buf.count(0)
    buf = list(filter((0).__ne__, buf))
    buf.extend([0] * amount)
    return buf

# returns [1, 1, 2, 1, 3, 0, 0]
print(f'{move_zeros2([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0])}')
