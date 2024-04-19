def disemvowel(s_):
    vowels = list('AOEUIaoeui')
    return "".join([c for c in f'{str(s_)}' if c not in vowels])

print(disemvowel("inB`D\\H u UATj!\\IAeEFL]arxk UUuJ! PGoOIl(Za'KE"))