from itertools import product
from typing import List


def calc(user: List, emoticons: List, case: tuple):
    total_cost = 0
    thr_sale_rate, thr_total_cost = user

    for idx, sale_rate in enumerate(case):
        if sale_rate < thr_sale_rate:
            continue
        total_cost += round(emoticons[idx] * (1 - sale_rate / 100))

    return [thr_total_cost <= total_cost, total_cost]


def solution(users: List, emoticons: List):
    answer = [0, 0]
    sales = [10, 20, 30, 40]
    cases = product(sales, repeat=len(emoticons))

    for case in cases:
        plus_user_count = 0
        total_cost = 0
        for user in users:
            is_plus, cost = calc(user, emoticons, case)
            if is_plus:
                plus_user_count += 1
            else:
                total_cost += cost
        if answer[0] < plus_user_count:
            answer = [plus_user_count, total_cost]
        elif answer[0] == plus_user_count:
            if answer[1] < total_cost:
                answer[1] = total_cost
    return answer


print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))