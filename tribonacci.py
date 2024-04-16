def tribonacci(signature, n):
    for i in range(2, n-1):
        signature.append(signature[i-2] + signature[i-1] + signature[i])
    return signature[0:n]

print(tribonacci([1, 1, 1], 10))
print(tribonacci([300, 200, 100], 0))