def order(sentence):
    words, words_copy = sentence.split(), sentence.split().copy()
    for i, word in enumerate(words.copy()):
        _i = int(get_pos(word))
        words[_i-1] = words_copy[i]
    return ' '.join(words)

def get_pos(word) -> int:
    for l in word:
        if l.isdigit(): return l
    return 0

print(order("4of Fo1r pe6ople g3ood th5e the2"))