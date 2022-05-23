from math import sqrt
from itertools import permutations as p

# 첫 풀이


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
    # 아랫 줄은 list(numbers) 했으면 됐을 듯!
    number = [i for i in numbers]
    for i in range(1, length + 1):
        arr = list(p(number, i))
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

# 두 번째 풀이


def solution(numbers):
    answer = 0
    num_list = list(numbers)
    num_set = set()
    for i in range(1, len(numbers) + 1):
        num_pm = list(p(num_list, i))
        for j in num_pm:
            number = ""
            for num in j:
                number += num
            if number[0] != '0':
                num_set.add(int(number))
    for k in num_set:
        if isPrime(k):
            answer += 1
    return answer
