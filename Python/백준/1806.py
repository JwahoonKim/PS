n, s = map(int, input().split())
numbers = list(map(int, input().split()))
sum = numbers[0]
answer = 100001
left, right = 0, 1
canMake = False

if sum >= s:
    answer = 1
while(left < n):
    if sum < s and right < n:
        sum += numbers[right]
        right += 1
    else:
        sum -= numbers[left]
        left += 1
    if sum >= s:
        answer = min(answer, right - left)
        canMake = True

if canMake:
    print(answer)
else:
    print(0)