from itertools import permutations
import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
numbers = list(map(int, input().split()))
numberOfOperator = list(map(int, input().split()))
operator = ["+", "-", "*", "//"]
# operator가 각각 몇 번씩 나오는지에 대한 정보 리스트
totalOperator = []
for i in range(4):
    for j in range(numberOfOperator[i]):
        totalOperator.append(operator[i])

max = -INF
min = INF

operPermutation = list(permutations(totalOperator, len(totalOperator)))

for oper in operPermutation:
    result = numbers[0]
    for i in range(n - 1):
        if oper[i] == "+":
            result += numbers[i + 1]
        elif oper[i] == "-":
            result -= numbers[i + 1]
        elif oper[i] == "*":
            result *= numbers[i + 1]
        elif oper[i] == "//":
            if result < 0:
                result = -(-result // numbers[i + 1])
            else:
                result //= numbers[i + 1]
    if result > max:
        max = result
    if result < min:
        min = result
print(max)
print(min)