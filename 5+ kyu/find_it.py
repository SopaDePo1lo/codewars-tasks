def find_it(seq):
    return [i for i in seq if seq.count(i)%2][0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))