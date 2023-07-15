import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
left_answer = arr[left]
right_answer = arr[right]

answer = left_answer + right_answer
while left < right:
    result = arr[left] + arr[right]
    if abs(answer) > abs(result):
        left_answer = arr[left]
        right_answer = arr[right]
        answer = result

    if answer == 0:
        break

    if result > 0:
        right -= 1
    else:
        left += 1

print(left_answer, right_answer)
