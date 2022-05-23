def solution(s):
    length = len(s)
    answer = length
    for i in range(1, length // 2 + 1):
        answer = min(answer, len(compression(i, s)))
    return answer


def compression(step, s):
    compressed_stirg = ''
    prev = s[0: step]
    repeat = 1
    # 압축 시작
    for i in range(step, len(s), step):
        next_unit = s[i: i + step]
        if prev == next_unit:
            repeat += 1
        else:
            compressed_stirg += str(repeat) + prev if repeat > 1 else prev
            prev = next_unit
            repeat = 1
    # else문에 안걸린 마지막 문자열 붙여주기
    compressed_stirg += str(repeat) + prev if repeat > 1 else prev
    return compressed_stirg
