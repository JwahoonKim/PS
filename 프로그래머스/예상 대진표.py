def solution(n, a, b):
    answer = 1
    # 큰 값을 b로
    if a > b:
        a, b = b, a
    while(1):
        if b % 2 == 0 and b - 1 == a:
            return answer
        else:
            answer += 1
            a = (a + 1) // 2
            b = (b + 1) // 2
