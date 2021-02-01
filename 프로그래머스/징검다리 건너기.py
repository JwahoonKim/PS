# 0이 연속적으로 K번 나오면 False를 아니면 True를 리턴하는 함수
def serialZero(arr, k):
    count = 0
    for i in arr:
        if i == 0:
            count += 1
            if count == k:
                return False
        else:
            count = 0
    return True


def solution(stones, k):
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2
        # i - mid 가 음수면 0 이 되게끔 list comprehension
        temp = [i - mid if i - mid >= 0 else 0 for i in stones]
        if serialZero(temp, k) == True:  # 문제가 없을 경우
            left = mid + 1
        else:
            right = mid - 1  # 0 이 연속적으로 k 만큼 있어서 문제가 되는 경우
    return left


if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))