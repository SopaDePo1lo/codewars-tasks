def unique_in_order(sequence):
    if list(sequence) == []:
        return []
    elif len(sequence) == 1:
        return list(sequence)
    result, initial, last = [], sequence[0], sequence[-1]
    sequence = sequence[1:]
    for i, element in enumerate(sequence):
        print(f'{initial}; {element} - i')
        if initial != element and i!=len(sequence)-1:
            result.append(initial)
            initial = element
        if i == len(sequence)-1 and initial!=element:
            result.extend([initial, element])
    if last != result[-1] or len(result) == 0:
        result.append(last)
    return result
 
 #horrible solution btw, i know

def unique_in_order2(sequence):
    if list(sequence) == []:
        return []
    elif len(sequence) == 1:
        return list(sequence)
    result, initial, last = [], sequence[0], sequence[-1]
    sequence = sequence[1:]
    for i, element in enumerate(sequence):
        if initial != element and i!=len(sequence)-1:
            result.append(initial)
            initial = element
        if i == len(sequence)-1 and initial!=element:
            result.extend([initial, element])
    try:
        if last != result[-1]:
            result.append(last)
    except IndexError:
        result.append(last)
    return result

# print(unique_in_order(['E', 'E', 'E', 'E', 'E', 'T', 'A', 'A', 'A', 'A', 'A', 'j', 'j', 'j', 'j', 'j', 'P', 'P', 'L', 'L', 'L', 'L', 'L', 'z', 'z', 'z', 'l', 'l', 'Y', 'Y', 'Y', 'Y', 'X', 'W', 'g', 'g', 'g', 'g', 'g', 'm', 'o', 'o']))
# print(unique_in_order("AA"))

def unique_in_order_x(_sequence):
    res, prev = [], None
    for i in _sequence:
        if i != prev:
            res.append(i)
            prev = i
    return res

print(unique_in_order_x("AAAABBBCCDAABBB"))