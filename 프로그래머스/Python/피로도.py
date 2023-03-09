from itertools import permutations


def go(k, case):
    result = 0
    for min_fatigue, use_fatigue in case:
        if k < min_fatigue:
            break
        result += 1
        k -= use_fatigue

    return result


def solution(k, dungeons):
    p = list(permutations(dungeons, len(dungeons)))

    answer = 0
    for case in p:
        answer = max(answer, go(k, case))

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))