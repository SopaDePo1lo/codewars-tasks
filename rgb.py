def rgb(r, g, b):
    colours, res = [r, g, b], ''
    for colour in colours:
        colour = max(0, min(colour, 255))
        res += str(hex(colour).split('x')[-1]).rjust(2, '0').upper()
    return res

print(rgb(-20, 275, 125))