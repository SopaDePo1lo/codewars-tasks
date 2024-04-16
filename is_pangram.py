def is_pangram(s):
    lst = list('qwertyuiopasdfghjklzxcvbnm')
    return len(set([i for i in list(s.lower()) if i in lst])) == 26

print(is_pangram("Cwm fjord bank glyphs vext quiz"))