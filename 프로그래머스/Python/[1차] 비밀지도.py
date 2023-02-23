from typing import List


def ten_to_bin(number, n):
    binary = str(bin(number))[2:]
    return "0" * (n - len(binary)) + binary


def union(str1, str2):
    res = ""
    for a, b in zip(str1, str2):
        res += "1" if a == "1" or b == "1" else "0"
    return res


def solution(n, arr1: List, arr2: List):
    map = [[0] * n for _ in range(n)]

    for idx, number in enumerate(arr1):
        map[idx] = ten_to_bin(number, n)

    for idx, number in enumerate(arr2):
        map[idx] = union(map[idx], ten_to_bin(number, n))

    for idx, r in enumerate(map):
        r = r.replace("1", "#").replace("0", " ")
        map[idx] = r

    return map

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))