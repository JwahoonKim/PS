from itertools import permutations

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
print(totalOperator)
max = -INF
min = INF

numComb = list(permutations(numbers, len(numbers)))
operComb = list(permutations(totalOperator, len(totalOperator)))

for number in numComb:
    for oper in operComb:
        result = number[0]
        for i in range(n - 1):
            if oper[i] == "+":
                result += number[i + 1]
            elif oper[i] == "-":
                result -= number[i + 1]
            elif oper[i] == "*":
                result *= number[i + 1]
            elif oper[i] == "//":
                if result < 0:
                    result = -(-result // number[i + 1])
                else:
                    result //= number[i + 1]
        if result > max:
            max = result
        elif result < min:
            min = result
print(max)
print(min)