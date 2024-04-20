def to_jaden_case(_input: str) -> str:
    return ' '.join([f'{word.capitalize()}' for word in _input.split(' ')])
print(to_jaden_case("How can mirrors be real if our eyes aren't real"))