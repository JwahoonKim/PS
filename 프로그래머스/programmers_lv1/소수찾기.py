from math import sqrt
from itertools import permutations as pm


def isPrime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def solution(numbers):
    count = 0
    length = len(numbers)
    number = [i for i in numbers]
    for i in range(1, length + 1):
        arr = list(pm(number, i))
        numSet = set()
        for j in arr:
            num = ""
            for k in j:
                num += str(k)
            if num[0] == "0":
                continue
            numSet.add(int(num))
        for x in numSet:
            if isPrime(x):
                count += 1
    return count
