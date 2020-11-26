n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int,input().split())))
# 이상한 풀이    
arr.sort()  # y가 같으면 x 순으로 정렬해주기 위함..?
arr_sort = sorted(arr, key = lambda x : x[1])
 # sort 제공 안했으면 어떻게함?

for i in range(n):
    print(arr_sort[i][0],arr_sort[i][1])