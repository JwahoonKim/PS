n = int(input())
exp = input()
stack = []
numbers = []
numDict = {}
oper = ['+', '-', '*', '/']

for _ in range(n):
    numbers.append(int(input()))

for e in exp:
    if e in oper:
        continue
    else:
        numDict[e] = numbers[ord(e) - ord('A')]

for e in exp:
    if e in oper:
        second = stack.pop()
        first = stack.pop()
        if e == '+':
            result = first + second
        elif e == '-':
            result = first - second
        elif e == '/':
            result = first / second
        else:
            result = first * second
        stack.append(result)
    else:
        stack.append(numDict[e])

print(f'{stack[0]:.2f}')
