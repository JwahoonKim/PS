def solution(n):
    answer = ''
    k = 0
    while(1):
        if 3 ** k > n:
            break
        else:
            k += 1
    for i in range(k - 1, -1):
        digit = n // (3 ** i)
        if digit == 1:
            answer += '1'
        elif digit == 2:
            answer += '2'
        else:
            answer += '4'
        n %= (3 ** i)

    return answer