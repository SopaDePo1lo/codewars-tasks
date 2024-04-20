def spin_words(sentence):
    words = sentence.split(" ")
    res = []
    for word in words:
        if len(word) >= 5:
            res.append(inverse_word(word))
        else:
            res.append(word)
    return ' '.join(res)

def inverse_word(buf):
    buf = list(buf)
    for i in range(int(len(buf)/2)):
        buf[i], buf[-(i+1)] = buf[-(i+1)] , buf[i]
    return ''.join(buf)

print(inverse_word('dsfghjkl;'))

print(spin_words("Welcome")) #emocleW