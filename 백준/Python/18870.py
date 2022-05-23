import sys, bisect
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
numset = list(set(numbers))
numset.sort()
for i in range(len(numbers)):
    now = numbers[i]
    index = bisect.bisect_left(numset, now)
    numbers[i] = index

print(' '.join(map(str, numbers)))