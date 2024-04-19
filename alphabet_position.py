def alphabet_position(text):
    alph = list('qwertyuiopasdfghjklzxcvbnm')
    return ' '.join([str(ord(_l)-96) for _l in list(text.lower()) if _l in alph])



alphabet_position("The sunset sets at twelve o' clock.")