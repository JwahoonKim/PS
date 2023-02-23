from typing import List


def solution(survey: List, choices: List):
    scores = [0] * 4
    score_dict = { 1:-3, 2:-2, 3:-1, 4:0, 5:1, 6:2, 7:3 }
    type_dict = { "RT":0, "CF":1, "JM":2, "AN":3 }

    for t, c in zip(survey, choices):
        if t[1] < t[0]:
            c = 8 - c
            t = t[1] + t[0]
        score = score_dict[c]
        scores[type_dict[t]] += score

    answer = ""
    answer += "R" if scores[0] <= 0 else "T"
    answer += "C" if scores[1] <= 0 else "F"
    answer += "J" if scores[2] <= 0 else "M"
    answer += "A" if scores[3] <= 0 else "N"
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],	[5, 3, 2, 7, 5]))