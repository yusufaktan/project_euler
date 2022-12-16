arr = []
for i in range(1, 21):
    arr.append(i)

def check(num):
    for j in arr:
        if num % j != 0:
            return False
    return True

num = 200000000
while True:
    if check(num):
        break
    num +=1

print(num)