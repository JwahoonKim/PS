import math

def solution(w,h):
    answer = 0
    x = min(w, h)
    y = max(w, h)
    if x == y:
        return x ** 2 - x
    if x == 1:
        return 0
    for i in range(1, x):
        answer += 2 * math.floor(y * i / x)
    return answer