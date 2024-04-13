def two_sum(numbers, target):
	for i, el1 in enumerate(numbers):
		for j, el2 in enumerate(numbers):
			if i != j and el1+el2 == target:
				return (i, j)




print(two_sum([1, 2, 3], 4)) # returns (0, 2) or (2, 0)
two_sum([3, 2, 4], 6) # returns (1, 2) or (2, 1)