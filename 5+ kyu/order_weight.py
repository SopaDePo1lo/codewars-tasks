def order_weight(_input: str) -> str:
    arr, weights, result = _input.split(' '), {}, []
    for element in arr:
        weights[element] = get_weight(element)
    weights = sorted(weights.items(), key=lambda x: x[1])
    for element in weights:
        weight, _ = element
        result.append(weight)
    return ' '.join(result)

def get_weight(_str: str) -> int:
    sum = 0
    for digit in _str:
        sum += int(digit)
    return sum

print(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))