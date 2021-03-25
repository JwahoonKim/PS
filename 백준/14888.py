from itertools import permutations as p

INF = int(10e10)
min = INF
max = -INF

n = int(input())
numbers = list(map(int, input().split()))
numOfOper = list(map(int, input().split()))
operator = ["+", "-", "*", "//"]
totalOperator = []
for i in range(4):
    totalOperator.extend([operator[i]] * numOfOper[i])

Case = list(p(totalOperator, sum(numOfOper)))

for case in Case:
    res = numbers[0]
    numCur = 1
    operCur = 0
    while numCur < len(numbers):
        if case[operCur] == "+":
            res += numbers[numCur]
        elif case[operCur] == "-":
            res -= numbers[numCur]
        elif case[operCur] == "*":
            res *= numbers[numCur]
        else:
            if res < 0:
                res = -(-res // numbers[numCur])
            else:
                res //= numbers[numCur]
        numCur += 1
        operCur += 1
    if res > max:
        max = res
    if res < min:
        min = res

print(max)
print(min)
