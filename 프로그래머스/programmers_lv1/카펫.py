# n + m = (brown / 2 ) + 2
# nm = brown + yellow
import math


def solution(brown, yellow):
    a = (brown + 4) // 2
    b = 4 * (brown + yellow)
    # 근의 공식
    row = (a + math.sqrt(a ** 2 - 4 * (brown + yellow))) // 2
    col = (a - math.sqrt(a ** 2 - 4 * (brown + yellow))) // 2
    return [int(row), int(col)]
