import sys
#pypy 안쓰고 더 최적화 못하나?
n, m = map(int, input().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)
flag = 0

while(start <= end):
    sum = 0
    mid = (start + end) // 2
    for leng in tree:
        if(leng > mid):
            sum += leng - mid
    if sum >= m:
        flag = mid
        start = mid + 1
    else: end = mid - 1

print(flag)
