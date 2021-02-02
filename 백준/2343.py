import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
# 이분탐색용 left, right
left = 1
right = max(arr) * n
answer = right

while left <= right:
    flag = False
    mid = (left + right) // 2
    count = 0
    sum = 0
    # arr의 원소 중 가장 큰 값이 블루레이 크기보다 크면 블루레이 길이 늘려야함
    if max(arr) > mid:
        left = mid + 1
        continue
    for i in range(len(arr)):
        if sum + arr[i] <= mid:
            sum += arr[i]
            # 마지막항 처리
            if i == len(arr) - 1:
                count += 1
        else:
            count += 1
            sum = arr[i]
            # 마지막항 처리
            if i == len(arr) - 1:
                count += 1
    if count > m:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)
# 정답출력
print(answer)
