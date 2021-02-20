import math

def solution(w,h):
    answer = 0
    x = min(w, h)
    y = max(w, h)
    # 시간 줄이기용
    if x == y:
        return x ** 2 - x
    if x == 1:
        return 0
    # 직선의 방정식에서 자연수 x에 대한 치역값을 각각 floor해주고
    # 대칭이므로 * 2 해서 다 더하면 답
    for i in range(1, x):
        answer += 2 * math.floor(y * i / x)
    return answer