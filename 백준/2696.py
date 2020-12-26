import sys
input = sys.stdin.readline
# 이거 시간복잡도 왜 되냐?
T = int(input())
for i in range(T):
    N = int(input())
    divided = (N - 1) // 10 + 1
    temp = []
    data = []
    for i in range(divided):
        b = list(map(int, input().split()))
        temp.append(b)
    for i in temp:
        for j in i:
            data.append(j)
    numberOfMedian = (N + 1) // 2
    oddNumber = list(range(1, N + 1, 2))
    print(numberOfMedian)
    median = []
    for odd in oddNumber:
        tempData = sorted(data[:odd])
        medianIndex = odd // 2
        median.append(tempData[medianIndex])
    divided = (numberOfMedian - 1) // 10 + 1
    for i in range(divided):
        print(' '. join(map(str, median[i * 10 : i * 10 + 10])))