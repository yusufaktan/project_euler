def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


arr = []
counter = 2
while True:
    if isPrime(counter):
        arr.append(counter)
    if len(arr) == 10001:
        break
    counter += 1

print(counter)
