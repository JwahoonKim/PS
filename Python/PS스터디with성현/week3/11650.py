n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))

#arr = sorted(arr, key = lambda x : (x[0], x[1] ))
#위에 코드는 시간초과
arr.sort() # -> 이거 어떻게 개선하지

for i in range(n):
    print(arr[i][0],arr[i][1])