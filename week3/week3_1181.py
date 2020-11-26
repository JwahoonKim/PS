n = int(input())
arr = []
for i in range(n):
    arr.append(input())

arr = sorted(arr, key = lambda x : (len(x), x))

for i in range(n-1): #range(n)까지하면 인덱스 벗어남
    if(arr[i] != arr[i+1]): #중복 제거용
        print(arr[i])

#마지막 항은 for문에 없었으니 추가..  > 이거 개선해야됨
print(arr[n-1])