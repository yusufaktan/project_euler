fibo = [1]

a = 1
b = 1
c = 0

while True:
    if ((a + b) < 4000000):
        c = a + b
        a = b
        b = c
        fibo.append(b)
    else:
        break

sum = 0
for i in fibo:
    if i % 2 == 0:
        sum +=i
        
print(sum)


