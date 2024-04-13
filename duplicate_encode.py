def duplicate_encode(word : str):
    letter_map = count_letters(word)
    word_list = list(word)
    for i, letter in enumerate(word_list):
        if letter_map[letter] > 1:
            word_list[i] = ')'
        else:
            word_list[i] = '('
    return ''.join(word_list)

def count_letters(_word: str) -> dict[str, int]:
    _buf = {}
    for letter in _word:
        if letter in _buf:
            _buf[letter] += 1
        else:
            _buf[letter] = 1
    return _buf


def duplicate_encode_better(word : str) -> str:
    word_list = list(word.lower())
    for i, letter in enumerate(word_list):
        if word.lower().count(letter) > 1:
            word_list[i] = ')'
            continue
        word_list[i] = '('
    return ''.join(word_list)

print(duplicate_encode_better("(()))())())()("))