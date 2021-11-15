n = int(input())
have = sorted(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))

def binary_search(target, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if have[mid] == target:
        return True
    if have[mid] > target:
        return binary_search(target, left, mid - 1)
    return binary_search(target, mid + 1, right)

# 이진탐색으로 찾기
for card_number in cards:
    if binary_search(card_number, 0, n - 1):
        print(1, end=' ')
    else:
        print(0, end=' ')