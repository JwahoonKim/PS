def time_to_sec(play_time):
    h, m, s = list(map(int, play_time.split(':')))
    return h * 3600 + m * 60 + s


def sec_to_time(answer_sec):
    h = answer_sec // 3600
    m = (answer_sec % 3600) // 60
    s = answer_sec % 60
    HH = str(h) if h > 9 else f'0{h}'
    MM = str(m) if m > 9 else f'0{m}'
    SS = str(s) if s > 9 else f'0{s}'
    return f'{HH}:{MM}:{SS}'


def solution(play_time, adv_time, logs):
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    acc_sum = [0] * (play_time_sec + 1)

    for log in logs:
        start, end = log.split("-")
        start_sec = time_to_sec(start)
        end_sec = time_to_sec(end)
        acc_sum[start_sec] += 1
        acc_sum[end_sec] -= 1

    for i in range(len(acc_sum) - 1):
        acc_sum[i + 1] += acc_sum[i]

    for i in range(len(acc_sum) - 1):
        acc_sum[i + 1] += acc_sum[i]

    max_view = acc_sum[adv_time_sec]
    answer_sec = 0
    for i in range(1, play_time_sec - adv_time_sec):
        if max_view < acc_sum[adv_time_sec + i] - acc_sum[i]:
            max_view = acc_sum[adv_time_sec + i] - acc_sum[i]
            answer_sec = i + 1

    return sec_to_time(answer_sec)
