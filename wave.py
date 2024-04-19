def wave(people: str):
    return [f'{people[:i]}{_l.upper()}{people[i+1:]}' for i, _l in enumerate(people) if _l in list('qwertyuiopasdfghjklzxcvbnm')]

print(wave("hello"))