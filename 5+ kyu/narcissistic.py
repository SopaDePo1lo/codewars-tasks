def narcissistic( value ):
    _pow = len(str(value))
    _initial_value = value
    _reference_value = 0
    while value > 10:
        _reference_value += (value%10)**_pow
        print(value%10)
        value = int(value/10) 
    _reference_value += value**_pow

    return _reference_value==_initial_value

def narcissistic_string( value ):
    _pow = len(str(value))
    _initial_value = value
    _reference_value = 0
    str_value = str(value)
    for letter in str_value:
        _reference_value += int(str_value[-1])**_pow
        str_value = str_value[:-1]
    return _reference_value==_initial_value




print(narcissistic_string(371))

