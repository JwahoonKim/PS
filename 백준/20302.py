import sys, math
input = sys.stdin.readline

n = int(input())
express = list(map(str, input().split()))

multiple = 1
divide = 1
flag = 1

for i in express:
    if i == '*':
        flag = 1
        flag = 0
    else:
        num = int(i)
        if flag == 1:
            multiple *= num
        else:
            divide *= num

result = 'mint chocolate' if multiple % divide == 0 else 'toothpaste'
print(result)


