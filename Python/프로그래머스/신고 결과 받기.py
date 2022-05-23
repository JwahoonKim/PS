def solution(id_list, report, k):
    answer = { id : 0 for id in id_list }
    report_dict = { id : set() for id in id_list }
    for r in report:
        report_user, reported_user = r.split(' ')
        report_dict[reported_user].add(report_user)
    for key, value in report_dict.items():
        if len(value) >= k:
            for v in value:
                answer[v] += 1
    return list(answer.values())
    