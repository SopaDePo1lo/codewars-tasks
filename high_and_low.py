def high_and_low(numbers):
    numbers = str(numbers).split(" ")
    print([int(num) for num in numbers ])
    return f'{max([int(num) for num in numbers])} {min([int(num) for num in numbers ])}'

print(high_and_low('8 3 -5 42 -1 0 0 -9 4 7 4 -4'))