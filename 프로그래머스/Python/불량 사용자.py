from itertools import product as p


def solution(user_id, banned_id):
    answer = 0
    combs = []
    cases = []
    for b_id in banned_id:
        now = []
        for u_id in user_id:
            if len(b_id) == len(u_id):
                for i in range(len(b_id)):
                    if b_id[i] == '*' or b_id[i] == u_id[i]:
                        if i == len(u_id) - 1:
                            now.append(u_id)
                    else:
                        break
        cases.append(now)

    for case in list(p(*cases)):
        case = set(case)
        if len(case) == len(banned_id):
            if case not in combs:
                answer += 1
                combs.append(case)
    return answer
