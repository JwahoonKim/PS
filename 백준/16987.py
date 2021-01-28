from itertools import permutations as p
import copy

def removeSelfHit(arr):
    for i in range(len(arr)):
        if arr[i] == i + 1:
            return False
    return True

n = int(input())
answer = 0
numbers = [i for i in range(1, n + 1)]
numPermutation = list(p(numbers, n))
eggs = []
for i in range(n):
    s, w = map(int, input().split())
    eggs.append([s, w])

for i in range(len(numPermutation)):
    count = 0
    flag = False
    number = numPermutation[i]
    if removeSelfHit(number) == False:
        continue
    temp = copy.deepcopy(eggs)
    for j in range(n):
        if temp[j][0] <= 0 or temp[number[j] - 1][0] <= 0:
            continue
        temp[j][0] -= temp[number[j] - 1][1]
        temp[number[j] - 1][0] -= temp[j][1]
    for m in range(n):
        if temp[m][0] <= 0:
            count += 1
    if count > answer:
        answer = count
print(answer)