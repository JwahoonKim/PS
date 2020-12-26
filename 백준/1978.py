import math
n = int(input())
number = list(map(int,input().split()))
count = 0
for num in number:
    if num == 1:
        continue
    if num == 2 or num == 3:
        count += 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            break
        if i == int(math.sqrt(num)):
            count += 1
        
print(count)