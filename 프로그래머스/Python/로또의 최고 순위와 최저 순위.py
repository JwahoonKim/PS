def solution(lottos, win_nums):
    rank = [1, 2, 3, 4, 5, 6, 6]
    match_num = [6, 5, 4, 3, 2, 1, 0]
    lotto_dict = dict(zip(match_num, rank))
    my_set = set(filter(lambda x : True if x != 0 else False, lottos))
    match_count = len(my_set & set(win_nums))
    return [lotto_dict[match_count + 6 - len(my_set)], lotto_dict[match_count]]


