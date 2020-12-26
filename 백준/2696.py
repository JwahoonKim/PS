import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    data = list(map(int, input().split())
    numberOfMedian = (N + 1) // 2
    oddNumber = list(range(1, N + 1, 2))
    
    print(numberOfMedian)

    for odd in oddNumber:
        tempData = sorted(data[:odd])
        medianIndex = odd // 2
        print(tempData[medianIndex], end = ' ')
    print('')


