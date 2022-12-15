arr=[]

def check(number):
    number=str(number)
    if(number == number[::-1]):
        number=int(number)
        arr.append(number)

for i in range(999):
    for k in range(999):
        check(i*k)

max=arr[0]

for i in range(len(arr)):
    if(max<arr[i]):
        max=arr[i]

print(max)