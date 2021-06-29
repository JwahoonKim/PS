from itertools import combinations as c
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        combs = []
        for order in orders:
            combs.extend(list(map(tuple_to_str, c(order, i))))
        count = Counter(combs)
        if count:
            most_count = max(count.values())
            for menu, order_num in count.items():
                if most_count != 1 and order_num == most_count:
                    answer.append(menu)
    answer.sort()
    return answer


def tuple_to_str(a):
    a = list(a)
    a.sort()
    a = ''.join(a)
    return a
