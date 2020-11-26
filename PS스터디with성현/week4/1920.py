#데이터 받기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

# 이진탐색으로 위해 n_list 정렬
n_list.sort()

# 특정 수가 배열에 존재하는지 확인하는 함수 (이진탐색)
def check(arr, x):
    start = 0 
    end = len(arr) - 1
    # 이진 탐색으로 찾는 반복 과정
    while(start <= end):
        mid = (start + end) // 2
        if(arr[mid] > x):
            end = mid - 1
        elif(arr[mid] < x):
            start = mid + 1
        elif(arr[mid] == x):
            return 1
    return 0
    
#m_list 에서 숫자 하나씩 뽑아서 n_list에 존재하는지 check  
for i in m_list:
    exs = check(n_list, i)
    print(exs)
