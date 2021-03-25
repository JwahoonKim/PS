T = int(input())
for _ in range(T):
    numList = list(map(int, input().split()))
    numList.sort()
    print(numList[-3])
