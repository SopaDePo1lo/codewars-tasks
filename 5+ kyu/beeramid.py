def beeramid(bonus, price):
	if bonus <= 0: return 0
	beers, levels, beers_used = int(bonus/ price), 1, 0
	while beers_used <= beers:
		beers_used += levels**2
		levels += 1
	return levels-2

print(beeramid(454, 5))