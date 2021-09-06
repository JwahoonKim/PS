def solution(s):
    length = len(s)
    answer = length
    for i in range(1, length // 2 + 1):
        answer = min(answer, len(compression(i, s)))
    return answer


def compression(unit, s):
    divided_arr = []
    cursor = 0
    # unit 단위로 s 쪼개기
    while(cursor < len(s)):
        divided_arr.append(s[cursor: cursor + unit])
        cursor += unit
    # 압축 시작
    cursor = 0
    repeat = 1
    now = divided_arr[0]
    comp_string = ""
    for i in range(1, len(divided_arr)):
        if divided_arr[i] == now:
            repeat += 1
        else:
            comp_string += (now if repeat == 1 else str(repeat) + now)
            now = divided_arr[i]
            repeat = 1
    # 아직 붙이지 못한 now까지 붙여주기
    if now:
        comp_string += (now if repeat == 1 else str(repeat) + now)
    return comp_string
