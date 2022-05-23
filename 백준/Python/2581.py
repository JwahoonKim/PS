from math import sqrt

def isPrime(num):
    if num == 2:
        return True
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

m = int(input())
n = int(input())

primeNumbers = []
sum = 0

for i in range(m, n + 1):
    if i == 1:
        continue
    if isPrime(i) == True:
        primeNumbers.append(i)
        sum += i

if len(primeNumbers) == 0:
    print(-1)
else:
    print(sum)
    print(primeNumbers[0])
