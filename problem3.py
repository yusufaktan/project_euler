number = 600851475143

arr = []
for i in range(2, number+1):
    if (number % i == 0):
        arr.append(i)

prime = []
for a in arr:
    for i in range(2, a):
        if (a % i) == 0:
            break
    else:
        prime.append(a)

print(max(prime))