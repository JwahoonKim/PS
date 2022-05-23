import math

def convert(n, k):
    result = ''
    while n:
        div, mod = divmod(n, k)
        n = div
        result = str(mod) + result
    return result

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
             return False
    return True

def getNumberArray(n):
    return map(int, filter(lambda x : x != '', n.split('0')))

def solution(n, k):
    answer = 0
    convertedNumber = convert(n, k)
    numberArray = getNumberArray(convertedNumber)
    for num in numberArray:
        if isPrime(num):
            answer += 1
    return answer
    