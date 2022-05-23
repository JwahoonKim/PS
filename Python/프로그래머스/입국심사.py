from typing import DefaultDict


def solution(n, times):
    left = 1
    right = min(times) * n
    while left <= right:
        count = 0
        mid = (left + right) // 2
        for time in times:
            count += mid // time
        if count >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))

if __name_- == "__main__":
    n = 6
    times = [7, 10]