from typing import List


def get_expire_date(privacy, term_dict):
    date, term = privacy.split()
    date_to_int(date)
    after = term_dict[term]
    return date_to_int(date) + after


def date_to_int(date):
    y, m, d = map(int, date.split('.'))
    return y * 28 * 12 + m * 28 + d


def solution(today: str, terms: List, privacies: List):
    term_dict = dict()
    for term in terms:
        a, b = term.split(" ")
        term_dict[a] = int(b) * 28

    answer = []
    for idx, privacy in enumerate(privacies, 1):
        expire_date = get_expire_date(privacy, term_dict)
        today_int = date_to_int(today)
        if today_int >= expire_date:
            answer.append(idx)
    return answer


print(solution("2022.05.19",	["A 6", "B 12", "C 3"],	["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))