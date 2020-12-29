from bisect import bisect_left,bisect_right

#데이터 받기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
count_list = []
# 이진탐색으로 위해 n_list 정렬
n_list.sort()

def counter(arr, x):
    right = bisect_right(arr, x)
    left = bisect_left(arr, x)
    return right - left

for i in m_list:
    count = counter(n_list, i)
    count_list.append(count)
    
for i in count_list:
    print(i, end = " ")