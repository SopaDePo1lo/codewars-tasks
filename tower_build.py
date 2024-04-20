def tower_builder(n_floors):
    return [f'{" "*floor}{("*"*(n_floors*2-1))[floor:-floor]}{" "*floor}' if floor != 0 else '*'*(n_floors*2-1) for floor in range(n_floors) ][::-1]

print(tower_builder(1))